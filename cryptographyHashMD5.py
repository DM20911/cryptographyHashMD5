#!/usr/bin/python 
#https://twitter.com/DM20911

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import binascii

inputFile = "/Users/dm20911/Documents/python/m2 master/WinMD5_2.exe"
#inputFile = "/Users/dm20911/Documents/python/m2 master/WinMD5.exe"
openedFile = open(inputFile,mode='rb')
readFile = openedFile.read()

digest = hashes.Hash(hashes.MD5(), backend=default_backend())
digest.update(readFile)
md5hash = digest.finalize() #Esto termina el proceso con cryptography obteniendo el MD5
parahexa = binascii.hexlify(md5hash) #Con esto pasamos el resultado a hexa

print(parahexa)
