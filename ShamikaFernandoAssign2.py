"""
Author:Shamika Fernando
Date: May 1st and May 20th
Task: INFT1004 Assignment 2 Spending Spree
"""

Nlist=[] #List created to collect and transfer name,max number of items and spending limit to csv file
#nameList =[] #List created to collect only names
listGCE=[] #User_name,initial_limit,Card_Blanace are stored

def menu():
    print("********************************************************************")
    #Welcome message
    print(" Welcome to ODEL gift card maker!")
    print(" Please select an option below to continue.")
    #User_selection variable gives the choice made by the (define,spending spree or quit)
    user_selection=(input(" Press 1 to define a gift card.\n Press 2 to go to spending spree.\n Press 3 to display the list of existing gift cards.\n Press 4 to display the spending history.\n Press q to exit.\n Type here: "))
    print('')
    print("********************************************************************")
    #Defines the gift card
    if user_selection=="1":
        file = open('giftCards.csv','a+')
        file.close()
        #Newcontent=open('giftCards.csv','rt')
        #Newcontent.read()
        #Newcontent.close()
        #Varable User_name gives the name of the card
        #card_limit equal to the value returned by card() function and gives yhe maximum amount user can spend
        #Max items take the value returned by Maxproducts function maximum number of items user wants to buy
        User_name=name()
        card_limit=Card()
        MaxItems=Maxproducts()
       
        #makes a list using User_name,card_limit and MaxItems
        NewString=""
        print("********************************************************************")

        print("Thank you and welcome" , User_name,"! here are your details")
        print("Your gift card name", User_name)
        print("Your card limit", "$",card_limit)
        print("Maximum number of items you are allowed to purchase", MaxItems)
        print('')
        print("********************************************************************")

        #initial_limit is the initial limit of money that was available in the gift card.
        #initial_limit=card_limit
        
        user_card_details=[User_name,card_limit,MaxItems]
        Nlist.append(user_card_details)   
        NewString=(str(user_card_details[0])+","+ str(user_card_details[1])+","+ str(user_card_details[2]))+"\n"
        Newcontent=open('giftCards.csv','at')
        Newcontent.write(NewString)
        Newcontent.close()
        
        Next_Step=selection_after_defining()
        
#----------------------------------------------------------------------------------------------------------------------       
#----------------------------------------------------------------------------------------------------------------------
        if Next_Step=="2":
            #initial_limit is the initial limit of money that was available in the gift card.
            initial_limit=card_limit 
            allGood=True #Program runs until allGood is false
            item_num=0
            Max=0
            avg=0
            listName=[] #List created using the names of items purchased.
            listPrice=[] #List created using the prices of items purchased.
            ListBalance=[] #List created using ending balance after each purchase
            List_start_Balance=[] #List created using starting balance before each purchase
           
            while allGood==True: #while loop is executed only when allgood is equal to true
                item_name=input("Please enter the name of the item you purchased? ") #user is asked to input the name and price of the good each time the while loop is executed
                item_price=Checkprice() #using Checkprice function checks wether user entered a integer
               
               
                if item_price>card_limit : 
                    #price of the item is greater than the remaining balance in the card,
                    #the program shows an message  to the user asking to select a new good
                    allGood=True
                    print("Price of the good is greater than your card balance. Please select another item. ")
                
                else:
                    starting_balance=card_limit
                    card_limit=card_limit-item_price  #card_limit reduces when an item is pruchased
                    item_num=item_num+1  #Number of items brought by the user increases
                    print("Card balance=" ,card_limit)
                    listName.append(item_name)
                    listPrice.append(item_price)
                    List_start_Balance.append(starting_balance) #balance before each purchase
                    ListBalance.append(card_limit) #ending balance after each purchase
                    print("purchase succesful")
                    if  item_price > Max:
                        Max = item_price #The highest priced good user purchased
                        max_good=item_name #The name of the highest priced good
                        
                if item_num>=MaxItems:
                      #user has  reached the maximum number of items allowable program ends.
                      allGood=False
                      print("You have reached the maximum number of purchases")
                    
                    
                if card_limit==0:
                    #user has spent the total gift card amount program ends.
                    allGood=False
                    print("Card balance is 0. You cant purchase anymore")
                    
            print("")
            print("----------------------------------------------------------------")
            print("Name of the gift card:", User_name )  
            print("Initial balance on the gift card:$", initial_limit) #Total money which was in the gift card before spending.  
            print("The most expensive item purchased by the user:",max_good,"$",Max)
            amount_spend=initial_limit-card_limit #Equvation to find the total amount spend by the user
            avg=amount_spend/item_num #average spending by the user
            Card_Blanace=initial_limit-amount_spend
            print("The average expense=$", avg)
            print("Number of items you have purchased=",item_num)
            listGCE=[User_name,initial_limit,Card_Blanace]
            
            
            #purchase history will be saved in a file named “spendingHistory.csv” (gift-card name, current balance, name of the item purchased, price, ending balance).
            for i in range(0, len(listName)):
                String=( str(listGCE[0])+","+ str(List_start_Balance[i])+","+ str(listName[i])+","+ str(listPrice[i])+"," + str(ListBalance[i])+"\n")
                content=open('spendingHistory.csv','at')
                content.write(String)
                content.close()
                
            menu()
                
                
        if Next_Step=="q":
             print("Thank you!. Have a nice day.")
