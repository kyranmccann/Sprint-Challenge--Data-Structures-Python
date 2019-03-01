import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# given code runtime: 9.342793703079224 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# solution 1 (under 1 second):
# duplicates = []
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)
# solution 2 runtime: 0.0069811344146728516 seconds:
duplicates = []
holder = {}
for name_1 in names_1:
    holder[name_1] = True

for name_2 in names_2:
    if holder.get(name_2, None):
        duplicates.append(name_2)
# one more try runtime: 0.00603938102722168 seconds
# i found this strategy online. the underlying data scructure in the set is a dictionary.
# duplicates = list(set(names_1) & set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
