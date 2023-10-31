def menu():
    print("FOOTBALL CLUB MANAGEMENT")

    print("\n")
    print("1.Members Entry Team1")
    print("2.Members Entry Team2")
    print("3.Members Entry Team3")
    print("4.Simulate match")
    print("5.Remove players from any team")
    print("6.Update Player goals")
    print("7.Update player trophies")
    print("8.Swap players between teams")
    print("9.Display TEAM1")
    print("10.Display TEAM2")
    print("11.DISPLAY TEAM3")
    print("12.Compare Team Statistics")
    print("13.Compare Player Statistics")

    choice =int(input("Enter your choice:"))
    
    if choice ==1:
        adddata1()
    elif choice==2:
        adddata2()
    elif choice==3:
        adddata3()
    elif choice==4:
        match()
    elif choice==5:
        remove()
    elif choice==6:
        updatedata1()
    elif choice==7:
        updatedata2()
    elif choice==8:
        swap()
    elif choice==9:
        fetchdata1()
    elif choice==10:
        fetchdata2()
    elif choice==11:
        fetchdata3()
    elif choice==12:
        compare()
    elif choice==13:
        display()
    
    elif(choice < 1 or choice > 13): 
        print("Please Enter Valid Option")
    else:
        print("wrong input")

def db():
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", password="1234")
    cursor=mycon.cursor()
    q="create database if not exists teams"
    cursor.execute(q)
db()
# Creating team by adding players to the teams
def adddata1():
    c="y"
    while c=="y":
        pid = input('Enter Player ID:')
        pname = input('Enter Player name:')
        pos = input('Enter Position of player:')
        goals =input('Enter No of goals scored/saved:')
        trophies =input('Enter No of trophies earned:')
        nation =input('Enter Nationality of player:')
        print (pid,pname,pos,goals,trophies,nation)
    
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", password="1234", database="teams")
        cursor=mycon.cursor()
        def table(): 
           cursor.execute('Create Table if not exists Team1(PID Integer(11) Not Null Primary key, Playername  varchar(30) Not null,Position varchar(20),Goals int(4), Trophies integer(4), Nationality varchar(20),Entrydate date)')
        def entry():
            q="select curdate()"
            cursor.execute(q)
            d=cursor.fetchone()
            date=d[0]
            print("Date of signing",pname,":",date)
            q="insert into Team1 values({},'{}','{}',{},{},'{}','{}')". format(pid, pname, pos, goals, trophies, nation, date)
            cursor.execute(q)
            mycon.commit()
        table() 
        entry()
        print(cursor.rowcount, "Record Inserted\n")
        c=input("Do you want to add more records?(y/n)")
##################################################################
def adddata2():
    pid = input('Enter Player ID:')
    pname = input('Enter Player name:')
    pos = input('Enter Position of player:')
    goals =input('Enter No of goals scored/saved:')
    trophies =input('Enter No of trophies earned:')
    nation =input('Enter Nationality of player:')
    print (pid,pname,pos,goals,trophies,nation)
    
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", password="1234", database="teams")
    cursor=mycon.cursor()
    def table(): 
        cursor.execute('Create Table if not exists Team2(PID Integer(11) Not Null Primary key, Playername varchar(30) Not null, Position varchar(20),Goals int(4), Trophies integer(4), Nationality varchar(20), Entrydate date)')
   
    def entry():
        q="select curdate()"
        cursor.execute(q)
        d=cursor.fetchone()
        date=d[0]
        print("Date of signing",pname,":",date)
        q="insert into Team2 values ({}, '{}', '{}', {}, {}, '{}', '{}')". Format (pid, pname, pos, goals, trophies, nation, date)
        cursor.execute(q)
        mycon.commit()
    table()
    entry()
    print(cursor.rowcount, "Record Inserted\n")
    c=input("Do you want to add more records?(y/n)")

def adddata3():
    pid = input('Enter Player ID:')
    pname = input('Enter Player name:')
    pos = input('Enter Position of player:')
    goals =input('Enter No of goals scored/saved:')
    trophies =input('Enter No of trophies earned:')
    nation =input('Enter Nationality of player:')
    print (pid,pname,pos,goals,trophies,nation)
   
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", password="1234", database="teams")
    cursor=mycon.cursor()
    
    def table(): 
        cursor.execute('Create Table if not exists Team3(PID Integer(11) Not Null Primary key, Playername varchar(30) Not null,Position varchar(20),Goals int(4), Trophies integer(4), Nationality varchar(20), Entrydate date)')
    def entry():
        q="select curdate()"
        cursor.execute(q)
        d=cursor.fetchone()
        date=d[0]
        print("Date of signing",pname,":",date)
        q="insert into Team3 values ({}, '{}', '{}', {}, {}, '{}', '{}')".  Format (pid, pname, pos, goals, trophies, nation, date)
        cursor.execute(q)
        mycon.commit()
    table() 
    entry()
    print(cursor.rowcount, "Record Inserted\n")