#----------------------------------------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------------------------------------
    #4th option for the main menue
    elif user_selection=="3":
            infile=open('giftCards.csv','rt')
            blog=infile.readlines()
            infile.close()
            for giftrow in blog:
                newrowlist=giftrow.split(",")
                new_gift_string=("Card name:"+str(newrowlist[0])+",  "+"Item price:"+str(newrowlist[1])+",  "+"Max number of items:"+str(newrowlist[2]))
                print(new_gift_string)
            
            
            menu()
            
#----------------------------------------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------------------------------------
    #5th Option for the main menuw
    elif user_selection=="4":
            #diplayList=[]
            infile2=open('spendingHistory.csv','rt')
            newlist=infile2.readlines()
            infile2.close()
            for row in newlist:
                rowlist=row.split(",")
                newstring=("Item name:"+str(rowlist[2])+",  "+"Item price:"+str(rowlist[1])+",  "+"Card Name:"+str(rowlist[0]))
                print(newstring)
                
            menu()
    
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
    
    #If user selects 2 he will get a defualt card
    elif user_selection=="2":
        User_name="Victory-day gift card"
        card_limit=200  #card_limit equal to the value returned by card() function
        MaxItems=4 #Max items take the value returned by Maxproducts function
        #the parts defined above are used to create user_card_details list 
        user_card_details=[User_name,card_limit,MaxItems]

        Nlist.append(user_card_details)
        print("Thank you and welcome" , User_name,"! here are your details")
        print("Your gift card name", User_name)
        print("Your card limit", "$",card_limit)
        print("Maximum number of items you are allowed to purchase", MaxItems)
        #initial_limit is the initial limit of money that was available in the gift card.
        #initial_limit=card_limit
        
        NewString=( str(user_card_details[0])+"," + str(user_card_details[1])+"," + str(user_card_details[2]))+"\n"
            
        Newcontent=open('giftCards.csv','at')
        Newcontent.write(NewString)
        Newcontent.close()
        
        initial_limit=card_limit 
        allGood=True #Program runs until allGood is false
        item_num=0
        Max=0
        avg=0
        listName=[]
        listPrice=[]
        ListBalance=[] #List created using ending balance after each purchase
        List_start_Balance=[] #List created using starting balance before each purchase
        
        while allGood==True: #while loop is executed only when allgood is equal to true
            item_name=input("Please enter the name of the item you purchased? ") #user is asked to input the name and price of the good each time the while loop is executed
            item_price=Checkprice()
           
           
            if item_price>card_limit : 
                #price of the item is greater than the remaining balance in the card,
                #the program shows an message  to the user asking to select a new good
                allGood=True
                print("Price of the good is greater than your card balance. Please select another item. ")
            
            else:
                starting_balance=card_limit
                card_limit=card_limit-item_price  #card_limit reduces when an item is pruchased
                item_num=item_num+1  #Number of items brought by the user increases
                print("Card balance=" ,card_limit)
                listName.append(item_name)
                listPrice.append(item_price)
                List_start_Balance.append(starting_balance) #balance before each purchase
                ListBalance.append(card_limit) #ending balance after each purchase
                print("purchase succesful")
                if  item_price > Max:
                    Max = item_price #The highest priced good user purchased
                    max_good=item_name #The name of the highest priced good
                    
            if item_num>=MaxItems:
                  #user has  reached the maximum number of items allowable program ends.
                  allGood=False
                  print("You have reached the maximum number of purchases")
                
                
            if card_limit==0:
                #user has spent the total gift card amount program ends.
                allGood=False
                print("Card balance is 0. You cant purchase anymore")
                
        print("")
        print("----------------------------------------------------------------")
        print("Name of the gift card:", User_name )  
        print("Initial balance on the gift card:$", initial_limit) #Total money which was in the gift card before spending.  
        print("The most expensive item purchased by the user:",max_good,"$",Max)
        amount_spend=initial_limit-card_limit #Equvation to find the total amount spend by the user
        avg=amount_spend/item_num #average spending by the user
        Card_Blanace=initial_limit-amount_spend
        print("The average expense=$", avg)
        print("Number of items you have purchased=",item_num)
        #List created to 
        listGCE=[User_name,initial_limit,Card_Blanace]
        #should the card balance be the balance after all the purchases or after individual purchases.
        
        #Add user information (gift-card name, currentbalance, name of the item purchased, price, ending balance).to giftCards.csv
        for i in range(0, len(listName)):
            String=(str(listGCE[0])+"," + str(List_start_Balance[i])+","+ str(listName[i])+","+ str(listPrice[i])+"," +str(ListBalance[i])+"\n")
            content=open('spendingHistory.csv','at')
            content.write(String)
            content.close()
            
        menu()
        
        
