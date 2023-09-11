#GENERATOR PRINCIPLE
#Problems gradually gain the amount of variables
#First problem has 6 variables. Thus, last problem has 105 variables)
#The way these variables are allocated is random
#Meaning, p1 has 10 variables distributed as 3 postmen, 4 mail, 3 location
#while p2 has 11 variables distributed as 2 postmen, 6 mails, 3 locations
#Hard criteria for random generation:
#1. There must be at least 2 postmen and 2 locations
#2. Mail must be at least a quarter of variables

import random
import subprocess


num_of_problems=100

check = True

postman_count = 2
mail_count = 2
loc_count = 2

for x in range(num_of_problems):
    subprocess.run(["python", "instance_generator.py", str(postman_count), str(mail_count), str(x), str(loc_count)])

    minMailNum = round((x+6)/4)
    mail_count = random.randint(minMailNum, x+2) #reserve 4 variables. 2 for postmen, 2 for locations
    postman_count = random.randint(2, (x+4)-mail_count) #reserve 2 variables for locations
    loc_count = random.randint(2, x+6 - mail_count - postman_count)

    print(str(mail_count)+"+"+str(postman_count)+"+"+str(loc_count)+"="+str(mail_count+postman_count+loc_count))
