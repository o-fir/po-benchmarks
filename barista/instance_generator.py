import random
import sys



def main(argv):
    if(len(argv) != 4):
        print("INPUT ERROR")
        print("args: num_baristas, num_customers, problem_num, barista_distribution")
        sys.exit()
    
    #====================================
    #VARIABLES
    num_baristas = int(argv[0])
    num_customers = int(argv[1])
    problem_num = int(argv[2])

    #barista distribution
    #0 - all at counter
    #1 - all at back
    #2 - random
    #3 - even distribution
    barista_distribution = int(argv[3])
    #=====================================
    filename="pfile"+str(problem_num)

    f = open(filename+".hddl", "w")

    f.write("; num_baristas: "+str(num_baristas)+"\n")
    f.write("; num_customers: "+str(num_customers)+"\n")
    f.write("; barista_distribution: "+str(barista_distribution)+"\n\n")
    
    f.write("(define\n")
    f.write("   (problem "+filename+")\n")
    f.write("   (:domain barista)\n")
    f.write("   (:objects\n")

    baristas = ""
    for x in range(num_baristas-1):
        baristas = baristas +"barista_"+str(x)+", "
    baristas = baristas +"barista_"+str(num_baristas-1) +" - barista"
    f.write("      "+baristas+"\n")

    customers = ""
    for x in range(num_customers-1):
        customers = customers +"customer_"+str(x)+", "
    customers = customers +"customer_"+str(num_customers-1) +" - customer"
    f.write("      "+customers+"\n")

    f.write("   )\n\n")
    f.write("   (:htn\n")
    f.write("      :parameters ()\n")
    f.write("      :subtasks (and\n")

    tasks = ""
    for x in range(num_customers):
        f.write("         (task"+str(x)+" (serve customer_"+str(x)+"))\n")
    f.write("      )\n")
    f.write("   )\n\n")
    f.write("   (:init\n")

    #barista distribution
    #CASE 0: all at counter
    if barista_distribution == 0:
        for x in range(num_baristas):
            f.write("      (barista-at-counter barista_"+str(x)+")\n")
    #CASE 1: all in back
    if barista_distribution == 1:
        for x in range(num_baristas):
            f.write("      (barista-in-the-back barista_"+str(x)+")\n")
    #CASE 2: random
    if barista_distribution == 2:
        for x in range(num_baristas):
            randBool = random.random() > 0.5
            if randBool:
                f.write("      (barista-in-the-back barista_"+str(x)+")\n")
            else:
                f.write("      (barista-at-counter barista_"+str(x)+")\n")
    #CASE 3: even distribution
    if barista_distribution == 3:
        switch = True
        for x in range(num_baristas):
            if switch:
                f.write("      (barista-in-the-back barista_"+str(x)+")\n")
            else:
                f.write("      (barista-at-counter barista_"+str(x)+")\n")
            switch = not(switch)
    f.write("   )\n")
    f.write(")")



    f.close()

    #open and read the file after the appending:
    f = open(filename+".hddl", "r")
    print(f.read())

if __name__ == "__main__":
   main(sys.argv[1:])
