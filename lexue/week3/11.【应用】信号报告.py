t = int(input())
a = t // 10
b = t % 10
x = {1 : "Unreadable", 2 : "Barely readable, occasional words distinguishable",
     3:"Readable with considerable difficulty" , 4:"Readable with practically no difficulty",5:"Perfectly readable"}
y = {1:"Faint signals, barely perceptible",
     2:"Very weak signals",
     3:"Weak signals",
     4:"Fair signals",
     5:"Fairly good signals",
     6:"Good signals",
     7:"Moderately strong signals",
     8:"Strong signals",
     9:"Extremely strong signals"}
print(x[a] + "," + y[b])