#!/usr/bin/env python
# coding: utf-8

# Python Package to Toggle Characters Case in a String by JKL404
import time,random
class ChoiceError(Exception):
    pass
class SpeedError(Exception):
    pass
class Toggle:
    def __new__(self,string=None, choice=0,speed=0):
        #Exception Handling
        try:
            #Initializing String and Choice
            self.choice=int(choice)
            self.string = string
            self.string1 = ''
            try:
                if choice < 0 or choice > 5:
                    raise ChoiceError()
            except:
                print("Toggle Error: Please check 'Choice' field, It Must be Integer between 0-5")
            #Checking Choice Conditions
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
                            if(ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90): 
                                self.string1 = self.string1 + chr((ord(self.string[i]) + 32))
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
            elif choice==5:
                self.string1=self.string
            #Typing Slow with toggle string
            if speed==0:
                return self.string1
            else:
                try:
                    if speed < 1 or speed > 1000:
                        raise SpeedError()
                    for l in self.string1:
                        print(l, flush=True,end='')
                        time.sleep(random.random()*10.0/speed)
                    print('')
                    return ''
                except TypeError:
                    print("Toggle Error: Please check 'Speed' field, It must be Integer between 1-1000")
        except TypeError:
            print("Toggle Error: nO StRiNg FoUnD fOr ToGgLe")
        except ChoiceError:
            print("Toggle Error: Please check 'Choice' field, It Must be between 0-5")
        except SpeedError:
            print("Toggle Error: Please check 'Speed' field, It Must be between 1-1000")
        except:
            print("Toggle Error: Please check the Syntax")
            
#print(Toggle("JokER beautiful",4,50))
