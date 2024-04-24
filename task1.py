import mysql.connector



while 1:
    choice=int(input("enter the choice to add task press 1\n to remove task press 2\n to mark task as completed press 3 \n press 4 for the show all the tasks\n press 123 to stop all operations and press enter\n: "))
    if choice==1:
        task=input("enter your task:")
        while 1:
            priority_of_range=int(input("press 1 for high\n press 2 for medium\n press 3 for low and press enter\n:"))
            if priority_of_range>3:
                priority_of_range=int(input("please press valid number and press enter:"))
            else:
                break
        if priority_of_range==1:
            priority_of_task="high"
        elif priority_of_range==2:
            priority_of_task="medium"
        else:
            priority_of_task="low"
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vishnu@123",
            database="cr"
        )

        cursor = conn.cursor()
        due_date=input("enter the due date for the task in yyyy-mm-dd formate: ")
        insert_query = f"INSERT INTO todolist (task,priority,due_date,status)  VALUES ('{task}','{priority_of_task}','{due_date}','not done')"
        cursor.execute(insert_query)
        conn.commit()
        cursor.close()
        conn.close()
    elif choice==2:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vishnu@123",
            database="cr"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM todolist"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        chosser=int(input("enter the id number for delete the task: "))
        insert_query = f"DELETE FROM todolist WHERE id = '{chosser}'"
        cursor.execute(insert_query)
        conn.commit()
        print("the taks has been deleted")
        cursor.close()
        conn.close()
    elif choice==3:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vishnu@123",
            database="cr"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM todolist"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        chosser=int(input("enter the id number for mark  the task done: "))
        insert_query = f"UPDATE todolist SET status='done' WHERE id = '{chosser}'"
        cursor.execute(insert_query)
        conn.commit()
        print("the task is done")
        query = f"SELECT * FROM todolist where id='{chosser}'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        
    elif choice==123:
        print("the process stoped")
        break
    elif choice==4:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vishnu@123",
            database="cr"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM todolist"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("please enter the valid choice :")