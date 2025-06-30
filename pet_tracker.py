class pet:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=False
    
    def display_info(self):
        if self.adopted==True:
            adoption_status="is adopted"
        else:
            adoption_status="Not adopted"
        print(f"Pet's name is : {self.name}", 
              f"Pet's age is : {self.age}" ,
              f"Pet's specie is: {self.species}",
              f"Pet's adoption status is :{adoption_status}"
        )

    def mark_adopted(self):
        self.adopted==True
        print(f"{self.adopted} is now adopted")    

    def birthday(self):
        self.age+=1
        print(f"Happy birthday{self.name}, your age is: {self.age}")


    

