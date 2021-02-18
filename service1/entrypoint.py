import sys
import hashlib

# print("Enter hashing name ('blake2b' for best results), than message, end with ^D (in Unix)")

inp = sys.stdin.readlines()  # test example ["blake2b","b","c"] ,input from service2 via watchdog
if  inp:
    hash_func = inp[0].strip()

    if hash_func != "md5":
        print("Hashing method is not valid")

    else:
        message = '\n'.join(inp[1:]).strip()

        h = hashlib.new(hash_func)

        h.update(str.encode(message))

        print(h.hexdigest())  # Fix : added ()
else:
    print("String is empty but check on service2(localhost:5000) output to be sure")  


