2+2 # This is a comment
# this is a line of comment

#Start by creating objects
x=3 #x is the object, need to send to console to validate it [CTRL+Enter]. CASE SENSITIVE. Can contain entire dataset
x
y=5
x+y
x = c(1,2,3,5) #Vector or array 1-D; function "c" is "combine". Between paranthhes are arguments.
x
x[4] #extract memeber of array; first element is 1 not 0
x[c(1,4)] #extract several members of array (vector)
x > 2 #Tests each member of the array; returns true or false. In this example, FALSE FALSE  TRUE  TRUE
x[x>2]n #Returns only members whose value is sup à 2

#Import dataset##########################################

# 1 - Download dataset
# 2 - Session-Set working directory-Choose directory
# 3 - Reading the dataset with command "read.table"

data1=read.table("data1.txt" , header = TRUE)
data1
head(data1) #First 6 lines only
summary(data1) #summary of data with basic info
data1$Investment #Get column by name (Dollar sign indicates column)

#######################################################
# Graph data
plot(data1$Investment ~ data1$Computer, xlab = "Computing Power") # simple visualization with new tag name in X
plot(data1$Investment ~ data1$gender)
hist(data1$Computer)
table(data1$Confidence, data1$gender)

#######################################################
#Try to answer real questions
#select invest for confident and invest for non-conf; does invest and confidence correlate?
invest_conf = data1$Investment[ data1$Confidence == "Confident" ] #double equality means equal to. Want to select only lines where confidence is true
hist(invest_conf)

invest_nonconf = data1$Investment[data1$Confidence == "Not confident"]
hist(invest_nonconf)

#Use preliminary tests to check data to see if strong tests are poss
#Shapiro test for gaussien (normal) distribution
shapiro.test(invest_conf)
shapiro.test(invest_nonconf)

#Variance test (degree of spread)
var.test(invest_conf, invest_nonconf)

#gaussien shapiro test ok
#Variance test fails but still can do paratetrical test

#Then parametrical tests
t.test(invest_conf, invest_nonconf) #Default: variance not the same
#Conclusion (faible p-val) therefore investment related to confidence and non-confidence

# graph
plot(data1$Investment ~ data1$Confidence)

#If same variability (spread)
#t.test(invest_conf, invest_nonconf, var.equal = TRUE)

#Non parametrical test : compare two data sets when not following gaussien distribution
#Can always use but less powerful than T test
wilcox.test(invest_conf, invest_nonconf)

#To Do : test gender instead of confidence
#Bring in perso dataset
#yann.lecunff@gmail.com
