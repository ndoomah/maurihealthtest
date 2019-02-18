# Title     : TODO
# Objective : TODO
# Created by: User1
# Created on: 2/5/2019

library(prophet)
library(readr)
library(ggplot2)
library(dplyr)

# Read in the ILI data.
ili <- read_csv("gastroenteritis.csv")
ili

ili %>%
  select(ds=date, y=disease)

pmod <- ili %>%
  select(ds=date, y=disease) %>%
  prophet()
#> Disabling daily seasonality. Run prophet with daily.seasonality=TRUE to override this.

future <- make_future_dataframe(pmod, periods=365*3)
tail(future)

forecast <- predict(pmod, future)
tail(forecast)

plot(pmod, forecast) + ggtitle("Three year forecast")

