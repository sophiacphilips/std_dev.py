# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 11/2/22
# This code takes a group of people's ages and finds the standard deviation among them.

class Person():
    """class of persons, containing their name and age"""
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age #used to get ages of people in group

#std dev formula  SUM(((x-u)^2)/N^1/2
#x=individual value
#u=average age
#N=total number of population
def std_dev(person_list):
    total=0 #this will be used to find the sum of all ages
    for person in person_list:
        total+= person.get_age() #sum formula
    average_age = total/(len(person_list))

#first_half_sum denotes the sum of first half of SD equation: ((x-u)^2)
    first_half_sum=0
    for person in person_list:
        first_half_sum += (person.get_age() - average_age) ** 2

    return (first_half_sum/(len(person_list)))**0.5 #this line puts the entire std dev equation together

#test
#p1= Person("Kyoungmin", 73)
#p2= Person("Mercedes", 24)
#p3= Person("Beatrice", 48)
#person_list=[p1,p2,p3]
#answer=std_dev(person_list)
#print(answer)

