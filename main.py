def tokens(sentence):
  word = sentence.lower()
  word2 = word.split() #split sentnces to words
  length = len(word2)
  return word2, length

sentence = 'this IS a life'
tokens2, lenght = tokens(sentence)
print('tokens', tokens2)
print('length', lenght)

chractr_name = 'john is bad'
Chracter_age = '80'
print('the boy', chractr_name + 'like that he is', Chracter_age + 'years in this world')
chractr_name = 'paul likes him'
print('the boy', chractr_name + 'is now ' + 'in love with john')
chractr_name = 'paul likes him'
Chracter_age = 50
is_female = False
print('the\nboy', chractr_name + 'is now ' + 'in love with john')
pie = 'joHnny best'
print(pie.upper().isupper())
print(len(pie))
print(pie[5])
print(pie.index('t'))
print(pie.replace('joHnny', 'beasty'))
from math import *
num = -6
print(str(num))
print(abs(num))
print(pow(num, 5))
num = 34.56
print(floor(num))
print(ceil(num))
print(sqrt(num))
location  = input('enter name of city: ')
food = input('enter name of favorite food: ')
friend = input('enter name of friend: ')
print('musa lived in ' + location + ' for 300 eons')
print('he loves when i cook ' + food + ' for him')
print ('he is madly in love with ' + friend)

name = input('first name and last name')
age = input('enter your age')
hobbies = input('enter your hobbies')
destination = input('enter your favorite destination')
print('Your are' + name + '.' + 'You are' + age + 'years' + 'and you love to' + hobbies + '.are you willing to travel to' + destination)

num1 = input('enter a number')
num2 = input('enter another number')
ans = float(num1) + float(num2)
print(ans)

items