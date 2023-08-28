# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    list=[]
    scorevalue=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        list+=[[name,score]]
        scorevalue.append(score)
    list.sort()    
    scorevalue.sort()
    min=scorevalue[0]
    second_min=0
    for i in scorevalue:
        if i !=min:
            second_min=i
            break
    for ele in list:
        if(second_min==ele[1]):
            print(ele[0])
        
    
        
