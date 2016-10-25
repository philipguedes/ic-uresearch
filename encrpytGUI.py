from tkinter import *
import AffineCipher, CaesarCipher, MultiplicativeCipher, TranspositionCipher, MyCipher



class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		# Setting the border, padding, etc for the application
		self.grid(padx = (10, 0), pady=30)

		# Calling the function to create widgets
		self.create_widgets()


	def create_widgets(self):
		# Local variable that will help 
		count_row = 0
		self.initialInstruction = Label(self, text = "Enter your Plain Text:", font=("Verdana", "12", "bold"))
		self.initialInstruction.grid(row = count_row, column = 0, columnspan = 10, sticky = W,pady=10)

		self.resultInstruction = Label(self, text = "Result:", font=("Verdana", "12", "bold"))
		self.resultInstruction.grid(row=count_row, column = 11, columnspan = 10, sticky = W, pady=10, padx=10)

		count_row += 1

		self.plainText = Text(self, width = 40, height=10, wrap= WORD)
		self.plainText.grid(row=count_row, column = 0, columnspan = 10, rowspan=10, sticky=W)
		
		# Setting the result for read-only
		self.result = Text(self, width= 40, height=10, wrap=WORD, state='disabled')
		"""
		Ps.: Before and after inserting, change the state, otherwise it won't update

		self.result.configure(state='normal')
		self.result.insert(0.0, 'Some Text')
		self.result.configure(state='disabled')

		"""
		self.result.grid(row=count_row, column=11, columnspan=10, sticky=W, padx=10)

		count_row += 10
		
		# Creating the variable for Radiobuttons
		# and setting the Radiobuttons initially unmarked
		self.cipher = IntVar()
		self.cipher.set(0)

		# Cipher Radiobutton Label
		count_row += 1
		self.cipherLabel = Label(self, text = "Choose the encrypt algorithm:", font=("Verdana", "12", "bold"))
		self.parameters_row = count_row
		self.cipherLabel.grid(row=count_row, column = 0, columnspan = 10, rowspan=3, sticky = W+S, pady=10)
		count_row += 3

		# Initializing and building Cipher Radiobutton
		Radiobutton(self, text = "Affine Cipher", variable = self.cipher, value=1,  font=("Verdana", "10"),
		command = self.update_gui).grid(row=count_row, column = 0, sticky=W)
		self.affine_row = count_row
		count_row += 1

		Radiobutton(self, text = "Caesar Cipher", variable = self.cipher, value=2, font=("Verdana", "10"),
		command = self.update_gui).grid(row=count_row, column = 0, sticky=W)
		count_row += 1

		Radiobutton(self, text = "Multiplicative Cipher", variable = self.cipher, value=3, font=("Verdana", "10"),
		command = self.update_gui).grid(row=count_row, column = 0, sticky=W)
		count_row += 1

		Radiobutton(self, text = "My Cipher", variable = self.cipher, value=4, font=("Verdana", "10"),
		command = self.update_gui).grid(row=count_row, column = 0, sticky=W)
		count_row += 1

		Radiobutton(self, text = "Transposition Cipher", variable = self.cipher, value=5, font=("Verdana", "10"),
		command = self.update_gui).grid(row=count_row, column = 0, sticky=W)
		count_row += 1

		""" Declarations that we may use in the future. """
		# Initializing the Run button
		self.runButton = Button(self, text="Run", command=self.run_algorithm)
		self.warning = Label(self, text="This key can't be used with this alphabet.\nPlease enter another key.", 
			font=("Verdana", "10", "italic"), fg="red", wraplength=0)

		# Initializing the rules
		# Order:
        # valid percent substitutions (from the Tk entry man page)
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
		vkcmd = (self.register(self.validateKey), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		vacmd = (self.register(self.validateAlphabet), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		# Initializing the variables
		self.defineParameters = Label(self, text = "Define the parameters:", font=("Verdana", "12", "bold"))
		self.keyLabel = Label(self, text="Enter your Key:            ", font=("Verdana", "10", "bold"))
		self.keyEntry = Entry(self, validate='key', validatecommand=vkcmd)
		self.alphabetLabel = Label(self, text="Which alphabet do you want to use?", font=("Verdana", "10", "bold"))
		self.alphabetEntry = Entry(self, validate='key', validatecommand=vacmd)
		self.alphabetButton = IntVar()
		self.customAlphabetLabel = Label(self, text="Enter your custom alphabet:", font=("Verdana", "10", "bold"))

		# Initializing the parameters
		self.key = 0
		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789,.!?;:()"

		# Initializing the RadioButtons for alphabet
		self.defaultAlphabet = Radiobutton(self, text = "Default alphabet", variable = self.alphabetButton,
			value=1, font=("Verdana", "10"),
		command = self.update_alphabet)
		self.customAlphabet = Radiobutton(self, text = "Custom alphabet", variable = self.alphabetButton, 
			value=2, font=("Verdana", "10"),
		command = self.update_alphabet)


	def validateAlphabet(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
		# Check if there's no repeated characters in the alphabet
		for letter in str(value_if_allowed):
			if str(value_if_allowed).count(letter) > 1:
				return False
		return True


	def validateKey(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
		# Check if there's only numbers in the key
		if len(str(value_if_allowed)) == 0:
			return True
		if text in '0123456789':
			try:
				int(value_if_allowed)
				return True
			except ValueError:
				return False
		return False


	def update_gui(self):
		# Clear the view for another input variable.
		self.alphabetButton.set(0)
		self.customAlphabetLabel.grid_forget()
		self.alphabetEntry.grid_forget()

		# Construct defineParameters
		self.defineParameters.grid(row=self.parameters_row, column = 11, columnspan = 10, sticky = W, pady=10, padx=10)
		
		# Construct keyLabel
		self.keyLabel.grid(row=self.affine_row, column = 11, columnspan=1,sticky=W, padx=10)

		# Construct keyEntry
		self.keyEntry.grid(row = self.affine_row, column = 12, sticky=W)
		
		# Construct alphabetLabel
		self.alphabetLabel.grid(row=self.affine_row+1, column = 11, columnspan=3, sticky=W, padx=10)

		# Construct the Radiobuttons
		self.defaultAlphabet.grid(row=self.affine_row+2, column = 11, sticky=W, padx=10)
		self.customAlphabet.grid(row=self.affine_row+2, column = 12, sticky=W)

		# Construct the Run button
		self.runButton.grid(row=self.affine_row+4, column = 11, sticky=W, padx=10)

		# Check if the cipher is the Transposition Cipher
		# Then, we don't need the alphabet input
		if self.cipher.get() == 5:
			self.alphabetLabel.grid_forget()
			self.defaultAlphabet.grid_forget()
			self.customAlphabet.grid_forget()


	def update_alphabet(self):
		case = self.alphabetButton.get()

		# Setting the default alphabet
		self.setDefaultAlphabet()

		# Delete other entry
		self.customAlphabetLabel.grid_forget()
		self.alphabetEntry.grid_forget()

		# Check if the user wants to select a Custom Alphabet
		if case == 2:
			self.customAlphabetLabel.grid(row=self.affine_row+3, column=11, columnspan=3, sticky=W, padx=10)
			self.alphabetEntry.grid(row=self.affine_row+3, column = 13, sticky=W)

	def run_algorithm(self):
		# Cleaning the warning messages		
		self.warning.grid_forget()
		self.result.configure(state='normal')
		self.result.delete(0.0, END)
		self.result.configure(state='disabled')

		# Getting the cipher
		cipher = self.cipher.get()

		# Getting the alphabet
		self.setDefaultAlphabet()
		if self.alphabetButton.get() == 2 and cipher != 5:
			self.alphabet = self.alphabetEntry.get()
			if len(self.alphabet) == 0:
				# Warning message
				self.warning["text"] = "Your custom alphabet cannot be empty.\nTip: you should consider enter a large alphabet."
				self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)
				return

		# Getting the key
		if len(self.keyEntry.get()) == 0:
			# Warning message
			self.warning["text"] = "Please enter a valid key (numbers only)."
			self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)
			return
		self.key = int(self.keyEntry.get())
		
		# Getting the message
		# Put end-1c for avoid getting '\n' at the end of the input.
		message = self.plainText.get("1.0", 'end-1c')
		if len(message) == 0:
			# Warning message
			self.warning["text"] = "I think you forgot to enter your message..."
			self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)
			return

		# Configuring the result
		self.result.configure(state='normal')
		
		# Encrypt according to the selected cipher
		if cipher == 1: # Affine Cipher
			valid = AffineCipher.validateKey(self.key, len(self.alphabet))
			if valid is True:
				# Continue the algorithm
				self.result.insert(0.0, AffineCipher.encryptMessage(message, self.key, self.alphabet))
			else:
				# Show a warning message
				self.warning["text"] = "This key can't be used with this alphabet.\nPlease enter another key."
				self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)
			
		elif cipher == 2: # Caesar Cipher
			self.result.insert(0.0, CaesarCipher.encryptMessage(message, self.key, self.alphabet))

		elif cipher == 3: # Multiplicative Cipher
			valid = MultiplicativeCipher.validateKey(self.key, len(self.alphabet))
			if valid is True:
				# Continue the algorithm
				self.result.insert(0.0, MultiplicativeCipher.encryptMessage(message, self.key, self.alphabet))
			else:
				# Show a warning message
				self.warning["text"] = "This key can't be used with this alphabet.\nPlease enter another key."
				self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)

		elif cipher == 4: # My Cipher
			valid = MyCipher.validateKey(self.key, len(self.alphabet))
			if valid is True:
				# Continue the algorithm
				self.result.insert(0.0, MyCipher.encryptMessage(message, self.key, self.alphabet))
			else:
				# Show a warning message
				self.warning["text"] = "This key can't be used with this alphabet.\nPlease enter another key."
				self.warning.grid(row=self.affine_row+6, column=11, sticky=W+W, padx=10, columnspan=2, rowspan=2)

		elif cipher == 5: # Transposition Cipher
			self.result.insert(0.0, TranspositionCipher.encryptMessage(message, self.key))

		# Setting result for read-only again
		self.result.configure(state='disabled')


	def setDefaultAlphabet(self):
		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789,.!?;:()"



def main():
	# Creating empty window with a Title
	root = Tk()
	root.title("Hide your messages!")
	
	# Getting the screen infos
	width = root.winfo_screenwidth()
	#height = root.winfo_screenheight()

	# I'm going to use this fixed height because it looks better in my screen
	height = 450 #Value for better render

	# Setting the geometry for the application
	root.geometry(str(int(width/2)) + "x" + str(int(height)))

	# Initializing the application
	app = Application(root)
	root.mainloop()

if __name__ == '__main__':
	main()