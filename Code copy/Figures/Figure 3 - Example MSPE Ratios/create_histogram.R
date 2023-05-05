library(tidyverse)
library(ggplot2)
library(extrafont)
# Load necessary packages
library(ggplot2)
library(tidyr)

# import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)


# Load necessary packages
library(ggplot2)
library(tidyr)
library(dplyr)

# Load necessary packages
library(ggplot2)
library(dplyr)

# Create the data frame
data <- data.frame(
  unit = c("A", "B", "C", "D"),
  MSPE_ratio = c(80.4926035091542, 0.967632629591452, 2.54933896644426, 0.652249765881413),
  actually_treated = c(1, 0, 0, 0)
)

# Create the histogram
# Create the histogram
p_hist <- ggplot(data, aes(x = MSPE_ratio, fill = ifelse(actually_treated == 1, "Unit A", "Other Units"))) +
  geom_histogram(binwidth = 1, position = "identity", alpha = 0.5) +
  labs(x = "MSPE Ratio (R)", y = "Count") +
  scale_fill_manual(values = c("Unit A" = "#268BCC", "Other Units" = "#ff9f00"),
                    labels = c("other units", "unit A"), name = NULL) +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
                     legend.title = element_blank(), legend.text = element_text(size = 12))

# Print the histogram
print(p_hist)
# hihi
# Save the histogram
ggsave("histogram.png", width = 10, height = 6, units = "in", dpi = 400)