import io
import math

def encryptMessage(message, key):
	lines = len(message)
	out = ''
	for i in range (0, key):
		j = i
		while j < lines:
			out += message[j]
			j += key
	return out

def decryptMessage(message, key):
	mod = (key-(len(message) % key)) % key
	lines = math.ceil(len(message)/key)
	out = ''
	for k in range(0, mod):
		if k == 0:
			message = message + '|'
		else:
			message = message[:-(k*lines)] + '|' + message[-(k*lines):]
	for i in range (0, lines):
		j = i
		while j < len(message):
			out += message[j]
			j += lines
	if mod > 0:
		return out[:-mod]		
	return out

def main():
	entrada = input('Input file: ')

	key = input('Enter key (number): ')
	key = int(key)

	with open(entrada, 'r') as f:
		dados = f.readlines()
		data = ''.join(dados)

	ans = ' '
	while ans.upper() != 'D' and ans.upper() != 'E':
		ans = input ('(E)ncrypt or (D)ecrypt? ')
		if ans.upper() == 'E':
			out = encryptMessage(data, key)
		if ans.upper() == 'D':
			out = decryptMessage(data, key)

	fout = open("output_transp.txt", "w")
	fout.write(out)
	fout.close()

if __name__ == '__main__':
	main()
