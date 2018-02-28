import pymysql
import imp

config = imp.load_source('config', '/home/scs811s/Github/hid-sp18-521/swagger/config.py')

connection = pymysql.connect(host='iu.ct18adbzpbgv.us-east-1.rds.amazonaws.com',
                             user=config.user,
                             password=config.password,
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
    result = cursor.execute(sql, (providerInsert['npi'], providerInsert['provider_type'], providerInsert['first_name'], providerInsert
                        ['last_name'], providerInsert['ssn']))
    connection.commit()
    return result

def provider_delete(npi):
    sql = 'DELETE FROM Provider WHERE npi = %s'
    result = cursor.execute(sql, (npi))
    connection.commit()
    return result

def provider_update(npi, providerUpdate):
    sql = "UPDATE Provider SET provider_type = %s, first_name = %s, last_name = %s, ssn = %s WHERE npi = %s"
    result = cursor.execute(sql, (providerUpdate['provider_type'], providerUpdate['first_name'], providerUpdate
                        ['last_name'], providerUpdate['ssn'], npi))
    connection.commit()
    return result


