import pyRserve
import rprog
import sql
class Analytics:
    def __init__(self,cursor):
        self.cursor = cursor

    def get_r_plot(self):
        self.cursor.execute(sql.profits)

        res = self.cursor.fetchall()
        self.arr = []
        for i in res:
            self.arr.append(float(i[0]))


        conn = pyRserve.connect()
        conn.r.xvar = self.arr
        return conn.eval(rprog.prog)