#----------------------------------------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------------------------------------
    #5th option in the main menu
    elif user_selection=="q":
        print("Thank you!. Have a nice day.")
#----------------------------------------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------------------------------------        
    #If user dosent select the valid input from the main menu.    
    else:
        print("Please enter a valid input")
        print("")
        menu()
        
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#Selection made after defining the gift card 
def selection_after_defining():
    print("Thank you for your time. Select the next step!")
    Valid_user_choice=False
    while Valid_user_choice==False:
        user_selection_two=(input(" Press 2 to  go to spending spree. \n press q to exit.\n Type your selection:?"))
        if user_selection_two=="2":
            return user_selection_two
        
        elif user_selection_two=="q":
            return user_selection_two
        
        elif user_selection_two=="3":
            infile=open('giftCards.csv','rt')
            blog=infile.readlines()
            infile.close()
            print(blog) 
        elif user_selection_two=="4":
            infile2=open('giftCards.csv','rt')
            blog2=infile2.read()
            infile2.close()
            print(blog2) 
        else:
            print('Invalid choice. select 2 to  go to spending spree or press q to exit')
        
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
def name():
    #Checks if the name entered by the user is their in the csv file.
    Newcontent=open('giftCards.csv','rt')
    InfoList=Newcontent.readlines()
    Newcontent.close()
    Is_name_similar=False
    #Is the new list created using 0th index newlist. This list only contains names and is used to check if the same name is repeted.
    NAME_LIST=[] 
    if len(InfoList)<=0:
        user_card_name=input(str("Please enter the name you like to have on your gift card? "))
        return user_card_name
    if len(InfoList)>0:
        for name in InfoList:
            newList = name.split(',')
            NAME_LIST.append(str(newList[0]))
            
    
    Is_name_similar=False
    #Read .csv file with user names
    #Define nameList from this .csv file
    for Cardname in NAME_LIST:
        while Is_name_similar==False:
            user_card_name=input(str("Please enter the name you like to have on your gift card? "))
            if user_card_name in NAME_LIST :
                print("Please try another name. This name has been already used!")
            
            else:
                return user_card_name
          
               
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
    

#Function card() gives cardlimit of user    
def Card():
    Is_Cardlimit_Valid=False
    while Is_Cardlimit_Valid==False:
        Credit_limit=Checkcard() #checkCard function is used to check wether the entered value in a numeric
            
        if Credit_limit<100:
            print("Please try again entering a value in the range $100-$500")
                #Is_Cardlimit_Valid=False
        
        elif Credit_limit>500:
            print("Please try again entering a value in the range $100-$500")
                #Is_Cardlimit_Valid=False
        
        else:
            return Credit_limit
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#checks wether the entered credit limit is a numeric  
def Checkcard():
    card_limit_not_found=True
    while(card_limit_not_found==True):
        Credit_limit=(input("Please enter the maximum limit ($100-$500) you like to spend? $ "))

        #Check if card limit is a number
        if(Credit_limit.isnumeric()):
            #This is a happy case we will now use this user input
            return int(Credit_limit)

        else:
            #This is the sad case we will now rerun the loop
            print("Invalid input, please enter a valid input.")        

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#select the maximum number of items user can select
def Maxproducts():
    Max_limit=True
    while Max_limit==True:
        NumberOfItems=CheckMaxproduct()
            
            
        if NumberOfItems<1:
            print("Please try again by entering a value in the range 1-5")
            
        
        elif NumberOfItems>5:
            print("Please try again by entering a value in the range 1-5")
             
        
        else:
            return NumberOfItems
        
        
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------        
#checks wether the entered number of items is a numeric        
def CheckMaxproduct():
    card_limit_not_found=True
    while(card_limit_not_found==True):
        NumberOfItems = input("please enter the number of items (1-5) you like to buy? ")

        #Check if card limit is a number
        if(NumberOfItems.isnumeric()):
            #This is a happy case we will now use this user input
            return int(NumberOfItems)

        else:
            #This is the sad case we will now rerun the loop
            print("Invalid input, please enter a valid input.")
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#checks wether the entered price is a numeric
def Checkprice():
    card_limit_not_found=True
    while(card_limit_not_found==True):
        price = input("Enter the price of item:")

        #Check if card limit is a number
        if(price.isnumeric()):
            #This is a happy case we will now use this user input
            return int(price)

        else:
            #This is the sad case we will now rerun the loop
            print("Invalid input, please enter a valid input.")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------


menu()