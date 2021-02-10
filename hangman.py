winning_name = 'shayam'
data = list(winning_name)
blanks = "_"*len(winning_name)
blank_list = list(blanks)
count = 3
for j in range(0,len(winning_name)):
    if count != 0 and blank_list != data:
        x= input(f"enter value{j}")
    for i in range(0,len(winning_name)):
        if winning_name[i] in x and count!=0:
            blank_list[i]=x
            print(blank_list)
            if blank_list == data:
                print('you won')
        else:
            if(winning_name.find(x) == -1 and count!=0):
                count -= 1
                print(f'you have {count} chance')
                if(count==0):
                    print("out of game")
                break


