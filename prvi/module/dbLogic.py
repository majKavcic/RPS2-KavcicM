from module import dbConfig
from module.objects import DnevnikObj

def getAll():
    sql = """
        SELECT d.ID, d.DatumCas, d.visina, d.teza, d.itm
        FROM dnevnik AS d
    """

    mydb = None
    cursor = None

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

    except Exception as e:
        print("Napaka pri pridobivanju dnevnika:", e)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if mydb is not None:
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