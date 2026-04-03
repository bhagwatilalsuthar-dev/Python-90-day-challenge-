import calendar
year=int(input('enter your year:...'))
month=int(input('enter your month:..'))
cal=calendar.month(year,month)
# print(cal)


nums=[
    [2,3],
    [4,5]
]
def sumRowColumn(ListOfSum):
 i=0
 j=0
 while i<len(ListOfSum):
    i+=ListOfSum
    print(i)



sumRowColumn(nums)