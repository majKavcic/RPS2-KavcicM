from module import dbConfin

def getAll(param =""):
    
    try: 
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        
        cursor.close()
        mydb.close()
        return True
    
    except:
        return False
    
    finally:
        pass