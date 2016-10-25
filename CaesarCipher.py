import io

def decryptMessage(message, key, alphabet):
	out = ''
	num = len(alphabet)
	for letter in message:
		aux = alphabet.find(letter)
		if letter in alphabet:
			out += alphabet[(aux - key) % num]	
		else:
			out += letter
	return out


def encryptMessage(message, key, alphabet):
	out = ''
	num = len(alphabet)
	for letter in message:
		aux = alphabet.find(letter)
		if letter in alphabet:
			out += alphabet[(key+aux)%num]	
		else:
			out += letter
	return out


def main():
	entrada = input('Input file: ')

	key = input('Enter key (number): ')
	key = int(key)
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	num = len(alphabet)
	
	with open(entrada, 'r') as f:
		dados = f.readlines()
		data = ''.join(dados)

	ans = ' '
	while ans.upper() != 'D' and ans.upper() != 'E':
		ans = input ('(E)ncrypt or (D)ecrypt? ')
		if ans.upper() == 'E':
			out = encryptMessage(data, key, alphabet)
		if ans.upper() == 'D':
			out = decryptMessage(data, key, alphabet)

	print('\"'+out+'\"')
	#Handle output

if __name__ == '__main__':
	main()