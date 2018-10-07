datasets = read.csv('Data.csv')
##To handle NaN or Na value with ifelse and Ave and mean method
datasets$Age=ifelse(is.na(datasets$Age),
                    ave(datasets$Age,FUN = function(x) mean(x,na.rm = TRUE)),
                    datasets$Age)

datasets$Salary=ifelse(is.na(datasets$Salary),
                       ave(datasets$Salary,FUN = function(x) mean(x,na.rm = TRUE)),
                       datasets$Salary
                       )

## To encode for categorical value with factor method
datasets$Country=factor(datasets$Country,
                        levels = c('France','Spain','Germany'),
                        labels = c(0,1,2))

##install.packages('caTools')
library(caTools)
set.seed(123) ## for random_state in python
##It will always go for training state,in python,its just reverse. It will go to test set
split= sample.split(datasets$Purchased,SplitRatio = 0.8)  ## 0.8 is for training set and 0.2 is for test set
traing_set= subset(datasets,split==TRUE)  ## this is only select for Train set using subset and split==true
test_set=subset(datasets,split==FALSE)   ## this is only select for Test set using subset and split==false

##Feature Scaling
traing_set[,2:3]=scale(traing_set[,2:3])
test_set[,2:3]=scale(test_set[,2:3])

