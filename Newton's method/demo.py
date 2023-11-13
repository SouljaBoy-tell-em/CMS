# оранжевый цвет подчеркивает области, там где выполнено достаточное условие;
# синие точки соответствуют dx > 0;
# красные точки соответствуют dx <= 0;

fig = plt.figure()
ax  = fig.add_subplot(111)

x0 = []
y0 = []
x1 = []
y1 = []
x2 = []
y2 = []

for val in x:
    
    if(ddfunc0(val) * func0(val) > 0):
        x0.append(val)
        y0.append(func0(val))
    
    if (-func0(val)/dfunc0(val) > 0):
        x1.append(val)
        y1.append(func0(val))
    else:
        x2.append(val)
        y2.append(func0(val))
        
plt.scatter(x0, y0, s = 50, c = "orange", marker = "o", 
                                label = "ddfunc0(val) * func0(val) > 0")
plt.scatter(x1, y1, s = 10, c =  "blue", marker = "o", label = "dx > 0")
plt.scatter(x2, y2, s = 10, c = "red", marker = "o", label = "dx <= 0")
plt.legend(loc='lower left')
