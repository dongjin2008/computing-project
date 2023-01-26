class unit_convert:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.ui = ""
    
    def get_ui(self):
        self.ui = int(input("Enter the number: "))

    def to_cm(self):
        if self.input == "m":
            return self.ui * 100

        elif self.input == "km":
            return self.ui * 100000

    def to_m(self):
        if self.input == "cm":
            return self.ui / 100

        elif self.input == "km":
            return self.ui * 1000

    def to_km(self):
        if self.input == "cm":
            return self.ui / 100000
        elif self.input == "m":
            return self.ui / 1000

    def to_g(self):
        if self.input == "kg":
            return self.ui * 1000
        elif self.input == "t":
            return self.ui * 1000000

    def to_kg(self):
        if self.input == "g":
            return self.ui / 1000
        elif self.input == "t":
            return self.ui * 1000
    
    def to_t(self):
        if self.input == "g":
            return self.ui / 100000
        elif self.input == "kg":
            return self.ui / 1000

    def to_ml(self):
        if self.input == "l":
            return self.ui * 1000
        elif self.input == "kl":
            return self.ui * 1000000

    def to_l(self):
        if self.input == "ml":
            return self.ui / 1000
        elif self.input == "kl":
            return self.ui * 1000
    
    def to_kl(self):
        if self.input == "ml":
            return self.ui / 100000
        elif self.input == "l":
            return self.ui / 1000

    def main(self):
        self.get_ui()
        if self.output == "cm":
            return str(self.to_cm()) + "cm"
        
        elif self.output == "m":
            return str(self.to_m()) + "m"

        elif self.output == "km":
            return str(self.to_km()) + "km"

        elif self.output == "g":
            return str(self.to_g()) + "g"

        elif self.output == "kg":
            return str(self.to_kg()) + "kg"

        elif self.output == "t":
            return str(self.to_t()) + "t"

        elif self.output == "ml":
            return str(self.to_ml()) + "ml"

        elif self.output == "l":
            return str(self.to_l()) + "l"

        elif self.output == "kl":
            return str(self.to_kl()) + "kl"

def UnitConvert(Input, Output):
    return unit_convert(input=Input, output=Output).main()