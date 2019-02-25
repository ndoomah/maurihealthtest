# Title     : TODO
# Objective : TODO
# Created by: User1
# Created on: 2/24/2019

library(prophet)
library(readr)
library(ggplot2)
library(dplyr)

rpredict = function(ili,diseasename){
                #ili <- read_csv(diseasedata)


                pmod <- ili %>%
                  select(ds=1, y=2) %>%
                  prophet(daily.seasonality=TRUE)
                #> Disabling daily seasonality. Run prophet with daily.seasonality=TRUE to override this.

                future <- make_future_dataframe(pmod, periods=360)
                #tail(future)

                forecast <- predict(pmod, future)
                #tail(forecast)

                #GENERATING MAIN PREDICTION GRAPH
                p = plot(pmod, forecast, xlab="date", ylab="number of cases") + ggtitle("Forecast for",diseasename)
                ggsave(p, file=paste0(diseasename,"graph.png"))

                #GENERATING COMPONENTS GRAPH - TRENDS
                png(paste0(diseasename,file=".png"))
                prophet_plot_components(pmod, forecast)
                #ggtitle(diseasename)

                dev.off()
                #pmod.plot_components(forecast).savefig(diseasename,".png")
                #dyplot.prophet(pmod, forecast)

}
