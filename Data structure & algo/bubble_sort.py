
def bubbleSortForward(get_list):
  for i in range(len(get_list),1,-1):
    for j in range(0,i-1):
      if get_list[j] > get_list[j+1]:
        temp = get_list[j]
        get_list[j] = get_list[j+1]
        get_list[j+1] = temp
  print(get_list)

take_list = [5,2,3,9,8]
bubbleSortForward(take_list)

