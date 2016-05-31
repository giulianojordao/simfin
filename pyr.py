import pyRserve

conn = pyRserve.connect()


def getRStats(xvar, breaks):
    prog = """
                library(ggplot2)
                graphics.off()
                pid <- Sys.getpid()

                filename <- paste('plot_',pid,'.png',sep="")
                png(width=480, height=480, file=filename)
                we <- gsub(",", "", "%s")   # remove comma
                we <- as.numeric(we)      # turn
                %s(we);

                #print(qplot(carat, price, data = diamonds))
                plot(xvar,xvar,col="blue", xlab='xlbl', ylab = 'ylbl')
                dev.off()

                im <- readBin(filename,"raw", 999999)

                result_vector <- im

	    """
    return conn.eval(prog)

# def getRScatterPlots(xvar, yvar):
