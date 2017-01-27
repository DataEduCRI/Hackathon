2+3 # this is comment
# This is a line of comment

x = 3
x
y = 5

x+y

x = 10
x

x = c(1,2,3,5)
x

exp(0)
x^2
?exp

x[2]
pos = c(1,4)
pos
x[pos]
x
x[c(1,4)]

x > 2
x[ x > 2  ]


# 1 - Download the dataset
# 2 - Specify in which folder the dataset is located : 
# Working directory
# 3 - Reading the dataset

data1 = read.table( "data1.txt" , header = TRUE )
data1
head(data1)
summary(data1)
data1$Computer
plot( data1$Computer, data1$Investment )
plot( data1$Investment ~ data1$Computer )
plot( data1$Investment ~ data1$gender)

mean(data1$Investment)
var(data1$Investment)
# mean(data1$gender)

head(data1)
table(data1$Confidence, data1$gender)

invest_confid = data1$Investment[ data1$Confidence == "Confident" ]
# Extract the Investment of the non confident students
invest_nconfid = data1$Investment[ data1$Confidence == "Not confident"]
# Boxplot showing investment as a function of confidence
plot(data1$Investment ~ data1$Confidence)

hist(invest_confid)
hist(invest_nconfid)
shapiro.test(invest_confid)
shapiro.test(invest_nconfid)

#### Parametrical tests 
var.test(invest_confid, invest_nconfid)
t.test(invest_confid, invest_nconfid, var.equal = F)
# If same variability : 
# t.test(invest_confid, invest_nconfid, var.equal = T)


##### Non-parametrical tests
wilcox.test(invest_confid, invest_nconfid)
