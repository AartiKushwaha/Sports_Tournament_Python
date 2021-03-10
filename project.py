import mysql.connector as ms
import matplotlib.pyplot as mp
d=ms.connect(host='localhost',user='root',password='aarti',database='Kabaddi_Masters')
c=d.cursor()
c.execute("create database if not exists Kabaddi_Masters")
c.execute("use Kabaddi_Masters;")
c.execute("create table if not exists Teams(sno int,teams char(20) primary key);")
c.execute("create table if not exists Points(sno int,teams char(20),played int,won int,lost int,tied int,total_points int, foreign key(teams) references Teams(teams) on delete cascade on update cascade);")
c.execute("create table if not exists Best_Players(sno int,name char(20),team char(20),type char(15),total_points int);")
c.execute("insert into Teams values(1,'Patna_Pirates');")
c.execute("insert into Teams values(2,'Dabang_Delhi');")
c.execute("insert into Teams values(3,'Bengaluru_Bulls');")
c.execute("insert into Teams values(4,'U-Mumba');")
c.execute("insert into Teams values(5,'Telugu_Titans');")
c.execute("insert into Points values(1,'Patna_Pirates',22,20,1,1,103);")
c.execute("insert into Points values(2,'Dabang_Delhi',22,19,2,1,98);")
c.execute("insert into Points values(3,'Bengaluru_Bulls',22,18,4,0,90);")
c.execute("insert into Points values(4,'U-Mumba',22,17,4,1,88);")
c.execute("insert into Points values(5,'Telugu_Titans',22,16,4,2,86);")
c.execute("insert into Best_Players values(1,'Pardeep_Narwal','Patna_Pirates','Raider',350);")
c.execute("insert into Best_Players values(2,'Naveen_Kumar','Dabang_Delhi','Raider',290);")
c.execute("insert into Best_Players values(3,'Pawan_Sehrawat','Bengaluru_Bulls','Raider',269);")
c.execute("insert into Best_Players values(4,'Fazal_Attrachli','U-Mumba','Defender',200);")
c.execute("insert into Best_Players values(5,'Vishal_Bhardwaj','Telugu_Titans','Defender',180);")
d.commit()
while 1:
    print("Operations to be performed are as follows :- ")
    print("Click 1 to view all the tables")
    print("Click 2 to add new records to table teams")
    print("Click 3 to add new record to points table")
    print("Click 4 to add new record to best_players table")
    print("Click 5 to update table Points")
    print("Click 6 to update table best_players")
    print("Click 7 to delete a record from teams")
    print("Click 8 to delete a record from Best_Players")
    print("Click 9 to view performance of each teams")
    print("Click 10 to view the qualified teams")
    print("Click 11 to exit")
    ch=int(input("Enter your choice :- "))
    if ch==1:
        print("The Tables are :-")
        c.execute("show tables;")
        for x in c:
            print(x)
    elif ch==2:
        print("The table Teams is:- ")
        c.execute("select * from teams;")
        for x in c:
            print(x)
        n=int(input("Enter number of records to be added :- "))
        for w in range(n):
            s=int(input("Enter serial no:- "))
            t=input("Enter team name:- ")
            k="insert into teams values({},'{}')".format(s,t)
            c.execute(k)
            d.commit()
        print("Successfully added new record !")
        print("The table now is:-")
        c.execute("select * from teams;")
        for x in c:
            print(x)
    elif ch==3:
        print("The Points Table is :-")
        c.execute("select * from points;")
        for x in c:
            print(x)
        n=int(input("How many records you want to enter? "))
        for w in range(n):
            s=int(input('Enter serial number:-'))
            t=input("Enter team name:-")
            p-int(input("Enter number of matches played:- "))
            w=int(input("Enter number of matches won:-"))
            l=int(input("Enter number of matches lost:-"))
            ti=int(input("Enter number of matches tied:-"))
            total=int(w*5+ti*3)
            k="insert into points values({},'{}',{},{},{},{},{})".format(s,t,p,w,l,ti,total)
            c.execute(k)
            d.commit()
            print("Successfully added new record !")
            print("Points table is:-")
            c.execute("select * from points;")
            for x in c:
                print(x)
    elif ch==4:
        print("The table Best_Players is:-")
        c.execute("select * from Best_Players;")
        for x in c:
            print(x)
        n=int(input("How many records you wanna add?"))
        for w in range(n):
            s=int(input("Enter serial number:- "))
            n=input("Enter name of player:- ")
            t=input("Enter team name:- ")
            ty=input("Enter whether raider or defender:- ")
            to=int(input("Enter total points:- "))
            k="insert into Best_Players values({},'{}','{}','{}',{})".format(s,n,t,ty,to)
            c.execute(k)
            d.commit()
            print("Successfully added new record !")
            print("The table now is:-")
            c.execute("select * from Best_Players;")
            for x in c:
                print(x)
    elif ch==5:
        print("The table points is:- ")
        c.execute("select * from points;")
        for x in c:
            print(x)
        n=int(input("How many records you wanna update?"))
        for w in range(n):
            t=input("Enter team name:-")
            p-int(input("Enter number of matches played:- "))
            w=int(input("Enter number of matches won:-"))
            l=int(input("Enter number of matches lost:-"))
            ti=int(input("Enter number of matches tied:-"))
            to=int(w*5+ti*3)
            k="update points set played=%s,won=%s,lost=%s,tied=%s,total_points=%s where team='%s'"%(p,w,l,ti,to,t)
            c.execute(k)
            d.commit()
            print("The records are successfully updated..")
            print("The table now is :-")
            c.execute("select * from points;")
            for x in c:
                print(x)
    elif ch==6:
        print("The table Best_Players is:- ")
        c.execute("select * from Best_Players;")
        for x in c:
            print(x)
        n=int(input("How many records you want to update?"))
        for w in range(n):
            na=input("Whose name points you want to change?")
            p=int(input("Ënter new points:- "))
            k="update Best_Players set total_points=%s where name='%s'"%(p,na)
            c.execute(k)
            d.commit()
        print("Updated the table successfully!")
        print("The table now is :-")
        c.execute("selet * from Best_Players;")
        for x in c:
            print(x)
    elif ch==7:
        print("The table Teams is:- ")
        c.execute("select * from teams;")
        for x in c:
            print(x) 
        r=int(input("Which record you want to delete (give the sno)?"))
        k="delete from teams where sno=%s"%(r,)
        c.execute(k)
        d.commit()
        print("Deleted the record")
        print("The table now is:- ")
        c.execute("select * from teams;")
        for x in c:
            print(x)
    elif ch==8:
        print("The table Best_Players is:- ")
        c.execute("select * from Best_Players;")
        for x in c:
            print(x)
        r=int(input("Enter the sno which you want to delete:-"))
        k="delete from Best_Players where sno=%s"%(r,)
        c.execute(k)
        print("Successfully deleted the record")
        print("The table Best_Players is now:- ")
        c.execute("select * from Best_Players;")
        for x in c:
            print(x)
    elif ch==9:
        c.execute("select total_points from points;")
        y=c.fetchall()
        c.execute("select team from points;")
        x=c.fetchall()
        mp.bar(x,y,color='r',width=0.5)
        mp.xlabel('Teams')
        mp.ylabel('Points')
        mp.title("Performance of Teams")
        mp.show()
    elif ch==10:
        print("The teams with a total of more than\n 80 points will be qualified")
        c.execute("select team from points where total_points>80;")
        print("Qualified teams are :-")
        for x in c:
            print(x)
    elif ch==11:
        break
    else:
        print("Ïnvalid choice")
        
            
        
        
        
        
            
            

            
            
            
                
                
                
