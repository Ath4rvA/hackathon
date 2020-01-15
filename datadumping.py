import mysql.connector
import csv
con = mysql.connector.connect(user = 'dbda', password= 'dbda', host='localhost', database = 'hackathon')
cur = con.cursor()
print("DataBase Connected")

csv_data = csv.reader(open("/home/atharva/Documents/hackathon/hackathon/Cricket-Dataset/matches.csv"))

"""
for row in csv_data:
    cur.execute('INSERT INTO deliveries (MATCH_ID, INNING, BATTING_TEAM, BOWLING_TEAM, OVER, BALL, BATSMAN, BOWLER, WIDE_RUNS, BYE_RUNS, LEGBYE_RUNS, NOBALL_RUNS, PENALTY_RUNS, BATSMAN_RUNS, EXTRA_RUNS, TOTAL_RUNS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s', row)
"""
counter=0
for row in csv_data:
    if counter==0:
        counter+=1
        continue
    date= row[3] 
    month,day,year= date.split('/') 
    new_date= year+'/'+month+'/'+day 
    row[3]= new_date 

    cur.execute('insert into matches (MATCH_ID, SEASON, CITY, DATE, TEAM1, TEAM2, TOSS_WINNER, TOSS_DECISION, RESULT, WINNER) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

con.commit()

cur.close()


cur = con.cursor()
csv_deliv = csv.reader(open("/home/atharva/Documents/hackathon/hackathon/Cricket-Dataset/deliveries.csv"))
counter=0
for row in csv_deliv:
    if counter==0:
        counter+=1 
        continue
    query='''INSERT INTO deliveries (MATCH_ID, INNING, BATTING_TEAM, 
                BOWLING_TEAM, `OVER`, BALL, 
                BATSMAN, BOWLER, WIDE_RUNS, BYE_RUNS, LEGBYE_RUNS, NOBALL_RUNS, 
                PENALTY_RUNS, BATSMAN_RUNS, EXTRA_RUNS, TOTAL_RUNS) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s)'''
    cur.execute(query, row)

con.commit()
cur.close()
print("Done")