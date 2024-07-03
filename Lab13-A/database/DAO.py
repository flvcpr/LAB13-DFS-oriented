from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select year(s.`datetime`) as y, count(*) as p
                    from sighting s 
                    group by year(s.`datetime`)"""
        cursor.execute(query)
        for row in cursor:
            result.append((row["y"], row["p"]))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getStates(y):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT s2.id, s2.Name, s2.Capital, s2.Lat, s2.Lng, s2.Area, s2.Population, s2.Neighbors
                    from sighting s , state s2 
                    where s.state = s2.id 
                    and YEAR(s.`datetime`) = %s """
        cursor.execute(query,(y,))
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArco(y,idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT s.state as s1, s2.state as s2
                    from sighting s ,sighting s2 
                    where s.`datetime` < s2.`datetime` 
                    and YEAR(s.`datetime`)=%s and YEAR(s2.`datetime` )=YEAR(s.`datetime`)"""
        cursor.execute(query, (y,))
        for row in cursor:
            result.append((idMap[row["s1"].upper()],idMap[row["s2"].upper()]))
        cursor.close()
        conn.close()
        return result
