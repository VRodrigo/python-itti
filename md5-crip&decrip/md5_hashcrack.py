import hashlib as hl
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

def file_writer(line_w,filename="hash.txt"):
    name = filename.split(".")[0]
    #import pdb; pdb.set_trace()
    with open("{fname}-cracked.txt".format(fname=name), "a") as file_w:
        file_w.write(line_w)
    return True

def main():
    if len(sys.argv[1:]) > 4:
        print("max 2 args")
        exit()
    if sys.argv[1] == "-h" or len(sys.argv) <= 1:
        print("Use1: python3 hash_generator.py -i <filename>\n"
            "Use2: python3 hash_generator.py -I <password>")
        exit()
    if sys.argv[1] == "-i":
        hash_list = file_reader(str(sys.argv[2]))
    if sys.argv[1] == "-I":
        hash_list = [str(sys.argv[2])]
    if sys.argv[3] == "-w":
        wordlist = file_reader(str(sys.argv[4]))
        for hash in hash_list:
            hash.replace("\n", "")
            for word in wordlist:
                word_hash = generator(word.replace("\n", ""))
                if word_hash == hash.replace("\n", ""):
                    if len(hash_list) > 1:
                        file_writer(hash.
                            replace("\n", "")+" : "+ word,str(sys.argv[2]))
                    else:
                        file_writer(hash+" : "+ word)
                    break
        exit()
    else:
        print("Use1: python3 hash_generator.py -i <filename>\n"
            "Use2: python3 hash_generator.py -I <password>")
        exit()

main()