def change(point, lis, ans):
    left, right, top, under = '', '' ,'', ''
    point2 = [i for i in point]
    lis.append(point)
    
    #change button left
    left += point2[0]
    left += point2[1]
    left += str(int(point2[2])-1)
    lis.append(left)
    
    #change button right
    right += point2[0]
    right += point2[1]
    right += str(int(point2[2])+1)
    lis.append(right)
    
    #change button top
    top += point2[0]
    top += str(int(point2[1])-1)
    top += point2[2]
    lis.append(top)

    #change button under
    under += point2[0]
    under += str(int(point2[1])+1)
    under += point2[2]
    lis.append(under)

    for i in lis:
       if '0' not in i and '7' not in i:
           ans.append(i)
    print ans
change(raw_input(), [], [])
