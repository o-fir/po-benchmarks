import random
import subprocess


num_of_problems=100

check = True

barista_count = 1
customer_count = 1
barista_distribution = 0

# every subsequent problem alternates between 1 more barista and 1-3 more customers

for x in range(num_of_problems):
    subprocess.run(["python", "instance_generator.py", str(barista_count), str(customer_count), str(x), str(barista_distribution)])
    if check:
        barista_count += 1
    else:
        customer_count += random.randint(1, 3)
    barista_distribution = random.randint(0,3)
    check = not(check)
