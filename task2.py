import mysql.connector
income=1000
import datetime

budget=[]
while 1:
    
        expenses_name=input("enter the expenses name: ")
        expenses=int(input("enter the expenses: "))
        print("select the categori")
        z=int(input("""1.Food\n2.rent\n3.tansportation\n4.Other\n: """))
        if z==1:
            categories="Food"
        elif z==2:
            categories="rent"
        elif z==3:
            categories="Transport"
        elif z==4:
            categories="Other"
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vishnu@123",
            database="cr"
        )
        budget=income-expenses
        cursor = conn.cursor()
        insert_query = f"INSERT INTO budget VALUES (CURRENT_DATE,'{categories}','{expenses_name}','{expenses}','{budget}')"
        cursor.execute(insert_query)
        print(f"you're added {expenses_name} ({expenses}) to your expenses.")
        insert_query = f"SELECT  price FROM budget WHERE date >= DATE_FORMAT(CURRENT_DATE, '%Y-%m-01') AND date < DATE_ADD(DATE_FORMAT(CURRENT_DATE, '%Y-%m-01'), INTERVAL 1 MONTH);"
        cursor.execute(insert_query)
        rows = cursor.fetchall()
        total_expencses=0
        i=1
        for row in rows:
            total_expencses+=int(row[0])
            i+=1
        print(f"you have {i} expenses totaling ",total_expencses)
        m=["Food","rent" ,"Transport" ,"Other"]
        f=1
        total_expencses
        for i in m:
            insert_query = f"SELECT  price FROM budget WHERE categories='{i}' AND date >= DATE_FORMAT(CURRENT_DATE, '%Y-%m-01') AND date < DATE_ADD(DATE_FORMAT(CURRENT_DATE, '%Y-%m-01'), INTERVAL 1 MONTH);"
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            x=0
            for row in rows:
                x+=int(row[0])
            print(f"{f}.{i}={x}")   
            f+=1
        print("\n")          
        print("budget")
        print(f"you have {abs(total_expencses-income)} left to spend this month")
        tot=abs(total_expencses-income)
        
        def days_in_current_month():
            current_date = datetime.datetime.now()
            year = current_date.year
            month = current_date.month
            next_month = month % 12 + 1
            next_year = year + month // 12
            first_day_of_next_month = datetime.date(next_year, next_month, 1)
            last_day_of_month = first_day_of_next_month - datetime.timedelta(days=1)
            return last_day_of_month.day

        print(f"that's roughly {tot/days_in_current_month()} per day")
        conn.commit()
        cursor.close()
        conn.close()
        