##############################################################
# Displaying team

def fetchdata1():
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
    cursor=mycon.cursor()
    cursor.execute("select * from team1")
    data=cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print("\n")
    print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {:<15}" .format(*headers))
   
    if data is not None:
        for x in data:
            print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {}" .format(*x))
    else:
        print("No Players in Team1")


def fetchdata2():
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
    cursor=mycon.cursor()
    cursor.execute("select * from team2")
    data=cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print("\n")
    print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {:<15}" .format(*headers))
    if data is not None:
       for x in data:    
             print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {}" .format(*x))
    else:
        print("No Players in Team2")


def fetchdata3():
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
    cursor=mycon.cursor()
    cursor.execute("select * from team3")
    data=cursor.fetchall()
    print("\n")
    headers = [i[0] for i in cursor.description]
    print("\n")
    print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {:<15}" .format(*headers))

    if data is not None:
        for x in data:
            print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<15} {}" .format(*x))

    else:
        print("No Players in Team3")
##############################################################
#Removing player from a team

def remove():
    a=int(input("Enter team number(1/2/3):"))
    if a==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def deldata():
             b=int(input("Enter Player Id of player you want to remove from Team 1:"))
             cursor.execute("select * from team1 where PID={}".format(b))
             msg1=cursor.fetchall()
             if msg1:
                sql = "Delete from team1 where PID={}".format(b)
                cursor.execute(sql)
                print("Player removed from Team 1")
                mycon.commit()
             else:
                print ("\n Player to be removed does not exist in Team 1") 
        deldata()
    
    elif a==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team2")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        
        def deldata1():
            b=int(input("Enter Player Id of player you want to remove from Team 2:"))
            cursor.execute("select * from team2 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                sql = "Delete from team2 where PID={}".format(b)
                cursor.execute(sql)
                print("Player removed from Team2")
                mycon.commit()
            else:
                print ("\n Player to be removed does not exist in Team 2") 
        deldata1()
            
        
    elif a==3:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team3")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def deldata2():
            b=int(input("Enter Player Id of player you want to remove from Team 3:"))
            cursor.execute("select * from team3 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                sql = "Delete from team3 where PID={}".format(b)
                cursor.execute(sql)
                print("Player removed from Team 3")
                mycon.commit()
            else:
                print ("\n Player to be removed does not exist in Team 3") 
        deldata2()

#############################################################
# Updating player details like goals scored or trophies awarded
        
def updatedata1():
    a=int(input("Enter team number(1/2/3):"))
    if a==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def changedata():
            b=int(input("Enter Player Id of player you want to Update: "))
            cursor.execute("select * from team1 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter goals scored by player: ")) 
                sql = "Update team1 set Goals={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Goals scored updated")
                mycon.commit()
              
            else:
                print ("\n Player does not exist in Team 1") 
         
        changedata()
                
            
    elif a==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234",  database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team2")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def changedata():
            b=int(input("Enter Player Id of player you want to Update: "))
            cursor.execute("select * from team2 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter goals scored by player: ")) 
                sql = "Update team2 set Goals={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Goals scored updated")
                mycon.commit()
              
            else:
                print ("\n Player does not exist in Team 2") 
        changedata()
        
    elif a==3:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team3")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def changedata():
            b=int(input("Enter Player Id of player you want to Update:"))
            cursor.execute("select * from team3 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter goals scored by player: ")) 
                sql = "Update team3 set Goals={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Goals scored updated")
                mycon.commit()
              
            else:
                print ("\n Player does not exist in Team 3") 
         
        changedata()
    else:
        print("WRONG INPUT,PLEASE TRY AGAIN")
        
