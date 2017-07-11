import MySQLdb

CONFIG={
    'host': '192.168.0.47',
    'port': 3406,
    'user': 'root',
    'passwd':'root',
    'charset': 'utf8'}

def main():
    
    print "*"*100
    for key in CONFIG.keys():
        print key,": ",CONFIG[key]
    print "*"*100
    index_from = 1 # show seq of records
    databases = {}

    conn = MySQLdb.connect(host=CONFIG['host'], port=CONFIG['port'], user=CONFIG['user'], passwd=CONFIG['passwd'], charset=CONFIG['charset'])
    curs = conn.cursor()

    # get data
    sql = '''show databases'''
    curs.execute(sql)
    db_results = curs.fetchall()
    for record in db_results:
        db = record[0]
        databases[db] = {}   
        sql = '''use {database}'''.format(database=db)
        curs.execute(sql)
        sql = '''show tables'''
        curs.execute(sql)
        tb_results = curs.fetchall()
        for row in tb_results:
            tb = row[0]
            databases[db][tb] = []
            sql = '''desc {table}'''.format(table=tb)
            curs.execute(sql)
            desc_results = curs.fetchall()
            for desc in desc_results:
                databases[db][tb].append(desc)


    # show data
    print len(databases.keys()), " databases"
    for db in databases.keys():
        print "",db, " total", len(databases[db].keys()), "tables "
        for tb in databases[db].keys():
            print "    ", db," : ",tb, " total", len(databases[db][tb])," columns"
            idx = index_from
            for record in databases[db][tb]:
                print "        ",idx ,record
                idx = idx + 1
            print "\n"

if __name__ == '__main__':
    main()
