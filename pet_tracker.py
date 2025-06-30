class pet:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=False
    
    def display_info(self):
        if self.adopted==False:
            adoption_status="is not adopted"
        else:
            adoption_status="is adopted"
        print(f"Pet's name is : {self.name} \n", 
              f"Pet's age is : {self.age} \n" ,
              f"Pet's specie is: {self.species} \n",
              f"Pet's adoption status is : {adoption_status}"
        )

    def mark_adopted(self):
        self.adopted=True
        print(f"{self.name} is now adopted")    

    def birthday(self):
        self.age+=1
        print(f"Happy birthday {self.name}, your age is: {self.age}")

pet1=pet("Max", "Dog", 1)
pet2=pet("Molly","Cat", 2)
pet3=pet("Flufy","Cat", 3)
pet4=pet("Barney","Dog", 2)


pet1.display_info()
#pet2.display_info()
#pet3.display_info()
#pet4.display_info()


pet1.birthday()
pet1.mark_adopted()
pet1.display_info()


    

