# sort function to sort the elememt in a list
#i = [12,3,4,45,55,23,45,22,54,2,5]
#i.sort(reverse=True)
#print(i)

#write a sorting function witout using list.sort function
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print (new_list)