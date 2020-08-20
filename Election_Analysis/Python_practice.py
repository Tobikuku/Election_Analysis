import sys
print(sys.version)
print(sys.executable)
(5+3)*3
counties = ["Arapahoe", "Denver", "Jefferson"]
counties
print("Hello World")
counties.extend(['suffolk'])
counties[0]
len(counties)
counties

counties
new_list = tuple(counties)
new_list
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Jefferson"] = 432438

score = int(input("What is your Test score?"))
if score >= 90: 
    print('Your grade is an A')
elif score >=80:
     print('Your grade is a B')
elif  score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
    print('Your grade is an F')
score = 99

if "suffolk" in counties:
    print("suffolk is in the list of counties")
else:
    print("suffolk is not in the list of counties")
   