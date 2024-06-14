students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
 
groups = (students + group_size - 1) // group_size
 
print("Number of groups formed:", groups)

# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4