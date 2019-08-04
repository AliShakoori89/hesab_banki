import json
import os.path

class Hesab_banki:


    print('1. baz kardan hesab: ')
    print('2.')
    print('3.')
    choise_num=str(input('Select the option you want:  '))
    if choise_num==1:
        #cus_name=str(input('Enter customer name: '))
        #cus_lastname=str(input('Enter customer lastname: '))
        #cus_id=str(input('Enter customer id: '))
        #cus_bank_acount_num=str(input('Enter customer num: '))
        #cus_supply=str(input('Enter supply: '))
        def __init__(self,cus_name,cus_lastname,cus_id,cus_bank_acount_num,cus_supply):
            self.mot1=str(input('Enter customer name: '))
            self.mot2=str(input('Enter customer lastname: '))
            self.mot3=str(input('Enter customer id: '))
            self.mot4=str(input('Enter customer num: '))
            self.mot5=str(input('Enter supply: '))         
        __init__()
        customer_obj = Hesab_banki(cus_name,cus_lastname,cus_id,cus_bank_acount_num,cus_supply)






#cus_specification={}
        #all_cus_specification={}
        #cus_name=
        #cus_lastname=
        #cus_id=
        #cus_bank_acount_num=
        #cus_supply=
        #cus_specification={'Name':cus_name,'lastname':cus_lastname,'bank_account':cus_bank_acount_num,'supply':cus_supply}
        #all_cus_specification[cus_id]=cus_specification

        #if not os.path.isfile('customer_list.json'):
         #   with open('customer_list.json','w')as f:
         #       f.write(json.dumps(d))
        #else:
          #  with open('customer_list.json')as f:
           #     feeds=json.load(f)
            #feeds.update(d)
            #with open('customer_list.json','w') as f:
             #   f.write(json.dumps(feeds))


