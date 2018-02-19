import pymysql.cursors

connection = pymysql.connect(host='iu.ct18adbzpbgv.us-east-1.rds.amazonaws.com',
                             user='scs811s',
                             password='',
                             db='pds',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

def provider_query_all():
    sql = "SELECT npi, provider_type, first_name, last_name, ssn FROM Provider WHERE NPI =%s"
    cursor.execute(sql, ('1234567890',))
    result = cursor.fetchall()
    return result

