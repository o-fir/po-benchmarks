import random
import sys


def main(argv):
    if(len(argv) == 4):
        print("INPUT ERROR")
        print("args: num_gardener, num_tree, num_hole, num_well")
        sys.exit()
    
    #====================================
    #VARIABLES
    num_gardener = int(argv[0])
    num_tree = int(argv[1])
    problem_num = int(argv[2])
    num_hole = int(argv[3])
    num_well = int(argv[4])

    #=====================================
    filename="pfile"+str(problem_num)

    f = open(filename+".hddl", "w")

    f.write("; num_gardener: "+str(num_gardener)+"\n")
    f.write("; num_tree: "+str(num_tree)+"\n")
    f.write("; num_hole: "+str(num_hole)+"\n")
    f.write("; num_well: "+str(num_well)+"\n\n")
    
    f.write("(define\n")
    f.write("   (problem "+filename+")\n")
    f.write("   (:domain garden)\n")
    f.write("   (:objects\n")

    gardener = ""
    for x in range(num_gardener-1):
        gardener = gardener +"gardener_"+str(x)+", "
    gardener = gardener +"gardener_"+str(num_gardener-1) +" - gardener"
    f.write("      "+gardener+"\n")

    tree = ""
    for x in range(num_tree-1):
        tree = tree +"tree_"+str(x)+", "
    tree = tree +"tree_"+str(num_tree-1) +" - tree"
    f.write("      "+tree+"\n")

    hole = ""
    for x in range(num_hole-1):
        hole = hole +"hole_"+str(x)+", "
    hole = hole +"hole_"+str(num_hole-1) +" - hole"
    f.write("      "+hole+"\n")

    well = ""
    for x in range(num_well-1):
        well = well +"well_"+str(x)+", "
    well = well +"well_"+str(num_well-1) +" - well"
    f.write("      "+well+"\n")



    f.write("   )\n\n")
    f.write("   (:htn\n")
    f.write("      :parameters ()\n")
    f.write("      :subtasks (and\n")

    tasks = ""
    #plant trees
    for x in range(num_tree):
        f.write("         (task"+str(x)+" (plant tree_"+str(x)+"))\n")
    f.write("      )\n")
    f.write("   )\n\n")
    f.write("   (:init\n")

    #randomly distribute gardeners
    for x in range(num_gardener):
        rand_hole = random.randint(0, num_hole-1)
        f.write("      (at gardener_"+str(x)+" hole_"+str(rand_hole)+")\n")
    #randomly fill watering cans
    for x in range(num_gardener):
        randBool = random.random() > 0.5
        if randBool:
            f.write("      (can-full gardener_"+str(x)+")\n")
        else:
            f.write("      (not(can-full gardener_"+str(x)+"))\n")


    f.write("   )\n")
    f.write(")")

    f.close()

    #open and read the file after the appending:
    f = open(filename+".hddl", "r")
    print(f.read())

if __name__ == "__main__":
   main(sys.argv[1:])
