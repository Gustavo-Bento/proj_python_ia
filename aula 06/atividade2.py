k = [100,200,120,170,205,24,300,350,400,500]
k.sort()
f = [round(1.8*(x-273)+32,2) for x in k]
c = [round(x-273.15,2) for x in k]

print("{:<4}{:<5}{:<9}{:<8}".format("Nº","°K","°C","°F"))
print("==========================")
for v in range(0,len(k),1):
    print("{:<4}{:<5}{:<9}{:<8}".format(v+1,k[v],c[v],f[v]))