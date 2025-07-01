#part1
class pet:
    def __init__(self,name,species,age,adopted=False):
        self.name=name
        self.species=species
        self.age=age
        self.adopted=adopted
    
    def display_info(self):
        if self.adopted==False:
            adoption_status="is not adopted"
        else:
            adoption_status="is adopted"
        return f"Pets name is : "+ self.name +" , Pets specie is: "+self.species +" , Pets age is :"+str(self.age) +" ,Pet : "+ adoption_status

    def mark_adopted(self):
        self.adopted=True
        return f"The pet {self.name} is now adopted"   

    def birthday(self):
        self.age+=1
        return f" Happy birthday {self.name}! \n your age now is : {self.age}"


pet1=pet("Max", "Dog", 1)
pet2=pet("Molly","Cat", 2)
pet3=pet("Flufy","Cat", 3)
pet4=pet("Barney","Dog", 2)

print(pet1.display_info())
print(pet1.birthday())
print(pet1.mark_adopted())
print(pet1.display_info())

#part2
pets_list = [pet1, pet2, pet3, pet4]

def find_non_adopted(list):
    non_adopted_list = []
    for pet in list:
        if pet.adopted == False:
            non_adopted_list.append(pet.display_info())
    return f"The List of non adopted pets is {non_adopted_list}"

print(find_non_adopted(pets_list))




    

