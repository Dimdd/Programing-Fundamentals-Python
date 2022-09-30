# year = int(input())
# happy_year_condition = False
#
# while not happy_year_condition:
#     year += 1
#     set_year = set()
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#
#     happy_year_condition = len(set_year) == len(str(year))
#
# print(year)

# year = int(input())
# current_year = year
# lst=[]
# for i in str(year):
#
#     lst.append(i)
#
#
# print(lst)
year = int(input())
current_year=year
lst=[]

happy_year=False
while not happy_year:
    year+=1


    for i in str(year):
        lst.append(i)
    break
    #     if str(year)[i]!=str(current_year)[i]:
    #         break
    # else:
    #         happy_year=True
    #         print(year)
    #         break
    # if str(year)[0] != str(year)[1] and str(year)[0] != str(year)[2] and str(year)[0] != str(year)[3] and str(year)[1] != str(year)[2] and str(year)[1]!=str(year)[3] and str(year)[3]!=str(year)[2]:
    #
    #     happy_year=True
    print(lst)

print(year)
# for i in range(year, 1000000):
#     year = int(year)
#     year += 1
#     year = str(year)
#
#     if year[0] != year[1] and year[1] != year[2] and year[2] != year[3] and year[0] != year[3] and year[1]!=year[3] and year[0]!=year[2]:
#         print(year)
#         break
