from xsackslib import XSACKS as xsacks

if __name__ == "__main__":
    message = "a simple message"
    key = "casualkeytouse"
    skey = "evenbetter"
    cipher = xsacks(key, skey)
    ciphered = cipher.cipher(message)
    print(ciphered)
    print(" ^ Ciphered message and key | Secure key: " + skey)
    deciphered = cipher.decipher(ciphered[0])
    print(deciphered)
    print("^ Deciphered message and key | Secure key: " + skey)
