from fractions import gcd
import AffineCipher, TranspositionCipher


def validateKey(key, num):
	return AffineCipher.validateKey(key, num)

def encryptMessage(message, key, alphabet):
	key1 = len(message)
	new_alphabet = AffineCipher.encryptMessage(alphabet, key1, alphabet)
	out1 = TranspositionCipher.encryptMessage(message, key)
	num = len(new_alphabet)
	count = 0
	out2 = ''
	first_symbol = True
	for symbol in out1:
		symbol_index = new_alphabet.find(symbol)
		if symbol_index > -1:
			symbol_index += new_alphabet.find(new_alphabet[count])
			if first_symbol is True:
				symbol_index += len(message)
				first_symbol = False
			out2 += new_alphabet[(symbol_index) % num]
		else:
			out2 += symbol
		count = (count + 1) % num
	return out2

def decryptMessage(message, key, alphabet):
	key1 = len(message)
	new_alphabet = AffineCipher.encryptMessage(alphabet, key1, alphabet)
	out1 = ''
	count = 0
	num = len(new_alphabet)
	first_symbol = True
	for symbol in message:
		symbol_index = new_alphabet.find(symbol)
		if symbol_index > -1:
			symbol_index -= new_alphabet.find(new_alphabet[count])
			if first_symbol is True:
				symbol_index -= len(message)
				first_symbol = False 
			out1 += new_alphabet[(symbol_index) % num]
		else:
			out1 += symbol
		count = (count +1) % num
	out2 = TranspositionCipher.decryptMessage(out1, key)
	return out2


def main():
	entrada = input('Input file: ')
	key = 0
	ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789,.!?;:()'

	key = input('Enter key (number): ')
	key = int(key)
	num = len(ALPHABET)

	while validateKey(key, num) is False:
		key = input('Sorry but this key will not work.\nPlease, enter a new key (number): ')
		key = int(key)

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

	fout = open("output.txt", "w")
	fout.write(out)
	fout.close()

if __name__ == '__main__':
	main()
