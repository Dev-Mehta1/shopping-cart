
complist = []
shoplist = []
item = 0
itemcount = 1
ending = "st"
shoppingend = "no"
removeitem = 0
removemore = "yes"


adm = input("are you a shopper or admin(a) :   ")
if adm == "a" :
    adm_access = input("enter the password :  ")
    if adm_access == "passtheword" :
        print("access granted")
else :
    while shoppingend == "no" :
        print(
            '''
enter(x) to end shopping 
to remove item enter(r).
            '''
        )
        print("enter your",str(itemcount)+ending,"item :")
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

        if item == "x" :
            shoppingend = "yes"
        elif item == "r" :
            while removemore == "yes" :
                print("your shopping list :")
                for obj in shoplist :
                    print(obj)
                removeitem = input("enter the unwanted item :  ")
                shoplist.remove(removeitem)
                print("your shopping list :")
                for obj in shoplist :
                    print(obj)
                removemore = input("want to remove more items (yes/no) :  ") 
                
        else : 
            shoplist.append(item)
            for obj in shoplist :
                print(obj)
    

    print(item)
        
