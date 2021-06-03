import mysql.connector

# GLOBAL VARIABLES DECLARATION
myConnnection = ""
cursor = ""
user_Name = ""
password = ""
room_rent = 0
restaurant_bill = 0
gaming_bill = 0
fashion_bill = 0
total_Amount = 0
customer_id = ""
grand_Total = 0


# MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
    global myConnection
    myConnection = mysql.connector.connect(host="localhost", user="root", password="sunny2001")
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor = myConnection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")


# MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection():
    global user_Name
    global password
    global myConnection
    global customer_id
    myConnection = mysql.connector.connect(host="localhost", user="root", passwd="sunny2001", database="HMS")
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()


# FUNCTION FOR USER INFORMATION
def userEntry():
    global customer_id
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"""
        cursor.execute(createTable)
        customer_id = input("Enter Customer Identification Number:")
        name = input("Enter Customer Name : ")
        address = input("Enter Customer Address : ")
        age = input("Enter Customer Age : ")
        nationality = input("Enter Customer Country : ")
        phone_no = input("Enter Customer Contact Number : ")
        email = input("Enter Customer Email : ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = [customer_id, name, address, age, nationality, phone_no, email]
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\n New Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")



# FUNCTION FOR USERS BOOKING RECORD

def bookingRecord():
    global customer_id
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = "CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE)"
            cursor.execute(createTable)
            checkin = input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
            checkout = input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
            sql = "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values = (customer_id, checkin, checkout)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# FUNCTION TO CALCULATE ROOM RENT BASED ON THE INPUT
def roomRent():
    global customer_id
    customer = searchCustomer()
    if customer:
        global room_rent
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"""
            cursor.execute(createTable)
            print("\n ##### We have The Following Rooms For You #####")
            print(" 1. Ultra Royal ----> 10000 Rs.")
            print(" 2. Royal ----> 5000 Rs. ")
            print(" 3. Elite ----> 3500 Rs. ")
            print(" 4. Budget ----> 2500 USD ")
            room_choice = int(input("Enter Your Option : "))
            room_no = int(input("Enter Customer Room No : "))
            no_of_days = int(input("Enter No. Of Days : "))
            if room_choice == 1:
                room_rent = no_of_days * 10000
                print("\nUltra Royal Room Rent : ", room_rent)

            elif room_choice == 2:
                room_rent = no_of_days * 5000
                print("\nRoyal Room Rent : ", room_rent)
            elif room_choice == 3:
                room_rent = no_of_days * 3500
                print("\nElite Royal Room Rent : ", room_rent)
            elif room_choice == 4:
                room_rent = no_of_days * 2500
                print("\nBudget Room Rent : ", room_rent)
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                sql = "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
                values = (customer_id, room_choice, no_of_days, room_no, room_rent)
                cursor.execute(sql, values)
                cursor.execute("COMMIT")
                print("Thank You , Your Room Has Been Booked For : ", no_of_days, "Days")
                print("Your Total Room Rent is : Rs. ", room_rent)
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")



