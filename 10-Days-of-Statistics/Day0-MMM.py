n = int(input())

if (10<=n<=2500):
    ar = str(input())
    num_list = list((ar.split(' ')))
    for i in range(0, len(num_list)):
        num_list[i] = int(num_list[i])
    num_list.sort()

    mean = float(((sum(num_list))/(len(num_list))))
    
    len_sorted_list = len(num_list)
    if len_sorted_list % 2 == 0:
        middle_term = len_sorted_list // 2
        middle_element_1 = num_list[middle_term - 1]
        middle_element_2 = num_list[middle_term]
        median = (middle_element_1 + middle_element_2) / 2
    else:
        middle_element = num_list[((len_sorted_list)//2)]
        median = ((middle_element)/2)
        
    occurences = {num: num_list.count(num) for num in num_list}
    max_occurences = max(occurences.values())
    max_occurences_element = [key for key, value in occurences.items()if value == max_occurences]
    
    mode = min(max_occurences_element)
    
    print(mean)
    print(median)
    print(mode)
