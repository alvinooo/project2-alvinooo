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

    # Upload missing blocks
    missing_hashes = metadata_response.hashList
    missing_blocks = [b for b in block_list if b.hash in missing_hashes]

    for block in missing_blocks:
        try:
            if block_client.storeBlock(block).message == responseType.ERROR:
                return "ERROR"
        except:
            return "ERROR"

    # Try again
    try:
        metadata_response = metadata_client.storeFile(f)
        if metadata_response.status == uploadResponseType.ERROR or len(metadata_response.hashList) > 0:
            return "ERROR"
    except:
        return "ERROR"

    print metadata_response

    return "OK"

def download(metadata_client, block_client, base_dir, filename):
    path = os.path.realpath(base_dir) + '/' + filename
    existing_blocks = hash_blocks_directory(base_dir)

    # Get file hashes
    try:
        f = metadata_client.getFile(filename)
        # file_hashes = metadata_client.getFile(path) ???
        if f.status == uploadResponseType.ERROR:
            return "ERROR"
    except:
        return "ERROR"

    file_hashes = f.hashList
    missing_hashes = [b for b in file_hashes if b.hash not in existing_blocks]

    # Download missing blocks
    file_blocks = []
    for h in file_hashes:
        if h in existing_blocks:
            file_blocks.append(existing_blocks[h])
        else:
            try:
                if file_blocks.append(block_client.getBlock(h)).status == "ERROR":
                    return "ERROR"
            except:
                return "ERROR"

    # Construct file
    with open("filename", 'w') as download:
        for hash in file_blocks:
            download.write(file_blocks[hash])

    return "OK"

def delete(metadata_client, block_client, base_dir, filename):
    try:
        response = block_client.deleteFile(file(filename))
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
        dataFromServer = rpc(sys.argv[3], metadata_client, block_client, sys.argv[2], sys.argv[4])
        print dataFromServer
    except Exception as e:
        print "Caught an exception while calling RPC"
        print e
        exit(1)