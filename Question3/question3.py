from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends.openssl.backend import backend
import random

def weak():
    hits = []
    i = 0
    while(i < 5):
        temp_num = bin(random.getrandbits(24))
        temp_num_ = bytes(temp_num)

        digest = hashes.Hash(hashes.SHA256(), backend)
        digest.update(temp_num_)
        a = digest.finalize()

        counter = 0
        while(True):
            temp_bin = bin(random.getrandbits(24))
            temp_bin = bytes(temp_bin)
            b_digest = hashes.Hash(hashes.SHA256(), backend)
            b_digest.update(temp_bin)
            b = b_digest.finalize()

            if(a[0:6]==b[0:6]):
                hits.append(counter)
                break
            counter += 1
        i += 1
        print "Done with: ", i

    print "counter: ", counter

    average = Average(hits)
    print "Array: ", hits
    print "Average: ", average

def Average(lst):
    return sum(lst) / len(lst)

def strong():
    hits = []
    array_of_hash = []

    run_times = 0
    i = 0
    counter = 0
    isFound = False
    while(isFound == False):
        temp_num = bin(random.getrandbits(24))
        temp_num_ = bytes(temp_num)
        digest = hashes.Hash(hashes.SHA256(), backend)
        digest.update(temp_num_)
        a = digest.finalize()

        for i in range(len(array_of_hash)):
                if array_of_hash[i] == a:
                    # print("Stuck here 3")
                    isFound = True
                    return counter

        counter += 1
        array_of_hash.append(a)
        run_times += 1


def user_input():
    a = input("Enter 1 for WEAK or 2 for STRONG: ")

    if a == 1:
        weak()
    elif a == 2:
        i = 0
        hits = []
        while(i < 100):
            hits.append(strong())
            i += 1
            print "Percent Done: ", i, "%"
        average = Average(hits)
        print "Average: ", average
    else:
        print "Incorrect input try again."
        user_input()


def main():
    user_input()

main()
