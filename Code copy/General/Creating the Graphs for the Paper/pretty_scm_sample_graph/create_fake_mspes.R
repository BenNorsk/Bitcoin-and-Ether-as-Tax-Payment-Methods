# Define the range for t
t <- 1:30

# Define the functions f1 and f2
f1 <- function(t) {
  return(t^1.2)
}

f2 <- function(t) {
  return(20^1.2 + (t - 20)^0.5)
}

# Calculate Y values
Y <- c(sapply(t[t <= 20], f1), sapply(t[t > 20], f1))

# Calculate Y* values
Y_star_B <- Y + rnorm(length(t[t <= 230]), mean = 0, sd = 1)
MSPE_B_pre <- mean((Y[t <= 20] - Y_star_B[t <= 20])^2)
MSPE_B_post <- mean((Y[t > 20] - Y_star_B[t > 20])^2)
MSPE_B_ratio <- MSPE_B_post / MSPE_B_pre

Y_star_C <- Y + rnorm(length(t[t <= 230]), mean = 0, sd = 1)
MSPE_C_pre <- mean((Y[t <= 20] - Y_star_C[t <= 20])^2)
MSPE_C_post <- mean((Y[t > 20] - Y_star_C[t > 20])^2)
MSPE_C_ratio <- MSPE_C_post / MSPE_C_pre

Y_star_D <- Y + rnorm(length(t[t <= 230]), mean = 0, sd = 1)
MSPE_D_pre <- mean((Y[t <= 20] - Y_star_D[t <= 20])^2)
MSPE_D_post <- mean((Y[t > 20] - Y_star_D[t > 20])^2)
MSPE_D_ratio <- MSPE_D_post / MSPE_D_pre


# Create the dataframe
df <- data.frame(t = t, Y = Y, Y_star_B = Y_star_B, Y_star_C = Y_star_C, Y_star_D = Y_star_D,
MSPE_B_pre = MSPE_B_pre, MSPE_B_post = MSPE_B_post, MSPE_B_ratio = MSPE_B_ratio,
MSPE_C_pre = MSPE_C_pre, MSPE_C_post = MSPE_C_post, MSPE_C_ratio = MSPE_C_ratio,
MSPE_D_pre = MSPE_D_pre, MSPE_D_post = MSPE_D_post, MSPE_D_ratio = MSPE_D_ratio)


# Save the dataframe
# write.csv(df, "example_mspes.csv")