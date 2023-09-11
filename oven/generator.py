#GENERATOR PRINCIPLE
#Problems gradually gain the amount of variables
#Numbers are distributed as follows: temps<ovens<bricks
#this distribution will ensure that there is always a possibility for
#bricks to share an oven
#
#Bricks form at least 1/3 of all variables
#There must be at least 2 temp modes
#There must be at least 4 bricks

import random
import subprocess


num_of_problems=100

check = True

num_ovens = 2
num_temps = 2
num_bricks = 4

for x in range(num_of_problems):
    subprocess.run(["python", "instance_generator.py", str(num_ovens), str(num_bricks), str(x), str(num_temps)])

    minOvenNum = round((x/3))+2
    num_ovens = random.randint(minOvenNum, x+2) 
    num_bricks = random.randint(2, x+6-num_ovens) 
    num_temps = random.randint(2, x+8 - num_ovens - num_bricks)

    print(str(num_ovens)+"+"+str(num_bricks)+"+"+str(num_temps)+"="+str(num_ovens+num_bricks+num_temps)+" : "+str(x))
