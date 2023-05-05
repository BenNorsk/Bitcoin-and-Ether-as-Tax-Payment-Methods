library(tidyverse)
library(ggplot2)
library(extrafont)

# # Create graph
# # Define the range for t
# t <- 1:30

# # Define the functions f1 and f2
# f1 <- function(t) {
#   return(t^1.2)
# }

# f2 <- function(t) {
#   return(20^1.2 + (t - 20)^0.5)
# }

# # Calculate Y values
# Y <- c(sapply(t[t <= 20], f1), sapply(t[t > 20], f2))

# # Calculate Y* values
# Y_star_till_20 <- Y[t <= 20] + rnorm(length(t[t <= 20]), mean = 0, sd = 1)
# Y_star_after_20 <- Y_star_till_20[length(Y_star_till_20)] + (t[t > 20] - 20) + rnorm(length(t[t > 20]), mean = 0, sd = 0.5)
# Y_star <- c(Y_star_till_20, Y_star_after_20)

# # Create the dataframe
# df <- data.frame(t = t, Y = Y, Y_star = Y_star)

# # Save the dataframe
# write.csv(df, "example_scm.csv")

# # Print the dataframe
# print(df)

# Read CSV
df <- read.csv("example_scm.csv")

# import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)

# Load necessary packages
library(ggplot2)


# Create the plot
# Create the plot
p <- ggplot(df, aes(x = t)) +
 geom_line(aes(y = Y, color = "Y1")) +
 geom_line(aes(y = Y_star, color = "Y1*", linetype = "Y1*")) +
 geom_vline(xintercept = 20, linetype = "dotted", color = "black") +
 labs(x = "Time (t)", y = "Outcomes (Y1)", color = "Legend") +
 scale_color_manual(values = c("Y1" = "#268BCC", "Y1*" = "#ff9f00")) +
 scale_linetype_manual(values = c("Y1*" = "dashed"), guide = "none") +
 theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
 axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
 legend.title = element_blank(), legend.text = element_text(size = 12)) +
 annotate("text", x = 20, y = max(df$Y_star), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000") +
 geom_ribbon(aes(ymin = Y[t > 20], ymax = Y_star[t > 20]), data = df[df$t > 20, ], alpha = 0.3, fill = "darkgrey")

# Print the plot
print(p)

# Print the plot
print(p)




# ggplot(df, aes(x = month, y = companies, group = canton, color = canton)) +
#   geom_line() + 
#   scale_color_manual(values = c("#268BCC", "#56B4F1", "#ff9f00", "#ff2200",  "#bfdf6e", "#b1b1b1")) +
#   labs(x = "Year (on a monthly basis)", y = "Number of companies", color = "Canton") +
#   theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
#         axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
#          legend.title = element_text(face = "bold"), legend.text = element_text(size = 12)) + 
#   geom_vline(xintercept = as.numeric(as.Date("2021-01-31")), linetype = "dotted") +
# annotate("text", x = as.Date("2021-01-31"), y = max(df$companies), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000")


# Save the plot as png (high quality)
ggsave("example_scm.png", width = 10, height = 6, units = "in", dpi = 400)