# Python Package to Toggle Characters Case in a String by JKL404
 
class Toggle:
    def __new__(self,string="error: nO StRiNg FoUnD fOr ToGgLe", choice="a"):
        #Initializing String and Choice
        self.choice=choice
        self.string = string
        self.string1 = ''
        if self.choice=='a':
            for i in self.string:
                if(ord(i) >= 65 and ord(i) <= 90): 
                    self.string1 = self.string1 + chr((ord(i) + 32)) 
                elif(ord(i) >= 97 and ord(i) <= 122):
                    self.string1 = self.string1 + chr((ord(i) - 32))
                else:
                    self.string1 = self.string1 + i
        return self.string1