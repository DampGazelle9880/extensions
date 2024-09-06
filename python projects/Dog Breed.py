class dog:
    #class variable
    species = "Dog"
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
dog1 = dog("Dash", "buddy")   
dog2 = dog("Lab", "bud")
print(f"{dog1.name} is a{dog1.breed}")
print(f"{dog2.name} is a{dog2.breed}")


        