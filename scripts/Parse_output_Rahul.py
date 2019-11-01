
raw_input = "raw-input-output.txt"
f=open(raw_input,"r")

out_file = "out.txt"
w_f = open(out_file,'w+')

line = "Time,Tair_min,Tair_mean,Tair_max,Tfuel_min,Tfuel_mean,Tfuel_max,rhoAir_min,rhoAir_mean,rhoAir_max,rhoFuel_min,rhoFuel_mean,rhoFuel_max,muAir_min,muAir_mean,muAir_max,muFuel_min,muFuel_mean,muFuel_max,nuAir_min,nuAir_mean,nuAir_max,nuFuel_min,nuFuel_mean,nuFuel_max,kAir_min,kAir_mean,kAir_max,kFuel_min,kFuel_mean,kFuel_max,layer_no,sumVolume,Nern_min,Nern_max,ibar0,ibar,V,stack_Voltage,min_curr,mean_curr,max_curr,Energy_Ir,Energy_Fr,Energy_t_min,Energy_t_mean,Energy_t_max"
w_f.writelines(line)
#w_f.writelines("\n")
s=[]
for i in f:
    if "ExecutionTime =" in i:
        w_f.writelines("\n")
        w_f.write(str(s).rstrip("\n"))
        s=[]
    if "Time =" in i  and "ExecutionTime =" not in i:
        c=i.split(" ")
        s.append(str(c[2].rstrip("\n")))
    if "Tair min mean max  =" in i:
        c=i.split(" ")
        s.append(str(c[6]))
        s.append(str(c[10]))
        s.append(str(c[14].rstrip("\n")))
    if "Tfuel min mean max =" in i:
        c=i.split(" ")
        s.append(str(c[5]))
        s.append(str(c[9]))
        s.append(str(c[13].rstrip("\n")))
    if "min,mean,max(rhoAir):" in i:
        c=i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(rhoFuel):" in  i:
        c=i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(muAir):" in i:
        c=i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(muFuel):" in i:
        c=i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(nuAir):" in i:
        c = i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(nuFuel):" in i:
        c = i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(kAir):" in i:
        c = i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
    if "min,mean,max(kFuel):" in i:
        c = i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[4]))
        s.append(str(c[7].rstrip("\n")))
##Solve Current values##
    if "sumVolume" in i:
        c=i.split("sumVolume")
        s.append(str(c[1]).rstrip("\n"))
    if "min,max(Nernst):" in i:
        c=i.split(" ")
        s.append(str(c[1]))
        s.append(str(c[3]).rstrip("\n"))
    if "V =" in i:
        c=i.split(" ")
        s.append(str(c[2]))
        s.append(str(c[8]))
        s.append(str(c[14]).rstrip("\n"))
        #print(s)
##Energy values##
    if "Solving for T, Initial residual" in i:
        c=i.split(" ")
        s.append(str(c[8]))
        s.append(str(c[12]))
    if "T min mean max     =" in i:
        c=i.split(" ")
        s.append(str(c[9]))
        s.append(str(c[13]))
        s.append(str(c[17]).rstrip("\n"))

w_f.write(str(s))
f.close()