favorite_animals=['dog','cat','monkey','rabbit']
print(favorite_animals)
print(f'the second element in the list is {favorite_animals[1]}')
favorite_animals.remove('monkey')
print(favorite_animals)

favorite_animals.append('chicken')
print(favorite_animals)
for animal in favorite_animals:
    print (f'i love {animal}')

numbers=[1,2,3,4,5]
number_sum=0
for number in numbers :
    number_sum=(number_sum+number)

print(number_sum)

