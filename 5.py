num_letters=int(input())
for i in range(97,97+num_letters):
   for a in range(3):
        for b in range(3):
            sorted_string=sorted(chr(i))
            print(sorted_string, end="")


