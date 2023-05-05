library(magrittr)
library(tidyverse)
library(dplyr)
library(augsynth)
library(glue)

# Set the language option to English
Sys.setenv(LANGUAGE = "en")

# Create a fucntion called synth_analysis that takes a canton as input
do_and_save_synth_analysis <- function(canton, data, cutoff) {
    # Do the analysis
    data %>% select(days, canton, companies, treatment, working_population, taxes) 
    asyn <- augsynth((companies ~ treatment | taxes + working_population), canton, days, data,
        progfunc = "Ridge", scm = T)
    # Save the results
    summary = summary(asyn)
    weights = as_tibble(asyn$weights, rownames = "canton")
    weights = rename(weights, weights = V1)
    print(summary)
    print(weights)
    write_csv(weights, glue("controlled_for_taxes/{canton}/{cutoff}_weights.csv"))

    # Plot the differences and save the plot
    plot(asyn, type = "diff")
}

# Read the command line arguments
args = commandArgs(trailingOnly = TRUE)
print(args)
data_path = as.character(args[2])
data = read_csv(data_path)
canton = args[1]
cutoff = as.character(args[3])

print(canton)
do_and_save_synth_analysis(canton, data, cutoff) 