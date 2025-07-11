library(tidyverse)
library(readr)
library(ggplot2)
library(dplyr)
library(car)
library(caret)
library(mice)
library(rms)
library(reshape2)
data <- read.csv("/Users/apple/Desktop/tikko 302/indian_liver_patient.csv")

# data over view
str(data)
summary(data)

# finding the missing value
sum(is.na(data))
colSums(is.na(data))
clean_data <- na.omit(data)

# draw the protein levels distribution
ggplot(clean_data, aes(x=Total_Protiens)) + 
  geom_histogram(aes(y=after_stat(density)), binwidth=0.1, fill="lightblue", color="blue") +
  geom_density(alpha=.2, fill="blue") +
  labs(title="Distribution of protein levels", x="protein levels", y="Frequency")

#draw the heat map
cor_matrix <- cor(clean_data[, sapply(clean_data, is.numeric)])

cor_melted <- melt(cor_matrix)

ggplot(data = cor_melted, aes(x=Var1, y=Var2, fill=value)) +
  geom_tile() + 
  scale_fill_gradient2(low="red", high="blue", mid="lightyellow", 
                       midpoint=0, limit=c(-1,1), space="Lab", 
                       name="Pearson\nCorrelation") +
  theme_minimal() + 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 10, hjust = 1),
        axis.text.y = element_text(size = 10)) +
  labs(title = "Correlation Matrix", x = "", y = "") +
  coord_fixed()

#create the original linear regression model
origin_model <- lm(Total_Protiens ~ ., data = clean_data)
summary(origin_model)

# DEBETA original model
# condition 1
par(mfrow=c(3, 2))
plot(origin_model)

# condition 2
qqPlot(origin_model, main="QQ Plot")

# condition 1
par(mfrow=c(3, 2))
plot(origin_model)

# condition 2
qqPlot(origin_model, main="QQ Plot")

# vif
vif(origin_model)

# Stepwise regression method of model selection
step_model <- step(origin_model, direction = "both")
summary(step_model)

vif(step_model)

# Check the residual plots of the simplified model
par(mfrow=c(2, 2))
plot(step_model)

cat("Full Model: Adjusted R^2 = ", summary(origin_model)$adj.r.squared, "\n")
cat("Reduced Model: Adjusted R^2 = ", summary(step_model)$adj.r.squared, "\n")
cat("Full Model: AIC = ", AIC(origin_model), "\n")
cat("Reduced Model: AIC = ", AIC(step_model), "\n")
cat("Full Model: BIC = ", BIC(origin_model), "\n")
cat("Reduced Model: BIC = ", BIC(step_model), "\n")

test_predictions <- predict(step_model, newdata = clean_data)
mse <- mean((test_predictions - clean_data$Total_Protiens)^2)
cat("Mean Squared Error on Test Set: ", mse, "\n")