import matplotlib.pyplot as plot


month =['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

rainFalls =[120,30,40,50,60,100,30,80,90,100,70,98]


plot.bar(month,rainFalls, color='blue')

plot.title("monthly rain fall bar")

plot.xlabel('month')
plot.ylabel('rainfalls')
plot.show()

