kg = [0.01,0.75,0.5,1,10,20,100,50,25,200]
kg.sort()
lua = [round(x*(1.62/9.81),3)for x in kg]
mar = [round(x*(3.71/9.81),3)for x in kg]
mer = [round(x*(3.7/9.81),3)for x in kg]


print("{:<3}{:<6}{:<8}{:<8}{:<7}".format("Nº","Kg","Lua","Marte","Mercurio"))
print("=================================")
for v in range(0,len(kg),1):
    print("{:<3}{:<6}{:<8}{:<8}{:<7}".format(v+1,kg[v],lua[v],mar[v],mer[v]))
