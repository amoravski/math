def max_triple_value_index(plist):
    triple_values = []
    for index, p in enumerate(plist):
        triple_value = p
        if index != 0:
            triple_value -= plist[index-1]
        if index != len(plist)-1:
            triple_value -= plist[index+1]
        triple_values.append(triple_value)
    max_value = max(triple_values)
    max_index = triple_values.index(max_value)
    print(max_index)
    return max_index

def lamarini(plist):
    value = 0
    value_list = []
    while plist:
        max_index = max_triple_value_index(plist)
        value += plist[max_index]
        value_list.append(max_index)
        length = len(plist)
        del plist[max_index]
        if max_index != length-1:
            del plist[max_index]
        if max_index != 0:
            del plist[max_index-1]
        print(plist)
    return value_list, value

print("Prices of lamarini")
plist = [0,4,2,3,4,5,4,4]
print(plist)
list_a, value = lamarini(plist)
print("Best possible total value of lamarini")
print(value)
