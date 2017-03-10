from util import *

def upload(metadata_client, block_client, base_dir, filename):
    path = os.path.realpath(base_dir) + '/' + filename

    f = file(filename)
    f.version = os.path.getmtime(path)
    hash_list, block_list = hash_blocks(path)
    f.hashList = hash_list

    # Get missing block hashes
    try:
        metadata_response = metadata_client.storeFile(f)
        if metadata_response.status == uploadResponseType.ERROR:
            return "ERROR"
    except:
        return "ERROR"

    # Upload missing blocks if necessary
    missing_hashes = metadata_response.hashList
    missing_blocks = [b for b in block_list if b.hash in missing_hashes]

    if len(missing_blocks) == 0:
        return "OK"
    for block in missing_blocks:
        try:
            if block_client.storeBlock(block).message != uploadResponseType.OK:
                return "ERROR"
        except:
            return "ERROR"

    # Store filename to metadata mapping
    try:
        metadata_response = metadata_client.storeFile(f)
        if metadata_response.status != uploadResponseType.OK or len(metadata_response.hashList) > 0:
            return "ERROR"
    except:
        return "ERROR"

    # # TEST
    # print metadata_response
    # # TEST

    return "OK"

def download(metadata_client, block_client, base_dir, filename):
    path = os.path.realpath(base_dir) + '/' + filename
    dir_blocks = hash_blocks_directory(base_dir)

    # Get file hashes
    try:
        f = metadata_client.getFile(filename)
        if f.status == uploadResponseType.ERROR:
            return "ERROR"
    except Exception as e:
        print e
        return "ERROR"

    # Download missing blocks
    file_blocks = []
    for h in f.hashList:
        if h in dir_blocks:
            file_blocks.append(dir_blocks[h])
        else:
            try:
                block = block_client.getBlock(h)
                if block.status == "ERROR":
                    return "ERROR"
                file_blocks.append(block)
                # TEST
                print "Downloaded block"
                # TEST
            except:
                return "ERROR"

    # Construct file
    with open(path, 'w') as download:
        for b in file_blocks:
            download.write(b.block)

    return "OK"

def delete(metadata_client, block_client, base_dir, filename):
    try:
        response = metadata_client.deleteFile(file(filename))
    except:
        return "ERROR"
    return "OK"

def rpc(cmd, *args):
    ops = {"upload": upload,
           "download": download,
           "delete": delete}
    return ops[cmd](*args)

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print "Invocation : <executable> <config_file> <base_dir> <command> <filename>"
        exit(-1)

    print "Starting client"
    config = parse_config(sys.argv[1])

    metadata_client = connect("localhost", config['metadata1'], MetadataServerService.Client)
    block_client = connect("localhost", config['block'], BlockServerService.Client)

    try:
        result = rpc(sys.argv[3], metadata_client, block_client, sys.argv[2], sys.argv[4])
        print result
    except Exception as e:
        print "Caught an exception while calling RPC"
        print e
        exit(1)