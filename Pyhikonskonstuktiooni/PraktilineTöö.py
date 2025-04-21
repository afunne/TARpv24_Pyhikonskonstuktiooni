import random

d = {} # initialize empty dictionary 

# Create and write to input.txt
with open('kusimused_vastused.txt', 'w') as f:
    f.write("what is the best drink on this world?: kvass\nhow much robux I have?: 300") 

# Read and process the file into a dictionary
with open('kusimused_vastused.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(':', 1)
        d[key.strip()] = value.strip()
print(d)

Q = random.choice(list(d.keys()))
print(Q)








