from tabulate import tabulate
import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    database = "project",
    user = "postgres",
    password = "suraj"
    
)
cursor = conn.cursor()
try:
    cursor.execute("""
            create table itemlist ( 
            id serial primary key,
            category varchar(100) not null,
            purches_At date not null,
            expiry_date date not null,
            quantity varchar(100) not null
        );""")
    conn.commit()
except Exception as e :
    print("ERROR : ",e)
    conn.rollback()

def insert_items():
    cursor = conn.cursor()
    category = input("Enter Item name :")
    purches_at = input("Enter purches date (YYYY-MM-DD):")
    expiry_date =input("Enter expiry date (YYYY-MM-DD):")
    quantity = input("Enter quantity :")
    try:                   
        cursor.execute("insert into itemlist (category,purches_at,expiry_date,quantity) values(trim(%s),%s,%s,trim(%s))",(category,purches_at,expiry_date,quantity))
        conn.commit()
        print("Item Added succesfully ✅") 
    except Exception as i :
        print("ERROR :",i)
        conn.rollback()   
    cursor.close()

def view_items():
    cursor = conn.cursor()
    print("=========== items list ===========")
    cursor.execute("select category,TO_CHAR(purches_at,'YYYY-MM-DD'),TO_CHAR(expiry_date,'YYYY-MM-DD'),quantity from itemlist;")
    data = cursor.fetchall()
    if data:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(data, headers=headers, tablefmt="psql"))
    else:
        print("List is empty 😔")
    cursor.close()

def expiring_items():
    cursor = conn.cursor()
    cursor.execute("select category, TO_CHAR(purches_at,'YYYY-MM-DD'), TO_CHAR(expiry_date,'YYYY-MM-DD'),quantity from itemlist where expiry_date <= current_date + interval '3 days' order by expiry_date;")
    data = cursor.fetchall()
    if data:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(data, headers=headers, tablefmt="psql"))
    else :
        print("NO items expiring soon...👏")
    cursor.close()

def delete_item():
    cursor = conn.cursor()
    del_val = input("enter name of product :")
    try:
        cursor.execute("delete from itemlist where category = (%s);",(del_val,))
        conn.commit()
        print("Item deleted succesfully ✅")
    except Exception as a:
        print("ERROR :",a)
        conn.rollback()
    cursor.close()

def menu():    
    while True:
        print("\n=========== Expiry Tracker ===========\nselect what you want to do (type -1 to exit)")
        print("1.add items\n2.view items\n3.view expiring items\n4.delete items\n=================================")
        choice = int(input("Enter your choise : "))
        match choice:
            case 1 : 
                insert_items()
            case 2 :
                view_items()
            case 3 :
                expiring_items()
            case 4 :
                delete_item()
            case -1 :
                break
            case _ :
                print("invalied input")
menu()