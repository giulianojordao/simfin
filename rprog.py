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