import random
import sys


def main(argv):
    if(len(argv) != 4):
        print("INPUT ERROR")
        print("args: num_oven, num_brick, num_temp")
        sys.exit()
    
    #====================================
    #VARIABLES
    num_oven = int(argv[0])
    num_brick = int(argv[1])
    problem_num = int(argv[2])
    num_temp = int(argv[3])

    #=====================================
    filename="pfile"+str(problem_num)

    f = open(filename+".hddl", "w")

    f.write("; num_oven: "+str(num_oven)+"\n")
    f.write("; num_brick: "+str(num_brick)+"\n")
    f.write("; num_temp: "+str(num_temp)+"\n\n")
    
    f.write("(define\n")
    f.write("   (problem "+filename+")\n")
    f.write("   (:domain postman)\n")
    f.write("   (:objects\n")

    ovens = ""
    for x in range(num_oven-1):
        ovens = ovens +"oven_"+str(x)+", "
    ovens = ovens +"oven_"+str(num_oven-1) +" - oven"
    f.write("      "+ovens+"\n")

    brick = ""
    for x in range(num_brick-1):
        brick = brick +"brick_"+str(x)+", "
    brick = brick +"brick_"+str(num_brick-1) +" - brick"
    f.write("      "+brick+"\n")

    temps = ""
    for x in range(num_temp-1):
        temps = temps +"temp_"+str(x)+", "
    temps = temps +"temp_"+str(num_temp-1)+" - temperature"
    f.write("      "+temps+"\n")

    f.write("   )\n\n")
    f.write("   (:htn\n")
    f.write("      :parameters ()\n")
    f.write("      :subtasks (and\n")

    tasks = ""
    #dry all bricks
    for x in range(num_brick):
        f.write("         (task"+str(x)+" (dry brick_"+str(x)+"))\n")
    f.write("      )\n")
    f.write("   )\n\n")
    f.write("   (:init\n")

    #set all ovens to cold
    for x in range(num_oven):
        f.write("      (oven-cold oven_"+str(x)+")\n")
    #randomly distribute bricks to temperature settings
    for x in range(num_brick):
        rand_temp = random.randint(0, num_temp-1)
        f.write("      (brick-spec brick_"+str(x)+" temp_"+str(rand_temp)+")\n")


    f.write("   )\n")
    f.write(")")

    f.close()

    #open and read the file after the appending:
    f = open(filename+".hddl", "r")
    print(f.read())

if __name__ == "__main__":
   main(sys.argv[1:])
