from module import dbConfig
from module.objects import DnevnikObj

def getAll():
    sql = """
    SELECT d.ID, d.DatumCas, d.visina, d.teza, d.itm FROM 'dnevnik 'd;
    """
    
    try: 
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.excute(sql)
        result = cursor.fetchall()
        rtn = []
        for r in resalt:
            obj = DnevnikObj(r[0], r[1], r[2], r[3], r[4])
            rtn.append(obj)
        return rtn
    except:
        return []
    finally:
        cursor.close()
        mydb.close()