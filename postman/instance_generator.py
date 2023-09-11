import random
import sys


def main(argv):
    if(len(argv) != 4):
        print("INPUT ERROR")
        print("args: num_postmen, num_mail, num_location")
        sys.exit()
    
    #====================================
    #VARIABLES
    num_postmen = int(argv[0])
    num_mail = int(argv[1])
    problem_num = int(argv[2])
    num_loc = int(argv[3])

    #=====================================
    filename="pfile"+str(problem_num)

    f = open(filename+".hddl", "w")

    f.write("; num_postmen: "+str(num_postmen)+"\n")
    f.write("; num_mail: "+str(num_mail)+"\n")
    f.write("; num_loc: "+str(num_loc)+"\n\n")
    
    f.write("(define\n")
    f.write("   (problem "+filename+")\n")
    f.write("   (:domain postman)\n")
    f.write("   (:objects\n")

    postmen = ""
    for x in range(num_postmen-1):
        postmen = postmen +"postman_"+str(x)+", "
    postmen = postmen +"postman_"+str(num_postmen-1) +" - postman"
    f.write("      "+postmen+"\n")

    mail = ""
    for x in range(num_mail-1):
        mail = mail +"mail_"+str(x)+", "
    mail = mail +"mail_"+str(num_mail-1) +" - mail"
    f.write("      "+mail+"\n")

    loc = ""
    for x in range(num_loc-1):
        loc = loc +"loc_"+str(x)+", "
    loc = loc +"loc_"+str(num_loc-1)+" - location"
    f.write("      "+loc+"\n")

    f.write("   )\n\n")
    f.write("   (:htn\n")
    f.write("      :parameters ()\n")
    f.write("      :subtasks (and\n")

    tasks = ""
    #deliver mail to random location
    for x in range(num_mail):
        rand_loc = random.randint(0, num_loc-1)
        f.write("         (task"+str(x)+" (deliver mail_"+str(x)+" loc_"+str(rand_loc)+"))\n")
    f.write("      )\n")
    f.write("   )\n\n")
    f.write("   (:init\n")

    #randomly distribute postmen
    for x in range(num_postmen):
        rand_loc = random.randint(0, num_loc-1)
        f.write("      (at postman_"+str(x)+" loc_"+str(rand_loc)+")\n")
    #randomly distribute mail
    for x in range(num_mail):
        rand_loc = random.randint(0, num_loc-1)
        f.write("      (at mail_"+str(x)+" loc_"+str(rand_loc)+")\n")


    f.write("   )\n")
    f.write(")")

    f.close()

    #open and read the file after the appending:
    f = open(filename+".hddl", "r")
    print(f.read())

if __name__ == "__main__":
   main(sys.argv[1:])