##############################################################
def updatedata2():
    a=int(input("Enter team number(1/2/3):"))
    if a==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def changedata():
            b=int(input("Enter Player Id of player you want to Update: "))
            cursor.execute("select * from team1 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter new Trophies of player: ")) 
                sql = "Update team1 set Trophies={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Trophies updated")
                mycon.commit()
                   
            else:
                print ("\n Player does not exist in Team 1")          
        changedata()
        
    elif a==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team2")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
       
        def changedata():
            b=int(input("Enter Player Id of player you want to Update: "))
            cursor.execute("select * from team2 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter new Trophies of player: ")) 
                sql = "Update team2 set Trophies={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Trophies updated")
                mycon.commit()
                   
            else:
                print ("\n Player does not exist in Team 2") 
            
        changedata()
    
    elif a==3:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select * from team3")
        data=cursor.fetchall()
        print("\n")
        for x in data:
            print(x)
        def changedata():
            b=int(input("Enter Player Id of player you want to Update: "))
            cursor.execute("select * from team3 where PID={}".format(b))
            msg1=cursor.fetchall()
            
            if msg1:
                c=int(input("Enter new Trophies of player: ")) 
                sql = "Update team3 set Trophies={} where PID={}".format(c,b)
                cursor.execute(sql)
                print("Trophies updated")
                mycon.commit()
                   
            else:
                print ("\n Player does not exist in Team 3") 
        changedata()
    
    else:
        print("WRONG INPUT,PLEASE TRY AGAIN")

##############################################################
# Comparing goals scored and trophies won by teams

def compare():
    print("1.Team with max goals")
    print("2.Team with max Trophies")
    ch=int(input("enter choice(1/2): "))
    if ch==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()

        q="select sum(Goals) from team1"
        cursor.execute(q)
        a=cursor.fetchone()
        x=a[0]
        print("\n")
        print("Goals scored by Team 1 is:", x)        
        w="select sum(Goals) from team2"
        cursor.execute(w)
        b=cursor.fetchone()
        y=b[0]
        print("Goals scored by Team 2 is:",y) 
        e="select sum(Goals) from team3"
        cursor.execute(e)
        c=cursor.fetchone()
        z=c[0]
        print("Goals scored by Team 3 is:",z)  
        aa=max(x,y,z)
        if x==aa:
            if y==aa:
                 if z==aa:
                     print("\nTEAM 1, TEAM 2 & TEAM 3 HAVE SCORED EQUAL GOALS:", aa)
                 else:
                     print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 1 & TEAM 2:", aa)
            else:
                if z==aa:
                     print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 1 & TEAM 3:", aa)
                else:
                     print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 1:", aa)
                    
                
        elif y==aa:
            if z==aa:
                print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 2 & TEAM 3:", aa)
            else:
                print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 2:", aa)
        else:
            print("\nMAXIMUM GOALS HAVE BEEN SCORED BY TEAM 3:", aa)
              
      
##############################################################
     
    elif ch==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()

        q="select sum(Trophies) from team1"
        cursor.execute(q)
        a=cursor.fetchone()
        x=a[0]
        print("\n")
        print("Trophies won by Team 1 is:", x) 

        w="select sum(Trophies) from team2"
        cursor.execute(w)
        b=cursor.fetchone()
        y=b[0]
        print("Trophies won by Team 2 is:", y) 

        e="select sum(Trophies) from team3"
        cursor.execute(e)
        c=cursor.fetchone()
        z=c[0]
        print("Trophies won by Team 3 is:", z) 
        aa=max(x,y,z)
        if x==aa:
            if y==aa:
                 if z==aa:
                     print("\nTEAM 1, TEAM 2 & TEAM 3 HAVE EQUAL TROPHIES:", aa)
                 else:
                     print("\nTEAM 1 & TEAM 2 HAVE MAXIMUM TROPHIES:", aa, "EACH")
            else:
                if z==aa:
                     print("\nTEAM 1 & TEAM 3 HAVE MAXIMUM TROPHIES:", aa, "EACH")
                else:
                    print("\nTEAM 1 HAS MAXIMUM TROPHIES:", aa)
                    
                
        elif y==aa:
            if z==aa:
                print("\nTEAM 2 & TEAM 3 HAVE MAXIMUM TROPHIES:", aa, "EACH")
            else:
                print("\nTEAM 2 HAS MAXIMUM TROPHIES:", aa)
        else:
            print("\nTEAM 3 HAS MAXIMUM TROPHIES:", aa)
                       
    else:
        print("Wrong Input,Please try Again")