# FUNCTION TO CALCULATE RESTAURENT EXPENSES
def Restaurant():
    global customer_id
    customer = searchCustomer()
    if customer:
        global restaurant_bill
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS RESTAURENT(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"""


            cursor.execute(createTable)
            print("1. Vegetarian Combo -----> 300 Rs.")
            print("2. Non-Vegetarian Combo -----> 500 Rs.")
            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
            choice_dish = int(input("Enter Your Cusine : "))
            quantity = int(input("Enter Quantity : "))
            if choice_dish == 1:
                print("\nSO YOU HAVE ORDER: Vegetarian Combo ")
                restaurant_bill = quantity * 300
            elif choice_dish == 2:
                print("\nSO YOU HAVE ORDER: Non-Vegetarian Combo ")
                restaurant_bill = quantity * 500

            elif choice_dish == 3:
                print("\nSO YOU HAVE ORDER: Vegetarian & Non-Vegetarian Combo ")
                restaurant_bill = quantity * 750
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")

                sql = "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s)"
                values = (customer_id, choice_dish, quantity, restaurant_bill)
                cursor.execute(sql, values)
                cursor.execute("COMMIT")
                print("Your Total Bill Amount Is : Rs. ", restaurant_bill)
                print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
                cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    else:
        pass


def Gaming():                                                                   # FUNCTION TO CALCULATE GAMING EXPENSES
    global customer_id
    customer = searchCustomer()
    if customer:
        global gaming_bill
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("""
            1. Table Tennis -----> 150 Rs./HR
            2. Bowling -----> 100 Rs./HR
            3. Snooker -----> 250 Rs./HR
            4. VR World Gaming -----> 400 Rs./HR
            5. Video Games -----> 300 Rs./HR
            6. Swimming Pool Games -----> 350 Rs./HR
            7. Exit
            """)
            game = int(input("Enter What Game You Want To Play : "))
            hour = int(input("Enter No Of Hours You Want To Play : "))
            print("\n\n#################################################")
            if game == 1:
                print("YOU HAVE SELECTED TO PLAY : Table Tennis")
                gaming_bill = hour * 150
            elif game == 2:
                print("YOU HAVE SELECTED TO PLAY : Bowling")
                gaming_bill = hour * 100
            elif game == 3:
                print("YOU HAVE SELECTED TO PLAY : Snooker")
                gaming_bill = hour * 250
            elif game == 4:
                print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
                gaming_bill = hour * 400
            elif game == 5:
                print("YOU HAVE SELECTED TO PLAY : Video Games")
                gaming_bill = hour * 300
            elif game == 6:
                print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
                gaming_bill = hour * 350
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                sql = "INSERT INTO GAMING VALUES(%s,%s,%s,%s)"
                values = (customer_id, game, hour, gaming_bill)
                cursor.execute(sql, values)
                cursor.execute("COMMIT")
                print("Your Total Gaming Bill Is : Rs. ", gaming_bill)
                print("FOR : ", hour, " HOURS", "\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
                print("\n\n#################################################")
                cursor.close()
        else:
            print("ERROR ESTABLISHING MYSQL CONNECTION !")



def Fashion():                                                                  # FUNCTION TO CALCULATE FASHION EXPENSES
    global customer_id
    customer = searchCustomer()
    if customer:
        global fashion_bill
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS 
            FASHION(CID VARCHAR(20),
            DRESS VARCHAR(30),
            AMOUNT VARCHAR(30),
            BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("""
                        1. Shirts -----> 1500 Rs.
                        2. T-Shirts -----> 300 Rs.
                        3. Pants -----> 2000 Rs.
                        4. Jeans -----> 4000 Rs.
                        5. Tassel top -----> 500 Rs.
                        6. Gown -----> 3000 Rs.
                        7. Western dress -----> 3000 Rs.
                        8. Skirts -----> 400 Rs.
                        9. Trousers -----> 200 Rs.
                        10. InnerWear -----> 30 Rs.
                        """)
            dress = int(input("Enter the your Choice wear: "))
            quantity = int(input("How many you want to buy: "))
            if dress == 1:
                print("\nShirts")
                fashion_bill = quantity * 1500
            elif dress == 2:
                print("\nT-Shirts")
                fashion_bill = quantity * 300
            elif dress == 3:
                print("\nPants")
                fashion_bill = quantity * 2000
            elif dress == 4:
                print("\nJeans")
                fashion_bill = quantity * 4000
            elif dress == 5:
                print("\nTassel top")
                fashion_bill = quantity * 500
            elif dress == 6:
                print("\nGown")
                fashion_bill = quantity * 3000
            elif dress == 7:
                print("\nWestern dress")
                fashion_bill = quantity * 3000
            elif dress == 8:
                print("\nSkirts")
                fashion_bill = quantity * 400
            elif dress == 9:
                print("\nTrousers")
                fashion_bill = quantity * 200
            elif dress == 10:
                print("\nInnerWear")
                fashion_bill = quantity * 30
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                sql = "INSERT INTO FASHION VALUES(%s,%s,%s,%s)"
                values = (customer_id, dress, quantity, fashion_bill)
                cursor.execute(sql, values)
                cursor.execute("COMMIT")
                print("\n\n#################################################")
                print("\nYOU SELECT ITEM NO : ", dress, "\nYOUR QUANTITY IS : ", quantity, " ITEMS",
                      "\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!")
                print("\nYour Total Bill Is : ", fashion_bill)
                print("\n\n#################################################")
                cursor.close()

        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")


def totalAmount():                                                                     # FUNCTION TO ADD UP ALL EXPENSES
    global customer_id
    customer = searchCustomer()
    if customer:
        global grand_Total
        global room_rent
        global restaurant_bill
        global fashion_bill
        global gaming_bill
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS 
            TOTAL(CID VARCHAR(20),
            C_NAME VARCHAR(30),
            ROOMRENT INT ,
            RESTAURENTBILL INT ,
            GAMINGBILL INT,
            FASHIONBILL INT,
            TOTALAMOUNT INT)"""
            cursor.execute(createTable)
            sql = "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
            name = input("Enter Customer Name : ")
            grand_Total = room_rent + restaurant_bill + fashion_bill + gaming_bill
            values = (customer_id, name, room_rent, restaurant_bill, gaming_bill, fashion_bill, grand_Total)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n **** CROWN PLAZA MIAMI **** CUSTOMER BIILING ****")
            print("\n CUSTOMER NAME : ", name)
            print("\nROOM RENT : Rs. ", room_rent)
            print("\nRESTAURENT BILL : Rs. ", restaurant_bill)
            print("\nFASHION BILL : Rs. ", fashion_bill)
            print("\nGAMING BILL : Rs. ", gaming_bill)
            print("___________________________________________________")
            print("\nTOTAL AMOUNT : Rs. ", grand_Total)
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


def searchOldBill():                                                # FUNCTION TO FIND IF ANY PREVIOUS BILL IS AVAILABLE
    global customer_id
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql = "SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql, (customer_id,))
            data = cursor.fetchall()
            if data:
                print(data)
            else:
                print("Record Not Found Try Again !")
                cursor.close()
        else:
            print("\nSomthing Went Wrong ,Please Try Again !")


def searchCustomer():                                                         # FUNCTION TO SEARCH DETAILS OF A CUSTOMER
    global customer_id
    if myConnection:
        cursor = myConnection.cursor()
        cid = input("ENTER CUSTOMER ID : ")
        sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again !")
            return False
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")



myConnection = MYSQLconnectionCheck()                                                           # Main Body Starts
if myConnection:
    MYSQLconnection()
    while True:
        print("""
        ---------------------------------------------
        |    1--->Enter Customer Details             |
        |    2--->Booking Record                     |
        |    3--->Calculate Room Rent                |
        |    4--->Calculate Restaurant Bill          |
        |    5--->Calculate Gaming Bill              |
        |    6--->Calculate Fashion store Bill       |
        |    7--->Display Customer Details           |
        |    8--->GENERATE TOTAL BILL AMOUNT         |
        |    9--->GENERATE OLD BILL                  |
        |    10--->EXIT                              |
        ---------------------------------------------
            """)
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            userEntry()
        elif choice == 2:
            bookingRecord()
        elif choice == 3:
            roomRent()
        elif choice == 4:
            Restaurant()
        elif choice == 5:
            Gaming()
        elif choice == 6:
            Fashion()
        elif choice == 7:
            searchCustomer()
        elif choice == 8:
            totalAmount()
        elif choice == 9:
            searchOldBill()
        elif choice == 10:
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")
