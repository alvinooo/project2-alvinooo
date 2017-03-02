from util import *

class MetadataServerHandler():

    def __init__(self, config_path, my_id):
        # Initialize block
        self.config = parse_config(config_path)
        self.id = my_id
        self.files = {}
        self.block_client = connect('localhost', int(self.config["block"]), BlockServerService.Client)

    def getFile(self, filename):
        # Function to handle download request from file
        if filename not in self.files:
            return file(filename, status=uploadResponseType.ERROR)
        self.files[filename].status = uploadResponseType.OK
        return self.files[filename]

    def storeFile(self, file):
        # Function to handle upload request
        response = uploadResponse(uploadResponseType.OK, [], [])

        # Ask block server for missing blocks
        try:
            missing = self.block_client.missingBlocks(file.hashList)
        except:
            return uploadResponse(uploadResponseType.ERROR)

        # Construct response
        if len(missing) > 0:
            response.status = uploadResponseType.MISSING_BLOCKS
            response.hashList = missing
        else:
            if file.filename not in self.files or file.version > self.files[file.filename].version:
                print "Overwriting"
                response.status = uploadResponseType.OK
                self.files[file.filename] = file
            else:
                print "Not overwriting"
                response.status = uploadResponseType.FILE_ALREADY_PRESENT

        # TEST
        print file.version
        print "missing", len(response.hashList), "blocks"
        print self.files.keys()
        # TEST
        return response

    def deleteFile(self, file):
        # Function to handle download request from file
        # TODO validation
        if file.filename not in self.files:
            print file.filename
            return response(responseType.ERROR)
        del self.files[file.filename]
        print self.files.keys()
        return response(responseType.OK)

    def readServerPort(self):
        # Get the server port from the config file.
        # id field will determine which metadata server it is 1, 2 or n
        # Your details will be then either metadata1, metadata2 ... metadatan
        # return the port
        return self.config["metadata" + self.id]

    # Add other member functions if needed
    def blocks_match(self, l1, l2):
        return len(l1) == len(l2) and all([hash1 == hash2 for hash1, hash2 in zip(l1, l2)])

# Add additional classes and functions here if needed

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print "Invocation <executable> <config_file> <id>"
        exit(-1)

    config_path = sys.argv[1]
    my_id = sys.argv[2]

    print "Initializing metadata server"
    handler = MetadataServerHandler(config_path, my_id)
    port = handler.readServerPort()
    # Define parameters for thrift server
    processor = MetadataServerService.Processor(handler)
    transport = TSocket.TServerSocket(port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # Create a server object
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "Starting server on port : ", port

    try:
        server.serve()
    except (Exception, KeyboardInterrupt) as e:
        print "\nExecption / Keyboard interrupt occured: ", e
        exit(0)
