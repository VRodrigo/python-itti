import hashlib as hl
from time import localtime,strftime
import sys

def generator(password):
    pass_enc = password.encode()
    hashed = hl.md5(pass_enc)
    hash = hashed.hexdigest()
    return hash

def file_reader(filename):
    lines = []
    with open(filename, "r") as file_r:
        lines = file_r.readlines()
    return lines

def file_writer(line_w):
    localdate = strftime("%Y%m%d_%H%M",localtime())
    with open("hash_file-{date}.txt".format(date = localdate), "a") as file_w:
        file_w.write(line_w+"\n")
    return True

def main():
    if len(sys.argv[1:]) > 2:
        print("max 2 args")
        exit()
    if sys.argv[1] == "-h" or len(sys.argv) <= 1:
        print("Use1: python3 hash_generator.py -i <filename>\n"
            "Use2: python3 hash_generator.py -I <password>")
        exit()
    if sys.argv[1] == "-i":
        pass_list = file_reader(str(sys.argv[2]))
        #import pdb;pdb.set_trace()
        for password in pass_list:
            file_writer(generator(password.replace("\n","")))
        exit()
    if sys.argv[1] == "-I":
        file_writer(generator(str(sys.argv[2])))
        exit()
    else:
        print("Use1: python3 hash_generator.py -i <filename>\n"
            "Use2: python3 hash_generator.py -I <password>")
        exit()

main()