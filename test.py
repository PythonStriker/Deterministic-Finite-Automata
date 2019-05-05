List = ['1,4', '2,3,2', '2', '4,4', '3,4', '4']
NewStatus = '2,3,2'
NewList = NewStatus.split(',')
NewList=set(NewList)
NewList=(sorted(set(NewList)))
NewStatus = ",".join(NewList)
print(NewStatus)
