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

    def setLastName():
        return
        #Ensure Capital first letter, only letters, no spaces

    def setPhoneNumber():
        return
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
user.setFirstName("mai1")
user.setFirstName("ma i")
user.setFirstName("mai")
user.setFirstName("Mai")