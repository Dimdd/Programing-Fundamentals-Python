key_number = int(input())
number_lines = int(input())
lst = []
lst1=[]

for l in range(number_lines):
    letters = input()
    lst.append(letters)
# new_list=new_item for item in lst
for n in range(len(lst)):
    new_list = (chr(ord(lst[n]) + key_number))
    lst1.append(new_list)


word = "".join(lst1)

print(word)
