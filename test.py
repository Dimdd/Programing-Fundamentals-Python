year = int(input())
lst=[]

happy_year=False

while not happy_year:
    year+=1
    lst=[]


    for i in str(year):
        lst.append(i)
    if lst.count(str(year)[0])<2 and lst.count(str(year)[1])<2 and \
            lst.count(str(year)[2])<2 and lst.count(str(year)[3])<2 and lst.count(str(year)[4])<2 :
        happy_year=True
        break



print(year)