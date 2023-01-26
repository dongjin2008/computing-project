class num_convert:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.ui = ""
    
    def get_ui(self):
        self.ui = input("Enter the {} number: ".format(self.input))

    def to_bin(self):
        if self.input == "dec":
            return bin(self.ui)[2:]

        elif self.input == "oct":
            return bin(int(self.ui, 8))[2:]

        elif self.input == "hex":
            return bin(int(self.ui, 16))[2:]

        elif self.input == "bin":
            return "It's already binary"

    def to_dec(self):
        if self.input == "dec":
            return "It's already decimal"

        elif self.input == "oct":
            return int(self.ui, 8)

        elif self.input == "hex":
            return int(self.ui, 16)

        elif self.input == "bin":
            return int(self.ui, 2)

    def to_oct(self):
        if self.input == "dec":
            return oct(self.ui)[2:]

        elif self.input == "oct":
            return "It's already octal"

        elif self.input == "hex":
            return oct(int(self.ui, 16))[2:]

        elif self.input == "bin":
            return oct(int(self.ui, 2))[2:]

    def to_hex(self):
        if self.input == "dec":
            return hex(self.ui)[2:]

        elif self.input == "oct":
            return hex(int(self.ui, 8))[2:]

        elif self.input == "hex":
            return "It's already hexadecimal"

        elif self.input == "bin":
            return hex(int(self.ui, 2))[2:]
    
    def main(self):
        self.get_ui()
        if self.output == "dec":
            return self.to_dec()
        
        elif self.output == "bin":
            return self.to_bin()

        elif self.output == "oct":
            return self.to_oct()
    
        elif self.output == "hex":
            return self.to_hex()


def NumConvert(Input, Output):
    return num_convert(input=Input, output=Output).main()