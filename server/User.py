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

    def setEmailAddress():
        return
        #verify in format xxx@xxx.xxx

    def setAddress():
        return
        #create another address class with street number, street name, suburb, state, post code
        #street number: numbers only < 1000
        #street name: only letters, capitalised first letter of each word
        #suburb: only letters, capitalised first letter of each word
        #state: choose from Australian States only
        #Post code: numbers only, 4 digits long



user = User()
#user.setFirstName("mai1")
#user.setFirstName("ma i")
#user.setFirstName("mai")
#user.setFirstName("Mai")
user.setPhoneNumber('123456')
user.setPhoneNumber('a42356')