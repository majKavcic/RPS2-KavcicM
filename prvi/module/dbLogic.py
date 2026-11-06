from module import dbConfig
from module.objects import DnevnikObj

def getAll():
    
    sql = """
    SELECT id, datumcas, visina, teza, itm FROM dnevnik;
    """.format()
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        rtn = []
        for r in result:
            obj = DnevnikObj(r[0], r[1], r[2], r[3], r[4])
            rtn.append(obj)
        return rtn
    except:
        return []
    finally:
        cursor.close()
        mydb.close()
        
def insertData(visina, teza, itm):
    
    sql = """
    INSERT INTO dnevnik (datumcas, visina, teza, itm)
    VALUES (NOW(), {}, {}, {});
    """.format(visina, teza, itm)
    vrniID = -1
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        mydb.rollback()
        return vrniID
    finally:
        cursor.close()
        mydb.close()
        
def deleteItm(id):
    
    sql = """
    DELETE FROM dnevnik 
        WHERE ID = {};
    """.format(id)
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        return True
    except:
        mydb.rollback()
        return False
    finally:
        cursor.close()
        mydb.close()