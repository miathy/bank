class Address:
    def __init__(self):
         #street number: numbers only < 1000
        #street name: only letters, capitalised first letter of each word
        #suburb: only letters, capitalised first letter of each word
        #state: choose from Australian States only
        #Post code: numbers only, 4 digits long
        self.streetNumber = streetNumber
        self.streetName = streetName
        self.suburb = suburb
        self.state = state   
        self.postCode = postCode
    
    def setStreetNumber(self, streetNumber):
        if any(char.isalpha() for char in streetNumber):
            print('Street number contains letters, Please enter again')
        elif len(str(streetName)) > 1000:
            print('Street number must be less than 1000 digits')
        else:
            self.streetNumber = streetNumber
            print('Street number is set to' + self.streetNumber)
    
    def setStreetName(self, streetName):
        if any(char.isdigit() for char in streetName):
            print("Name contains Digits, Please enter again")
        elif any(char[0].islower() for char in streetName.split()):
            print('Please capitalize 1st letter of each word')
        else:
            self.streetName = streetName
            print("Street Name set to " + self.streetName)
    
    def setSuburb(self, suburb):
        if any(char.isdigit() for char in suburb):
            print("Name contains Digits, Please enter again")
        elif any(char[0].islower() for char in suburb):
            print('Please capitalize 1st letter of each word')
        else:
            self.suburb = suburb
            print("Street Name set to " + self.suburb)
    
    def setState(self, state):
        states = ['VIC', 'QLD', 'NT', 'TAS', 'NSW', 'WA','SA','ACT']
        if state not in states:
            print('please enter Australian State only')
        else:
            self.state = state
    
    def setpostCode(self, postCode):
        if any(char.isalpha() for char in postCode):
            print('Post code contains letters, Please enter again')
        elif len(str(postCode)) !=4:
            print('Street number must have 4 digits, please enter again')
        else:
            self.postCode = postCode
            print('post code is set to' + self.postCode)
            





           