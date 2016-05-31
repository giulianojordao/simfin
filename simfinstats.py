import pyRserve
import pyhdb
from bottle import get, post, request, response, run  # or route


@get('/login')  # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Hostname: <input name="hostname" type="text" />
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')  # or @route('/login', method='POST')
def do_login():
    response.content_type = 'image/jpeg'

    username = request.forms.get('username')
    password = request.forms.get('password')
    hostname = request.forms.get('hostname')

    connection = pyhdb.connect(
        host=hostname,
        port=30015,
        user=username,
        password=password
    )

    cursor = connection.cursor()
    cursor.execute("""

            SELECT SUM(ACDOCA."HPEINH") AS TOTAL_PRICE  FROM "SAPE1D"."ACDOCA" ACDOCA  INNER JOIN "SAPE1D"."KNA1" KNA1
            ON KNA1."KUNNR" = ACDOCA."KUNNR"

            GROUP BY KNA1."NAME1"
            ORDER BY TOTAL_PRICE DESC

        """)

    res = cursor.fetchall()

    connection.close(),

    conn = pyRserve.connect()
    arr = []

    for i in res:
        arr.append(float(i[0]))
    print(arr)

    conn.r.xvar = arr

    prog = """
                    library(ggplot2)
                    graphics.off()
                    pid <- Sys.getpid()

                    filename <- paste('plot_',pid,'.png',sep="")
                    png(width=480, height=480, file=filename)

                    # print(qplot(carat, price, data = diamonds))
                    plot(xvar,xvar,col="blue", xlab='HPEINH', ylab = 'ylbl')
                    dev.off()

                    im <- readBin(filename,"raw", 999999)

                    result_vector <- im

                """
    bmp = conn.eval(prog)

    return bmp

run(host='localhost', port=8080, debug=True, reloader=True)
