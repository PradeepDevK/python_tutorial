#Python version 3.x.x

import hashlib
def calculate(unsorted_dict, sha_phrase, sha_method=hashlib.sha256):
# sorting the keys of the data

    sorted_keys = sorted(unsorted_dict, key=lambda x: x.lower())

#sorting the data and concatenating "=" between the key and the value
    sorted_dict = {k: unsorted_dict[k] for k in sorted_keys}
    result = "".join(f"{k}={v}" for k, v in sorted_dict.items())

#Adding the SHA Request Phrase and preparing the string to the encryption

    result_string = f"{sha_phrase}{result}{sha_phrase}"

#Encrypting the result of the out sting with given algorithm from sha_method

    signature = sha_method(result_string.encode()).hexdigest()
    return signature

#Data Sample

dataDict = {'command':'AUTHORIZATION','access_code':'zx0IPmPy5jp1vAz8Kpg7','merchant_identifier':'CycHZxVj','merchant_reference':'XYZ9239-yu898','amount':'10000','currency':'AED','language':'en','customer_email':'test@payfort.com','order_description':'iPhone 6-S'}

print(calculate(dataDict,"018T4u7gIeNNaQUhjmNAMV&*",hashlib.sha256))