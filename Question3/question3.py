from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends.openssl.backend import backend
import time
import random

# digest = hashes.Hash(hashes.SHA256())
# digest.update(b"abc")
# digest.update(b"123")
# a = digest.finalize()
# print(a)

def weak():
    hits = []
    i = 0
    while(i < 1000):
        temp_num = random.randint(0,400)
        temp_num_ = bin(temp_num)
        temp_num_ = bytes(temp_num_, 'utf-8')

        digest = hashes.Hash(hashes.SHA256())
        digest.update(temp_num_)
        a = digest.finalize()
        start = time.time()

        temp = 0
        counter = 0
        while(True):
            temp += 1
            temp_bin = bin(temp)
            temp_bin = bytes(temp_bin, 'utf-8')
            print(temp_bin)

            b_digest = hashes.Hash(hashes.SHA256())

            b_digest.update(temp_bin)
            b = b_digest.finalize()
            # print("a: " , a)
            # print("b: ", b)

            if(a==b):
                hits.append(counter)
                break
            counter += 1
        i += 1
        end=time.time()

    # print("\n\n\n\n\n\n\n\n NO WAY")
    # print("start: ", start)
    # print("end: ", end)
    print("counter: ", counter)

    average = Average(hits)
    print("array: ", hits)
    print("average: ", average)


def Average(lst):
    return sum(lst) / len(lst)

# def strong():
#     i = 0;
#     while(i <= 104):


def main():
    weak()
main()
