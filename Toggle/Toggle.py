#!/usr/bin/env python
# coding: utf-8

# In[58]:


# Python Package to Toggle Characters Case in a String by JKL404
 
class Toggle:
    def __new__(self,string="error: nO StRiNg FoUnD fOr ToGgLe", choice=0):
        #Initializing String and Choice
        self.choice=choice
        self.string = string
        self.string1 = ''
        if self.choice==0:
            for i in self.string:
                if(ord(i) >= 65 and ord(i) <= 90): 
                    self.string1 = self.string1 + chr((ord(i) + 32)) 
                elif(ord(i) >= 97 and ord(i) <= 122):
                    self.string1 = self.string1 + chr((ord(i) - 32))
                else:
                    self.string1 = self.string1 + i
        elif self.choice==1 or self.choice==2:
            if self.choice==1:
                flag=0
            else:
                flag=1
            for i in range(len(self.string)):
                if self.string[i]==" ":
                    if flag==0:
                        flag=1
                    else:
                        flag=0
                if i % 2 == flag:
                    if(ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90): 
                        self.string1 = self.string1 + chr((ord(self.string[i]) + 32)) 
                    else:
                        self.string1 = self.string1 + self.string[i]
                else:
                    if(ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122):
                        self.string1 = self.string1 + chr((ord(self.string[i]) - 32))
                    else:
                        self.string1 = self.string1 + self.string[i]
        elif self.choice==3 or self.choice==4:
            if self.choice==3:
                flag=0
            else:
                flag=1
            for i in range(len(self.string)):
                if flag==0:
                    if i ==0:
                        if(ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90): 
                            self.string1 = self.string1 + chr((ord(self.string[i]) + 32))
                        else:
                            self.string1 = self.string1 + self.string[i]
                    elif self.string[i-1]==" ":
                        if(ord(self.string[i+1]) >= 65 and ord(self.string[i+1]) <= 90): 
                            self.string1 = self.string1 + chr((ord(self.string[i+1]) + 32))
                        else:
                            self.string1 = self.string1 + self.string[i]
                    elif(ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122):
                        self.string1 = self.string1 + chr((ord(self.string[i]) - 32))
                    else:
                        self.string1 = self.string1 + self.string[i]
                else:
                    if i ==0:
                        if(ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122):
                            self.string1 = self.string1 + chr((ord(self.string[i]) - 32))
                        else:
                            self.string1 = self.string1 + self.string[i]
                    elif self.string[i-1]==" ":
                        if(ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122):
                            self.string1 = self.string1 + chr((ord(self.string[i]) - 32))
                        else:
                            self.string1 = self.string1 + self.string[i]
                    elif ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90: 
                            self.string1 = self.string1 + chr((ord(self.string[i]) + 32))
                    else:
                        self.string1 = self.string1 + self.string[i]
        return self.string1
#print(Toggle("JokER beautiful",4))

