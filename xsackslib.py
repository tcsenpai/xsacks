
class XSACKS:
    def __init__(self, key, skey):
        self.skey = skey
        self.key = key
        # Preparing needed variables
        self.message = ""
        self.messageCIPHER = []
        self.messageCIPHERAscii = []
        self.keyCIPHER = []
        self.keyCIPHERAscii = []
        self.keyDECIPHER = []
        self.keyDECIPHERChar = []
        self.keyDECIPHERParts = []
        self.keyDECIPHERParts1 = []
        self.keyDECIPHERParts2 = []
        self.messageDECIPHERAscii = []
        self.messageDECIPHERchar = []

        self.messageASCII = []
        self.keyASCII = []
        self.keyASCII1 = []
        self.keyASCII2 = []

        self.skeyASCII = []
        self.keyPARTS = []

        # Preparing the ascii lists
        self.keyDivider()
        self.keypartsToAscii()
        self.skeyToAscii()

    # Dividing the key in two parts
    def keyDivider(self):
        n = int(len(self.key) / 2)
        partnumber = 0
        for i in range(0, len(self.key), n):
            partnumber += 1
            if not partnumber > 2:
                self.keyPARTS.append(self.key[i : i + n])
            else:
                self.keyPARTS[1] = self.keyPARTS[1] + self.key[i : i + n]

    # Populating the ascii lists for the key parts
    def keypartsToAscii(self):
        for char in self.keyPARTS[0]:
            self.keyASCII1.append(ord(char))
        for char in self.keyPARTS[1]:
            self.keyASCII2.append(ord(char))
        for char in self.key:
            self.keyASCII.append(ord(char))

    # Populating the ascii lists for the skey
    def skeyToAscii(self):
        for char in self.skey:
            self.skeyASCII.append(ord(char))

    # Populating the ascii list for the message
    def messageToAscii(self):
        for char in self.message:
            self.messageASCII.append(ord(char))

    def cipher(self, message):
        self.message = message
        self.messageToAscii()

        # Cipher
        counterEven = 0
        counterOdd = 0
        for i in range(0, len(self.messageASCII)):
            if (i % 2) == 0:
                # Use the first part of the key
                counterEven += 1
                if counterEven > len(self.keyASCII1) - 1:
                    counterEven = 0
                cipherResult = int(self.messageASCII[i]) + int(
                    self.keyASCII1[counterEven]
                )
                while (cipherResult > 125) or (cipherResult < 32):
                    if cipherResult > 125:
                        cipherResult = 31 + (cipherResult - 125)
                    if cipherResult < 32:
                        cipherResult = 126 - (32 - cipherResult)
                self.messageCIPHER.append(cipherResult)
            else:
                # Use the second part of the key
                counterOdd += 1
                if counterOdd > len(self.keyASCII2) - 1:
                    counterOdd = 0
                cipherResult = int(self.messageASCII[i]) + int(
                    self.keyASCII2[counterOdd]
                )
                while (cipherResult > 125) or (cipherResult < 32):
                    if cipherResult > 125:
                        cipherResult = 31 + (cipherResult - 125)
                    if cipherResult < 32:
                        cipherResult = 126 - (32 - cipherResult)
                self.messageCIPHER.append(cipherResult)

        for char in self.messageCIPHER:
            self.messageCIPHERAscii.append(chr(char))

        # Cipher the key
        counterSkey = 0
        for i in range(0, len(self.keyASCII)):
            counterSkey += 1
            if counterSkey > len(self.skeyASCII) - 1:
                counterSkey = 0
            cipherResult = int(self.keyASCII[i]) + int(self.skeyASCII[counterSkey])
            while (cipherResult > 125) or (cipherResult < 32):
                if cipherResult > 125:
                    cipherResult = 31 + (cipherResult - 125)
                if cipherResult < 32:
                    cipherResult = 126 - (32 - cipherResult)
            self.keyCIPHER.append(cipherResult)

        for char in self.keyCIPHER:
            self.keyCIPHERAscii.append(chr(char))

        # Return a string
        messageCIPHERstr = ""
        for i in self.messageCIPHERAscii:
            messageCIPHERstr = messageCIPHERstr + i
        keyCIPHERstr = ""
        for i in self.keyCIPHERAscii:
            keyCIPHERstr = keyCIPHERstr + i

        return messageCIPHERstr, keyCIPHERstr

    def decipher(self, message):
        self.message = message
        self.messageToAscii()

        self.skey = str(self.skey)

        # Decipher the key
        counterSkey = 0
        for i in range(0, len(self.keyCIPHER)):
            counterSkey += 1
            if counterSkey > len(self.skeyASCII) - 1:
                counterSkey = 0
            cipherResult = int(self.keyCIPHER[i]) - int(self.skeyASCII[counterSkey])
            while (cipherResult > 125) or (cipherResult < 32):
                if cipherResult > 125:
                    cipherResult = 31 + (cipherResult - 125)
                if cipherResult < 32:
                    cipherResult = 126 - (32 - cipherResult)
            self.keyDECIPHER.append(cipherResult)

        for char in self.keyDECIPHER:
            self.keyDECIPHERChar.append(chr(char))

        # Divide the key deciphered
        n = int(len(self.key) / 2)
        partnumber = 0
        for i in range(0, len(self.keyDECIPHERChar), n):
            partnumber += 1
            if not partnumber > 2:
                self.keyDECIPHERParts.append(self.keyDECIPHERChar[i : i + n])
            else:
                self.keyDECIPHERParts[1] = (
                    self.keyDECIPHERParts[1] + self.keyDECIPHERChar[i : i + n]
                )
        # Convert it to ascii
        for char in self.keyDECIPHERParts[0]:
            self.keyDECIPHERParts1.append(ord(char))
        for char in self.keyDECIPHERParts[1]:
            self.keyDECIPHERParts2.append(ord(char))
        # Copy the functions to cipher but to decipher
        counterEven = 0
        counterOdd = 0
        for i in range(0, len(self.messageCIPHERAscii)):
            if (i % 2) == 0:
                # Use the first part of the key
                counterEven += 1
                if counterEven > len(self.keyDECIPHERParts1) - 1:
                    counterEven = 0
                cipherResult = ord(self.messageCIPHERAscii[i]) - int(
                    self.keyDECIPHERParts1[counterEven]
                )
                while (cipherResult > 125) or (cipherResult < 32):
                    if cipherResult > 125:
                        cipherResult = 31 + (cipherResult - 125)
                    if cipherResult < 32:
                        cipherResult = 126 - (32 - cipherResult)
                self.messageDECIPHERAscii.append(cipherResult)
            else:
                # Use the second part of the key
                counterOdd += 1
                if counterOdd > len(self.keyDECIPHERParts2) - 1:
                    counterOdd = 0
                cipherResult = ord(self.messageCIPHERAscii[i]) - int(
                    self.keyDECIPHERParts2[counterOdd]
                )
                while (cipherResult > 125) or (cipherResult < 32):
                    if cipherResult > 125:
                        cipherResult = 31 + (cipherResult - 125)
                    if cipherResult < 32:
                        cipherResult = 126 - (32 - cipherResult)
                self.messageDECIPHERAscii.append(cipherResult)

        for char in self.messageDECIPHERAscii:
            self.messageDECIPHERchar.append(chr(char))

        # Return a string
        messageDECIPHERAsciistr = ""
        for i in self.messageDECIPHERchar:
            messageDECIPHERAsciistr = messageDECIPHERAsciistr + i
        keyDECIPHERstr = ""
        for i in self.keyDECIPHERChar:
            keyDECIPHERstr = keyDECIPHERstr + i

        return messageDECIPHERAsciistr, keyDECIPHERstr

