import re
from Address import Address
class User:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.phoneNumber = None
        self.emailAddress = None
        self.address = None
    
    def setFirstName(self, firstName):
        #Ensure Capital first letter, only letters, no spaces
        if any(char.isdigit() for char in firstName):
            print("Name contains Digits, Please enter again")
        elif any(char == ' ' for char in firstName):
            print("Name contains Space! Please enter again")
        elif (firstName[0].islower()):
            print("Captilise first letter!!! Try Again!!")
        else:
            self.firstName = firstName
            print("First Name set to " + self.firstName)

    def setLastName(self, lastName):
        #Ensure Capital first letter, only letters, no spaces
        if any(char.isdigit() for char in lastName):
            print("Name contains Digits, Please enter again")
        elif any(char == ' ' for char in lastName):
            print("Name contains Space! Please enter again")
        elif (lastName[0].islower()):
            print("Captilise first letter!!! Try Again!!")
        else:
            self.lastName = lastName
            print("Last Name set to " + self.lastName)

    def setPhoneNumber(self, phoneNumber):
        if any(char.isalpha() for char in phoneNumber):
            print('Phone number contains letters, Please enter again')
        elif phoneNumber[0] != 0:
            print('Phone number must start with 0, Please enter again')
        elif len(str(phoneNumber)) > 10:
            print('Phone number contains 10 digits only, please enter again')
        elif len(str(phoneNumber)) < 10:
            print('Phone number contains 10 digits only, please enter again')
        else:
            self.phoneNumber = phoneNumber
            print("Phone Number set to " + self.phoneNumber)

        

        #Ensure numbers only, 10 digits, starts with 0

    def setEmailAddress(self, emailAddress):
        if type(emailAddress) is str:
            if re.match(r'[^@]+@[^@]+\.[^@]+',emailAddress):
                print('address is valid')
                self.emailAddress = emailAddress
            else:    
                print('address is not valid')
        else:
            print('it is not a string')

    def setAddress(self, address):
        if type(address) is Address:
            self.address = address
        else:
            print('Address is not the same')


user = User()
#user.setFirstName("mai1")
#user.setFirstName("ma i")
#user.setFirstName("mai")
#user.setFirstName("Mai")
#user.setPhoneNumber('123456')
#user.setPhoneNumber('a42356')

a1 = Address()

#user.setEmailAddress(1) 
user.setAddress(a1)