##############################################################
#Displaying players who have scored maximum goals and players who have won maximum trophies 
def display():
    print("1.Max Goals")
    print("2.Max Trophies")
    ch=int(input("enter choice(1/2): "))
    if ch==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        
        q1='select max(goals) from team1'
        cursor.execute(q1)
        p=cursor.fetchone()
        x=p[0]
        
        q2='select max(goals) from team2'
        cursor.execute(q2)
        q=cursor.fetchone()
        y=q[0]
        
        q3='select max(goals) from team3'
        cursor.execute(q3)
        r=cursor.fetchone()
        z=r[0]
        aa=max(x,y,z)
        print(aa)
        cursor.execute("select playername,goals from team1 where goals={}".format(aa))
        data=cursor.fetchall()
        
        print("\nMAXIMUM GOALS HAVE BEEN SCORED BY:")
        for a in data:    
            print("Team1:","Name:",a[0],":","Goals",a[1])
    
        cursor.execute("select playername,goals from team2 where goals={}".format(aa))
        data1=cursor.fetchall()
        for b in data1:    
            print("Team2:","Name:",b[0],":","Goals",b[1])
        
        cursor.execute("select playername,goals from team3 where goals={}".format(aa))
        data2=cursor.fetchall()
        for c in data2:    
            print("Team3:","Name:",c[0],":","Goals",c[1])            

    elif ch==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()

        q="select max(trophies) from team1"
        cursor.execute(q)
        p=cursor.fetchone()
        x=p[0]
        print(x)
    
        w="select max(trophies) from team2"
        cursor.execute(w)
        t=cursor.fetchone()
        y=t[0]
 
        e="select max(trophies) from team3"
        cursor.execute(e)
        r=cursor.fetchone()
        z=r[0]
 
        aa=max(x,y,z)
        print(aa)
        cursor.execute("select playername,trophies from team1 where trophies={}" .format(aa))
        data=cursor.fetchall()
        print("\nPLAYER WITH MAXIMUM TROPHIES:")
        for x in data:    
            print("Team1:","Name:", x[0],":", "Trophies:",x[1])
        cursor.execute("select playername,trophies from team2 where trophies={}".format(aa))
        data1=cursor.fetchall()

        for y in data1:    
            print("Team2:","Name:", y[0],":", "Trophies:",y[1])
        cursor.execute("select playername,trophies from team3 where trophies={}".format(aa))
        data2=cursor.fetchall()

        for z in data2:    
            print("Team3:","Name:", z[0],":", "Trophies:",z[1])
      
##############################################################
# Simulating football match between teams

def match():
    print("You want a match between:")
    print("1.Team 1 and Team 2")
    print("2.Team 1 and Team 3")
    print("3.Team 2 and Team 3")
    ch=int(input("enter choice:"))
    if ch==1:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select PID,Playername,goals,Trophies from team1")
        data=cursor.fetchall()
        print("\n")
        for x in data:    
            print(x)

        print("\n V/S")

        cursor.execute("select PID, Playername, goals, Trophies from team2")
        mdata=cursor.fetchall()
        print("\n")
        for x in mdata:
            print(x)
    elif ch==2:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select PID, Playername, goals, Trophies from team1")
        data=cursor.fetchall()
        print("\n")
        for x in data:    
            print(x)
            
        print("\n V/S")

        cursor.execute("select PID, Playername, goals, Trophies from team3")
        mdata=cursor.fetchall()
        print("\n")
        for x in mdata:
            print(x)
    elif ch==3:
        import mysql.connector as ms
        mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
        cursor=mycon.cursor()
        cursor.execute("select PID, Playername, goals, Trophies from team2")
        data=cursor.fetchall()
        print("\n")
        for x in data:    
            print(x)
        print("\n V/S")
        cursor.execute("select PID, Playername, goals, Trophies from team3")
        mdata=cursor.fetchall()
        print("\n")
        for x in mdata:
            print(x)
    else:
        print("wrong input")

    c=input("Do you want to continue:(y/n):")
    print("\n")
    if c=="y":
        import random
        a=random.randint(0,10)
        b=random.randint(0,10)
        if a>b:
            if ch==1:
                print("\nMatch between Team 1 & Team 2")
                print("Score of the match is:",a," : ",b)
                print("Team 1 won the match!")
            elif ch==3:              
                print("\nMatch between Team 2 & Team 3")
                print("Score of the match is:",a," : ",b)
                print("Team 2 won the match!")
            elif ch==2:
                print("\nMatch between Team 1 & Team 3")
                print("Score of the match is:", a," : ",b)
                print("Team 1 won the match!")
        elif a<b:
            if ch==1:              
                print("\nMatch between Team 1 & Team 2")
                print("Score of the match is:",a,":",b)
                print("Team 2 won the match!")
            elif ch==3:                
                print("\nMatch between Team 2 & Team 3")
                print("Score of the match is:",a,":",b)
                print("Team 3 won the match!")
            elif ch==2:               
                print("\nMatch between Team 1 & Team 3")
                print("Score of the match is:",a,":",b)
                print("Team 3 won the match!")
            
        else:
            print("Score of the match is:",a,":",b)
            print("It is a tie!!!")

