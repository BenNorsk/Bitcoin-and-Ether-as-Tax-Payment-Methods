library(magrittr)
library(dplyr)
library(augsynth)
data(kansas)

# Set the language option to English
Sys.setenv(LANGUAGE = "en")

kansas %>% 
  select(year, qtr, year_qtr, state, treated, gdp, lngdpcapita) %>% 
  filter(state == "Kansas" & year_qtr >= 2012 & year_qtr < 2013) 
#> # A tibble: 4 x 7
#>    year   qtr year_qtr state  treated    gdp lngdpcapita
#>   <dbl> <dbl>    <dbl> <chr>    <dbl>  <dbl>       <dbl>
#> 1  2012     1    2012  Kansas       0 143844        10.8
#> 2  2012     2    2012. Kansas       1 141518        10.8
#> 3  2012     3    2012. Kansas       1 138890        10.8
#> 4  2012     4    2013. Kansas       1 139603        10.8

syn <- augsynth(lngdpcapita ~ treated, fips, year_qtr, kansas,
                progfunc = "None", scm = T)


summary(syn)
#> 
#> Call:
#> single_augsynth(form = form, unit = !!enquo(unit), time = !!enquo(time), 
#>     t_int = t_int, data = data, progfunc = "None", scm = ..2)
#> 
#> Average ATT Estimate (p Value for Joint Null):  -0.029   ( 0.328 )
#> L2 Imbalance: 0.083
#> Percent improvement from uniform weights: 79.5%
#> 
#> Avg Estimated Bias: NA
#> 
#> Inference type: Conformal inference
#> 
#>     Time Estimate 95% CI Lower Bound 95% CI Upper Bound p Value
#>  2012.25   -0.018             -0.045              0.006   0.111
#>  2012.50   -0.041             -0.070             -0.015   0.022
#>  2012.75   -0.033             -0.062             -0.007   0.044
#>  2013.00   -0.019             -0.046              0.005   0.111
#>  2013.25   -0.029             -0.053             -0.005   0.044
#>  2013.50   -0.046             -0.073             -0.022   0.022
#>  2013.75   -0.032             -0.056             -0.010   0.022
#>  2014.00   -0.045             -0.074             -0.018   0.022
#>  2014.25   -0.043             -0.074             -0.014   0.022
#>  2014.50   -0.029             -0.061              0.000   0.044
#>  2014.75   -0.018             -0.053              0.011   0.144
#>  2015.00   -0.029             -0.066              0.005   0.078
#>  2015.25   -0.019             -0.051              0.010   0.122
#>  2015.50   -0.022             -0.056              0.007   0.111
#>  2015.75   -0.019             -0.055              0.013   0.189
#>  2016.00   -0.028             -0.067              0.008   0.100