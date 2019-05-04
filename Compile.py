global NFA_StautsMatrix,DFA_StautsMatrix,StartWorld,EndWorld,\
    StatusNumber,EnterNumber,EnterWorld,NFA_StatusWorld,DFA_StatusWrold
EnterWorld = []                                                                    #输入状态
NFA_StatusWorld = []                                                               #NFA有穷状态集
DFA_StatusWrold = []                                                               #DFA有穷状态集

def main():
    global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
        StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld,DFA_StatusWrold
    StartWorld = input("输入开始状态:")
    EndWorld = input("输入结束状态:")
    StatusNumber = int(input("输入状态个数:"))
    EnterNumber = int(input("状态机输入个数:"))
    print("输入不确定又穷状态机转换表:")
    NFA_StautsMatrix = [[] for _ in range(0,EnterNumber + 1)]                      #NFA状态转换表
    for row in range(0,StatusNumber + 1):                                          #存入状态转换表
        line  = input().split(' ')
        for column in range(len(line)):
            NFA_StautsMatrix[row].append(line[column])

    for enter in NFA_StautsMatrix[0]:                                              #存入输入状态
        if enter!='\\' and enter!='&':
            EnterWorld.append(enter)

    for row in range(1,EnterNumber+1):                                             #NFA有穷状态集
        NFA_StatusWorld.append(NFA_StautsMatrix[row][0])
    print(Frist_Closure(StartWorld),DFA_StatusWrold)

#-----------------------------------------------------------------------------------------------------------------------#
def Frist_Closure(string):
    global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld,\
        StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld,DFA_StatusWrold
    List = []
    flag = 0
    NewStatus = string
    if ',' not in string:
        while flag == 0 :
            for row in range(1,EnterNumber+1):
                if ',' not in string:
                    if string == NFA_StautsMatrix[row][0]:
                        if NFA_StautsMatrix[row][1]!='&' and NFA_StautsMatrix[row][1]!='*':
                            if NFA_StautsMatrix[row][1] not in NewStatus:
                                NewStatus = NewStatus+','+NFA_StautsMatrix[row][1]
                                string = NFA_StautsMatrix[row][1]
                            else:
                                flag = 1
                        else:
                            flag = 1
                else:
                    List = string.split(',')
                    for number in range(len(List)):
                        if List[number] not in NewStatus:
                            NewStatus = NewStatus+','+List[number]
                            string = List[number]
                        elif List[number] in NewStatus and List[number] in NewStatus:
                            flag = 1
                            break
        if NewStatus not in DFA_StatusWrold:
            DFA_StatusWrold.append(NewStatus)
        return NewStatus
    else:
        List = string.split(',')
        for number in List:
            for row in range(1,EnterNumber+1):
                if number == NFA_StautsMatrix[row][0]:
                    if ',' not in NFA_StautsMatrix[row][1]:
                        if NFA_StautsMatrix[row][1] != '&' and NFA_StautsMatrix[row][1] != '*':
                            if NFA_StautsMatrix[row][1] not in NewStatus:
                                NewStatus = NewStatus + ',' + NFA_StautsMatrix[row][1]
                            else:
                                pass
                        else:
                            break
        if NewStatus not in DFA_StatusWrold:
            DFA_StatusWrold.append(NewStatus)
        return NewStatus

def Second_Closure(string,enter):
    global NFA_StautsMatrix, DFA_StautsMatrix, StartWorld, EndWorld, \
        StatusNumber, EnterNumber, EnterWorld, NFA_StatusWorld,DFA_StatusWrold
    List = []
    if ',' not in string:
        pass
    else:
        List = string.split(',')
        for number in List:
            for row in range(1, EnterNumber + 1):
                if number == NFA_StautsMatrix[row][0]:
                    #NFA_StatusWorld.index(enter)
                    pass


#-----------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()