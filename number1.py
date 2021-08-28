from pyfiglet import Figlet
from termcolor import colored
f=Figlet(font='banner3-D')
print(colored((f.renderText('Iron shop')),'yellow'))
print(colored(' Hello, welcome to the iron shop ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' Staff arrival : 1 ', 'green', attrs=['reverse', 'blink']),colored(' Customers arrival : 2 ', 'green', attrs=['reverse', 'blink']))
print()
enter=int(input( "Please enter your desired number : " ))

# نمایش عملیات مجاز برای کارکنان
def menu_for_Staff():
    print(' 1 - Add','\n','2 - Edit','\n','3 - Search','\n','4 - Remove')

# نمایش لیست موجودی ها برای کارکنان
def show_list_for_Staff():
    for i in range(len(main_list)):
        print(main_list[i]['code number'],'\t',main_list[i]['name'],'\t',main_list[i]['weight'],'\t',main_list[i]['price'],'\t',main_list[i]['count'],'\t')

# تابع افزودن محصول
def add():
    code_number=int(input('enter code number : '))
    name=input('enter name : ')
    weight=float(input('enter weight : '))
    price=int(input('enter price : '))
    count=int(input('enter count : '))
    main_list.append({'code number':code_number,'name':name,'weight':weight,'price':price,'count':count})

# تابع ویرایش محصول
def edit():
    print(colored(' What correction do you want to make ? ', 'yellow', attrs=['reverse', 'blink']))
    print(' 1 - edit code number','\n','2 - edit name','\n','3 - edit weight','\n','4 - edit price','\n','5 - edit count')
    Operation=int(input("Please enter your desired number : "))
    code_number=int(input('Which one of code number do you want to edit ? '))
    for i in range(len(main_list)):
        if main_list[i]['code number']==code_number:
            if Operation==1:
                code_number_2=int(input("new code number ? "))
                main_list[i]["code number"]=code_number_2
            if Operation==2:
                name_2=input("new name ? ")
                main_list[i]["name"]=name_2           
            if Operation==3:
                weight_2=float(input("new weight ? "))
                main_list[i]["weight"]=weight_2
            if Operation==4:
                price_2=int(input("new price ? "))
                main_list[i]["price"]=price_2
            if Operation==5:
                count_2=int(input("new count ? "))
                main_list[i]["count"]=count_2

#  تابع جستجو محصول
def search():
    print(colored('Which one of code number do you want to search ? ', 'yellow', attrs=['reverse', 'blink']))
    while True:
        code_number=int(input("Please enter your desired code number : ")) 
        for i in range(len(main_list)):
            if main_list[i]['code number']==code_number:
                print()
                print(main_list[i]['code number'],'\t',main_list[i]['name'],'\t',main_list[i]['weight'],'\t',main_list[i]['price'],'\t',main_list[i]['count'])
                print()
                print(colored('operation accomplished ', 'green', attrs=['reverse', 'blink']))
                break
        else:
            print(colored('This product does not exist. ', 'red', attrs=['reverse', 'blink']))
        break

# تابع حذف محصول
def remove():
    print(colored('Which one of code number do you want to remove ? ', 'red', attrs=['reverse', 'blink']))
    code_number=int(input("Please enter your desired code number : "))
    for i in range(len(main_list)):
        if main_list[i]['code number']==code_number:
            del main_list[i]
            break

# تابع خرید
purchases=[]
def buy():
    while True:
        code_number=int(input("Please enter your desired code number : "))
        for i in range(len(main_list)):
            if main_list[i]['code number']==code_number:
                ask=int(input("How many do you need ? "))
                if ask<=main_list[i]['count']:
                    purchases.append({'code number':main_list[i]['code number'],'name':main_list[i]['name'],'weight':main_list[i]['weight'],'price':main_list[i]['price'],'count':ask})
                    main_list[i]['count']=main_list[i]['count']-ask
                    print(purchases)
                else:
                    print(colored('Inventory is not enough. We will provide it for you at the first opportunity ', 'red', attrs=['reverse', 'blink']))
                
        print(colored('Do you want to continue shopping ?', 'yellow', attrs=['reverse', 'blink']))
        Continue=input()
        if Continue=='NO' or Continue=='no' or Continue=='n' or Continue=='N': 
            break        

eshtal=open('eshtal.txt','r')
eshtal1=eshtal.read()
ironware=eshtal1.split("\n")
main_list=[]
for i in range(len(ironware)):
    ironware_list=ironware[i].split(',')
    dictionary={}
    dictionary['code number']=int(ironware_list[0])
    dictionary['name']=ironware_list[1]
    dictionary['weight']=float(ironware_list[2])
    dictionary['price']=int(ironware_list[3])
    dictionary['count']=int(ironware_list[4])
    main_list.append(dictionary)

# ورود کارمندان
if enter==1:
    while True:
        username=input('Please enter username : ')
        password=input('Please enter password : ')
        if username=='admin' and password=='admin':
            show_list_for_Staff()
            while True:
                print(colored('What are you going to do ? ', 'yellow', attrs=['reverse', 'blink']))
                menu_for_Staff()
                Operation=int(input('Please enter the desired number : '))
                # افزودن محصول
                if Operation==1:
                    add()
                    show_list_for_Staff()
                    print(colored('operation accomplished ', 'green', attrs=['reverse', 'blink']))
                    print()  
                # ویرایش محصول
                if Operation==2:
                    edit()
                    show_list_for_Staff()
                    print(colored('operation accomplished ', 'green', attrs=['reverse', 'blink']))
                    print()
                # جستجو محصول
                if Operation==3:
                    search()

                    print()
                # حذف محصول
                if Operation==4:
                    remove()
                    show_list_for_Staff()
                    print(colored('operation accomplished ', 'green', attrs=['reverse', 'blink']))
                    print()
        else:
            print(colored('Wrong username or password. Please try again', 'red', attrs=['reverse', 'blink']))

# ورود مشتریان
if enter==2:
    print(colored('Welcome to the shop customers club ', 'white', attrs=['reverse', 'blink']))
    buy()

# جزئیات فاکتور خرید
def detail_factor():
    for i in range(len(purchases)):  
        print(colored('code number : ', 'yellow', attrs=['reverse', 'blink']),purchases[i]['code number'])
        print(colored('name        : ', 'green', attrs=['reverse', 'blink']),purchases[i]['name'])
        print(colored('weight      : ', 'yellow', attrs=['reverse', 'blink']),purchases[i]['weight'])
        print(colored('price       : ', 'green', attrs=['reverse', 'blink']),purchases[i]['price'])
        print(colored('count       : ', 'yellow', attrs=['reverse', 'blink']),purchases[i]['count'])
        print()

# فاکتور کلی خرید
def local_factor():
    Total_purchase_length=0
    Total_purchase_amount=0
    Total_purchase_weight=0
    for i in range(len(purchases)):
        Total_purchase_amount=Total_purchase_amount+(purchases[i]['count']*purchases[i]['price'])
    for i in range(len(purchases)):
        Total_purchase_weight=Total_purchase_weight+(purchases[i]['count']*purchases[i]['weight'])
    for i in range(len(purchases)):
        Total_purchase_length=Total_purchase_length+(purchases[i]['count']*12) # شایان ذکر است که هر شاخه آهن 12 متر طول دارد
    print(colored('Total purchase length : ', 'red', attrs=['reverse', 'blink']),Total_purchase_length,'Metr')
    print(colored('Total purchase amount : ', 'yellow', attrs=['reverse', 'blink']),Total_purchase_amount,'Rial')
    print(colored('Total purchase weight : ', 'red', attrs=['reverse', 'blink']),Total_purchase_weight,'Kg')

detail_factor()
local_factor()