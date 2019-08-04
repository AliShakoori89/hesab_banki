import json
import os.path

class Hesab_banki:
    
    def __init__(self,cus_name,cus_lastname,cus_id,cus_bank_acount_num,cus_supply):       
        self.cus_name=cus_name
        self.cus_lastname=cus_lastname
        self.cus_id=cus_id
        self.cus_bank_acount_num=cus_bank_acount_num
        self.cus_supply=cus_supply


    def deposit (self,cus_sup):
        #print(data[id_search]['suply'])
        the_amount_of_curtains=int(input('How many sheets do you want to add: '))
        data[id_search]['supply']=cus_sup+the_amount_of_curtains
        with open('customer_list.json','w') as f:
            f.write(json.dumps(data))

        

cus_specification={}
all_cus_specification={}
print('optins :')
print('')
print('1. add: ')
print('2. deposit: ')
choise_num=int(input('Enter your choise: '))
if choise_num==1:
    cus_name=str(input('Enter customer name: '))
    cus_lastname=str(input('Enter customer lastname: '))
    cus_id=str(input('Enter customer id: '))
    cus_bank_acount_num=str(input('Enter customer bank acount num: '))
    cus_supply=int(input('Enter supply: '))
    customer_obj=Hesab_banki(cus_name,cus_lastname,cus_id,cus_bank_acount_num,cus_supply)
    cus_specification={'Name':cus_name,'lastname':cus_lastname,'id':cus_id,'bank_account':cus_bank_acount_num,'supply':cus_supply}
    all_cus_specification[cus_id]=cus_specification
    if not os.path.isfile('customer_list.json'):
        with open('customer_list.json','w')as f:
            f.write(json.dumps(all_cus_specification))
    else:
        with open('customer_list.json')as f:
            feeds=json.load(f)
        feeds.update(all_cus_specification)
        with open('customer_list.json','w') as f:
            f.write(json.dumps(feeds))
if choise_num==2:
    id_search=str(input('Enter customer id: '))
    with open('customer_list.json') as f:
        data=json.load(f)
        if id_search in data:
            customer_obj=Hesab_banki(data[id_search]['Name'],data[id_search]['lastname'],data[id_search]['id'],data[id_search]['bank_account'],data[id_search]['supply'])
            #print(data[id_search]['Name'],data[id_search]['lastname'],data[id_search]['id'],data[id_search]['bank_account'],data[id_search]['supply'])
            #customer_select=Hesab_banki(data[id_search]['Name'],data[id_search]['lastname'],data[id_search]['id'],data[id_search]['bank_account'],data[id_search]['supply'])
            #done=customer_obj.deposit(customer_select)
            #print(data[id_search]['supply'])
            cus_sup=data[id_search]['supply']
            customer_obj.deposit(cus_sup)
        else:
            print('')
            print('json file not exist id')
    
    

            
 
    


