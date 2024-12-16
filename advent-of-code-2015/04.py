import hashlib


def coder(key):
    prefix = "00000"
    number = 1

    while True:
        input_data = key + str(number)
        hash_result = hashlib.md5(input_data.encode()).hexdigest()
        number += 1
        if hash_result.startswith(prefix):
            return number - 1


def coder_2(key):
    prefix = "000000"
    number = 1

    while True:
        input_data = key + str(number)
        hash_result = hashlib.md5(input_data.encode()).hexdigest()
        number += 1
        if hash_result.startswith(prefix):
            return number - 1


key = input()
print(coder(key))
print(coder_2(key))
3938038
