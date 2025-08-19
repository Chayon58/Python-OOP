class Vaccine:
    def __init__(self, name, made_in,interval):
        self.name = name
        self.made_in = made_in
        self.interval =  interval
#=================================================================
        
class person:
    def __init__(self, pname, age, ptype = "General Citizen"):
        self.pname = pname
        self.age = age
        self.ptype = ptype
        self.vac = ""
        self.firstdose = False
        self.sectdose = False

    def PushVaccine(self, vacN, dose = "1st dose"):
        if dose== "1st dose":
            if self.age >= 25 or self.ptype == "Student":
                self.vac = vacN   #storing object of vaccine/memory location
                self.firstdose = True
                print("First dose done for", self.pname)
            else:
                print("Sorry" , self.pname, "minimum age for taking vaccine is 25 years now.")
        else:
            if self.vac.name != vacN.name:
             print("Sorry" , self.pname, "you cannot take 2 different vaccine")
            else:
                self.sectdose = True
                print("Second dose done for", self.pname)
    
    def showDetail(self):
        print ("Name : ", self.pname,"\nAge : ", self.age,"\nType : ", self.ptype)
        print("Vaccine Name : ", self.vac.name)
        if self.firstdose == True:
            print("Dose Given : First Dose")
            print("Dose Given : Second Dose")
        elif self.sectdose ==True:
            print("Dose Given : First Dose")
            print(" 2nd dose: Please come after", self.vac.interval, "days")
        

#===================================================================