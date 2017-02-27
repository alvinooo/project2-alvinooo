from util import *

class BlockServerHandler():

    def __init__(self, configpath):
        # Initialize using config file, intitalize state etc
        self.config = parse_config(config_path)
        self.blocks = {}

    def storeBlock(self, hashBlock):
        # Store hash block, called by client during upload
        if hashBlock.hash != hashlib.sha256(hashBlock.block).hexdigest():
            return response(responseType.ERROR)
        self.blocks[hashBlock.hash] = hashBlock
        return response(responseType.OK)

    def getBlock(self, hash):
        # Retrieve block using hash, called by client during download
        if hash not in self.blocks:
            return hashBlock(status="ERROR")
        return self.blocks[hash]

    def deleteBlock(self, hash):
        # Delete the particular hash : block pair
        if hash not in self.blocks:
            return response(responseType.ERROR)
        del self.blocks[hash]
        return response(responseType.OK)

    def readServerPort(self):
        # In this function read the configuration file and get the port number for the server
        return self.config["block"]

    # Add your functions here
    def missingBlocks(self, missing):
        # print len(self.blocks)
        # print "missing", len([hash for hash in missing if hash not in self.blocks]), "blocks"
        return [hash for hash in missing if hash not in self.blocks]

# Add additional classes and functions here if needed


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Invocation <executable> <config_file>"
        exit(-1)

    config_path = sys.argv[1]

    print "Initializing block server"
    handler = BlockServerHandler(config_path)
    # Retrieve the port number from the config file so that you could strt the server
    port = handler.readServerPort()
    # Define parameters for thrift server
    processor = BlockServerService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # Create a server object
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    print "Starting server on port : ", port

    try:
        server.serve()
    except (Exception, KeyboardInterrupt) as e:
        print "\nExecption / Keyboard interrupt occured: ", e
        exit(0)
