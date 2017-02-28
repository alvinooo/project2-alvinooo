import sys
import os

sys.path.append('gen-py')

# Thrift specific imports
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from shared.ttypes import *
from metadataServer.ttypes import *
from blockServer.ttypes import *

from metadataServer import MetadataServerService
from blockServer import BlockServerService

import hashlib

# Shared
def parse_config(path):
	config = {}
	with open(path) as config_file:
		for line in config_file.readlines():
			config[line[:line.find(':')]] = line[line.find(':')+1:].strip()
	return config

def connect(ip_addr, port, service):
	transport = TSocket.TSocket(ip_addr, port)
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = service(protocol)

	try:
		transport.open()
		return client
	except Exception as e:
		print "Error while opening socket to server\n", e
		exit(1)

# Client
def read_blocks(f, block_size=4194304):
	while True:
		block = f.read(block_size)
		if not block:
			break
		yield block

def hash_blocks(filename):
	hash_list = []
	block_list = []
	with open(filename) as f:
		for block in read_blocks(f, block_size=5):
			block_hash = hashlib.sha256(block).hexdigest()
			hash_list.append(block_hash)
			block_list.append(hashBlock(block_hash, block))
	return hash_list, block_list

def hash_blocks_directory(path):
	dir_blocks = {}
	for filename in os.listdir(path):
		file_hashes, file_blocks = hash_blocks(path + '/' + filename)
		for h, b in zip(file_hashes, file_blocks):
			dir_blocks[h] = b
	return dir_blocks

# Metadata server

# Block server