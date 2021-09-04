import re
import psycopg2

####################################################
####################################################

con = psycopg2.connect(
    host='localhost',
    database='pipeline_db',
    user='postgres',
    password='dip008')

# Cursor
cur = con.cursor()

####################################################
####################################################


with open('log', 'r') as f:
    all_lines = f.readlines()
    date_time_lst = []
    category_lst = []
    message_lst = []

    for line in all_lines:
        p_date = r'[a-zA-Z]{1,3}\s[0-9]{1,2}\s[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}'
        date = re.findall(p_date, line)[0]
        date_time_lst.append(date)
        # print(date_time_lst, "\n")

        p_cat = r't[\s][a-zA-Z-._]+\[|t[\s][a-zA-Z-]+:'
        category = re.findall(p_cat, line)[0][2:-1]
        category_lst.append(category)
        # print(category_lst)


        p_msg = r':\s[a-zA-z.0-9()\[\]_*!@#$%^&<>\'\"\-:/,=\s]*'
        message = re.findall(p_msg, line)[0][2:]
        message_lst.append(message)
        # print(date_time, category, message)

        # Executing SQL command to insert the data
        cur.execute('insert into new_app1_destination (id,"Date_Time","Log_Category","Actual_Message") values (%s, %s, %s, %s)', (len(message_lst), date, category, message))
        con.commit()

# Closing the connection
cur.close()
con.close()