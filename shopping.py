
complist = []
shoplist = []
item = 0
itemcount = 1
ending = "st"
shoppingend = "no"
removeitem = 0
removemore = "yes"

def itemremover() :
    print("your shopping list :")
    for obj in shoplist :
        print(obj)
    removeitem = input("enter the unwanted item :  ")
    shoplist.remove(removeitem)
    print("your shopping list :")
    for obj in shoplist :
        return obj
    

adm = input("are you a shopper or admin(a) :   ")
if adm == "a" :
    adm_access = input("enter the password :  ")
    if adm_access == "passtheword" :
        print("access granted")
else :
    while shoppingend == "no" :
        print("Enter your ",str(itemcount)+ending,"item ,enter(finish) to end shopping ,to remove item enter(remove), to see your shopping list enter(veiw) .")
        item = input("enter item here :  ")

        itemcount = itemcount+1
        if itemcount == 1 or itemcount == 21 or itemcount == 31 :
            ending = "st"
        elif itemcount == 2 or itemcount == 22 or itemcount == 32 :
            ending = "nd"
        elif itemcount == 3 or itemcount == 23 or itemcount == 33 :
            ending = "rd"
        else :
            ending = "th"

        if item == "finish" :
            shoppingend = "yes"
        elif item == "remove" :
            while removemore == "yes" :
                itemremover
                removemore = input("want to remove more items (yes/no) :  ") 
                
        else : 
            shoplist.append(item)
    


    print(item)
        
