name = "Tony Stark" #string is also stored in indexes in python
print(name[5])
print(len(name)) #len ---> prints the total no.of characters in name 

names = "Tony Stark,Steve Rogers,Bruce Banner,Peter Parker,Stephan Strange,Logan,Wade Wilson"
print(names[0:30]) #this will give names between 0th index and 30th index

fruits = "mango, orange, papaya, kiwi, watermelon"
for i in fruits:
    print(i) #for loop in strings

nm = "Harry"
print(nm[-4:-2])

name = "jake fraser mcgurk"
print(name.upper()) #converts string into UPPERCASE

name = "SacHin RamEsh TenDulKar"
print(name.lower()) #converts string into LOWERCASE

a = "!!!Surya!!!"
print(a.rstrip("!")) #this method will strip all the ! characters in the string from the end but not from start

b = "Jack"
print(b.replace("Jack","Reacher")) #this will replace the given string with a new value

c = "India, Australia, England, South Africa, New Zealand"
print(c.split()) #this will convert the string into a list

d = "introduction to python programming"
print(d.capitalize()) #this will convert the first letter of the string in capital form

e = "ababaabbcbbaaabbbccc"
print(e.count("a")) #this will count the occurrences of a in the string

f = "roses are red, skies are blue!"
print(f.endswith("!")) #returns true if the string is ending with the same character given 

g = """If I had a penny that fell from above
For every time I fell in love
I’ll be rollin in my money
Every day would be sunny
And I’ll be looking forward for my next break up"""
print(g.find("in")) #returns the index number of the character encountered firstly in string

