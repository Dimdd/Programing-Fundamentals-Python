#  You will be given a number. Print the largest number that can be formed from the digits of the given number.


input_number = input()

list_with_numbers = []
for a in input_number:
    list_with_numbers.append(a)
# for i in range(len(list_with_numbers)):
# list_with_numbers[i]=int(list_with_numbers[i]) # convert list with strings in integer numbers
list_with_numbers.sort(reverse=True)  # gives descending order of the list
for b in list_with_numbers:
    print(b, end="")