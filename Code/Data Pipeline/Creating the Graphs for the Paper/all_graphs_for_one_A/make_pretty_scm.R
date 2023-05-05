library(tidyverse)
library(ggplot2)
library(extrafont)

fix_synth_date <- function(df) {
  # For every column where canton is synth_ZG, replace the month with the month of the previous row
    for (i in 1:nrow(df)) {
        if (df[i, "canton"] == "synth_ZG") {
        df[i, "month"] <- df[i - 1, "month"]
        }
    }
    return(df)
}

# read the CSV data into a data frame
df <- read.csv("0_synth_ZG.csv")

# Select only the month, days, canton, companies and treatment columns
df <- df[, c("month", "canton", "companies", "days")]

# Select only the rows where the canton is ZG or synth_ZG
df <- filter(df, canton == "ZG" | canton == "synth_ZG")

df <- fix_synth_date(df)

# convert the "month" column to a date format
df$month <- as.Date(df$month)
print(head(df))
# define the order of the cantons
canton_order <- c("ZG", "synth_ZG")
# convert the "canton" column to a factor with the specified order
df$canton <- factor(df$canton, levels = canton_order)

# Now, reshape, that the canton disappears, and instead, there is a Y column for all companies where canton = ZG and Y_star for canton = synth_ZG
df <- df %>%
  spread(key = canton, value = companies)

# Rename the columns
colnames(df) <- c("month", "days", "Y", "Y_star")
df$month <- as.Date(df$month)

print(head(df))
# import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)

# save the df
write.csv(df, "formatted_0_ZG_df.csv", row.names = FALSE)




# # register the "sourcesanspro" font
# loadfonts()


p <- ggplot(df, aes(x = month)) +
 geom_line(aes(y = Y, color = "ZG")) +
 geom_line(aes(y = Y_star, color = "synth. ZG", linetype = "Y1*")) +
 labs(x = "Year (on a monthly basis)", y = "Number of companies (Y)", color = "Canton") +
 scale_color_manual(values = c("ZG" = "#268BCC", "synth. ZG" = "#ff9f00")) +
 scale_linetype_manual(values = c("Y1*" = "dashed"), guide = "none") +
 theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
 axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
 legend.title = element_text(size = 12, face = "bold"), legend.text = element_text(size = 12)) +
 annotate("text", x = as.Date("2021-01-31"), y = max(df$Y_star), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000") +
 geom_ribbon(data = df[df$month > as.Date("2020-12-31"), ], aes(ymin = Y, ymax = Y_star), alpha = 0.3, fill = "darkgrey") +
 geom_vline(xintercept = as.numeric(as.Date("2021-01-31")), linetype = "dotted")

# Save the plot as png (high quality)
# ggsave("no_control_companies.png", width = 10, height = 6, units = "in", dpi = 400)

