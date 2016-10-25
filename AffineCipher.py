import CaesarCipher, MultiplicativeCipher
import io
import math
from fractions import gcd

def validateKey(key, num):
	if gcd(key, num) != 1:
		return False
	keyM = key % num
	if MultiplicativeCipher.validateKey(keyM, num) != 1:
		return False
	return True

def getKeys(key, num):
	keyM = key % num
	keyC = key // num
	return (keyM, keyC)

def encryptMessage(message, key, alphabet):
	keyM, keyC = getKeys(key, len(alphabet))
	partial = MultiplicativeCipher.encryptMessage(message, keyM, alphabet)
	out = CaesarCipher.encryptMessage(partial, keyC, alphabet)
	return out


def decryptMessage(message, key, alphabet):
	keyM, keyC = getKeys(key, len(alphabet))
	partial = CaesarCipher.decryptMessage(message, keyC, alphabet)
	out = MultiplicativeCipher.decryptMessage(partial, keyM, alphabet)
	return out


def main():
	entrada = input('Input file: ')
	
	ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789,.!?;:()'
	num = len(ALPHABET)

	key = 0
	key = input('Enter key (number): ')
	key = int(key)

	while validateKey(key, num) is False:
		key = input('Sorry but this key will not work.\nPlease, enter a new key (number): ')
		key = int(key)

	key = key % num

	with open(entrada, 'r') as f:
		dados = f.readlines()
		data = ''.join(dados)

	ans = ''
	while ans.upper() != 'D' and ans.upper() != 'E':
		ans = input ('(E)ncrypt or (D)ecrypt? ')
		if ans.upper() == 'E':
			out = encryptMessage(data, key, ALPHABET)
		if ans.upper() == 'D':
			out = decryptMessage(data, key, ALPHABET)

	fout = open("output_affine.txt", "w")
	fout.write(out)
	fout.close()

if __name__ == '__main__':
	main()