###################################################################
#Swapping players from one team to another

def swap():
    import mysql.connector as ms
    mycon=ms.connect(host="localhost", user="root", passwd="1234", database='teams')
    cursor=mycon.cursor()
    print("Swap Players between:")
    print("1.Team1 and Team2")
    print("2.Team1 and Team3")
    print("3.Team2 and Team3")
    ch=int(input("enter your choice:"))
    
    if ch==1:
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        print("TEAM1")
        for x in data:    
            print(x)
        cursor.execute("select * from team2")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM2")
        for x in mdata:
             print(x)

        a=int(input("Enter Player Id of player you want swap from Team1:"))
        c=int(input("Enter Player Id of player you want swap from Team2:"))
        cursor.execute("select * from team1 where PID={}".format(a))
        d=cursor.fetchone()
        print(d[0],d[1], d[2], d[3], d[4], d[5], d[6])
        cursor.execute("select * from team2 where PID={}".format(c))
        e=cursor.fetchone()
        print(e)
        print(d)
        q="update team2 SET PID={},  Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}', Entrydate='{}' where PID={}" .format (d[0], d[1], d[2], d[3], d[4], d[5], d[6], e[0])
        cursor.execute(q)
        mycon.commit()
        q1="update team1 SET PID={}, Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}', Entrydate='{}' where PID={}". format(e[0], e[1], e[2], e[3], e[4], e[5], e[6],d[0])
        cursor.execute(q1)
        mycon.commit()
        print("\n")
        print("AFTER SWAPPING:")
    
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        print("TEAM1")
        for x in data:
            print(x)
        cursor.execute("select * from team2")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM2")
        for x in mdata:
            print(x)
    elif ch==2:
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        print("TEAM1")
        for x in data:    
            print(x)
        cursor.execute("select * from team3")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM3")
        for x in mdata:
             print(x)

        a=int(input("Enter Player Id of player you want swap from Team1:"))
        c=int(input("Enter Player Id of player you want swap from Team3:"))
        cursor.execute("select * from team1 where PID={}".format(a))
        d=cursor.fetchone()
    
        cursor.execute("select * from team3 where PID={}".format(c))
        e=cursor.fetchone()
    
        q="update team3 SET PID={}, Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}', Entrydate='{}' where PID={}" .format(d[0], d[1], d[2], d[3], d[4], d[5], d[6],e[0])
        cursor.execute(q)
        mycon.commit()

        q="update team1 SET PID={}, Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}',  Entrydate='{}' where PID={}" .format(e[0], e[1], e[2], e[3], e[4], e[5], e[6],d[0])
        cursor.execute(q)
        mycon.commit()
        print("\n")
        print("AFTER SWAPPING:")
    
        cursor.execute("select * from team1")
        data=cursor.fetchall()
        print("\n")
        print("TEAM1")
        for x in data:
            print(x)
        cursor.execute("select * from team3")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM3")
        for x in mdata:
            print(x)
    
    elif ch==3:
        cursor.execute("select * from team2")
        data=cursor.fetchall()
        print("\n")
        print("TEAM2")
        for x in data:    
            print(x)
        cursor.execute("select * from team3")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM3")
        for x in mdata:
             print(x)

        a=int(input("Enter Player Id of player you want swap from Team2:"))
        c=int(input("Enter Player Id of player you want swap from Team3:"))
        cursor.execute("select * from team2 where PID={}".format(a))
        d=cursor.fetchone()
    
        cursor.execute("select * from team3 where PID={}".format(c))
        e=cursor.fetchone()
    
        q="update team3 SET PID={}, Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}', Entrydate='{}' where PID={}". format(d[0], d[1], d[2], d[3], d[4], d[5], d[6], e[0])
        cursor.execute(q)
        mycon.commit()

        q="update team2 SET PID={}, Playername='{}', Position='{}', Goals={}, Trophies={}, Nationality='{}', Entrydate='{}' where PID={}" .format(e[0], e[1], e[2], e[3], e[4], e[5], e[6], d[0])
        cursor.execute(q)
        mycon.commit()
        print("\n")
        print("AFTER SWAPPING:")
    
        cursor.execute("select * from team2")
        data=cursor.fetchall()
        print("\n")
        print("TEAM2")
        for x in data:
            print(x)
        cursor.execute("select * from team3")
        mdata=cursor.fetchall()
        print("\n")
        print("TEAM3")
        for x in mdata:
            print(x)

menu()
########################################################

def runAgain():
    runAgn = input("\nWant To Run Again Y/N: ")
    if(runAgn.upper() == 'Y'):
        menu()
        runAgain()
runAgain() 
##########################################################    
