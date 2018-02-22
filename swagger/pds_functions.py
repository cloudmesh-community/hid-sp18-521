import pymysql.cursors

connection = pymysql.connect(host='iu.ct18adbzpbgv.us-east-1.rds.amazonaws.com',
                             user='IUuser',
                             password='Password123',
                             db='pds',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

def provider_query_all():
    sql = "SELECT npi, provider_type, first_name, last_name, ssn FROM Provider"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def provider_query_npi(npi):
    sql = "SELECT npi, provider_type, first_name, last_name, ssn FROM Provider WHERE NPI =%s"
    cursor.execute(sql, (npi))
    result = cursor.fetchall()
    return result

def provider_insert(providerInsert):
    sql = "INSERT INTO Provider (npi, provider_type, first_name, last_name, ssn) VALUES (%s,%s,%s,%s,%s)"

    cursor.execute(sql, (providerInsert['npi'], providerInsert['provider_type'], providerInsert['first_name'], providerInsert
                         ['last_name'], providerInsert['ssn']))

    result = cursor.fetchall()

    return result

