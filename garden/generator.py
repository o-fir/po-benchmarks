#GENERATOR PRINCIPLE
#Problems gradually gain the amount of variables
#There's an equal amount of trees and holes
#There are more trees than gardeners

import random
import subprocess


num_of_problems=100

check = True

gardener_count = 2
tree_hole_count = 1
well_count = 1

for x in range(num_of_problems):
    subprocess.run(["python", "instance_generator.py", str(gardener_count), str(tree_hole_count), str(x), str(tree_hole_count), str(well_count)])

    minTreeNum = round((x+6)/4)
    tree_hole_count = random.randint(minTreeNum, x+2) 
    gardener_count = random.randint(2, (x+4)-tree_hole_count) 
    well_count = random.randint(2, x+6 - tree_hole_count - gardener_count)
    tree_hole_count = round(tree_hole_count/2)+1#previous calculations take into account holes and trees together

    print(str(tree_hole_count*2)+"+"+str(gardener_count)+"+"+str(well_count)+"="+str(tree_hole_count*2+gardener_count+well_count))
