#Import GCD, Greatest Common Divisor method
from fractions import gcd
import io
import math

# Key and alphabet size
def validateKey(key, num):
	if gcd(key, num) != 1:
		return False
	return True

def encryptMessage(message, key, alphabet):
 	out = ''
 	num = len(alphabet)
 	for symbol in message:
 		if symbol in alphabet:
 			symIndex = alphabet.find(symbol)
 			out += alphabet[(symIndex*key) % num]
 		else:
 			out += symbol
 	return out

def decryptMessage(message, key, alphabet):
	out = ''
	num = len(alphabet)
	invKey = cryptomath.modInverse(key, num)
	for symbol in message:
		if symbol in alphabet:
			symIndex = alphabet.find(symbol)
			out += alphabet[(symIndex * invKey) % num]
		else:
			out += symbol
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

	fout = open("output_mult.txt", "w")
	fout.write(out)
	fout.close()

if __name__ == '__main__':
	main()
