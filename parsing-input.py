import os

raw_input = "/home/ad26/OpenFOAM/openfuelcell/run/quickTest/raw-input-output.txt"

out_file = "/home/ad26/Projects/Fall-19/EECS-245/OpenFuelCell/parsed-input1.txt"

w_f = open(out_file,'w')

line = "Tair_min,Tair_mean,Tair_max,Tfuel_min,Tfuel_mean,Tfuel_max,rhoAir_min,rhoAir_mean,rhoAir_max,rhoFuel_min,rhoFuel_mean,rhoFuel_max,muAir_min,muAir_mean,muAir_max,muFuel_min,muFuel_mean,muFuel_max,nuAir_min,nuAir_mean,nuAir_max,nuFuel_min,nuFuel_mean,nuFuel_max,kAir_min,kAir_mean,kAir_max,kFuel_min,kFuel_mean,kFuel_max,fuel_flow_ir_Ux,fuel_flow_fr_Ux,fuel_flow_ir_Uy,fuel_flow_fr_Uy,fuel_flow_ir_Uz,fuel_flow_fr_Uz,fuel_flow_ir_p,fuel_flow_fr_p,air_flow_ir_Ux,air_flow_fr_Ux,air_flow_ir_Uy,air_flow_fr_Uy,air_flow_ir_Uz,air_flow_fr_Uz,air_flow_ir_p,air_flow_fr_p,energy_ir_T,energy_fr_T,T_min,T_mean,T_max"
w_f.writelines(line)

count_steps = 0
for line in open(raw_input,'r').readlines():

	Tair_min = 0.0
	Tair_mean = 0.0
	Tair_max = 0.0
	Tfuel_min = 0.0
	Tfuel_mean = 0.0
	Tfuel_max = 0.0
	rhoAir_min = 0.0
	rhoAir_mean = 0.0
	rhoAir_max = 0.0
	rhoFuel_min = 0.0
	rhoFuel_mean = 0.0
	rhoFuel_max = 0.0
	muAir_min = 0.0
	muAir_mean = 0.0
	muAir_max = 0.0
	muFuel_min = 0.0
	muFuel_mean = 0.0
	muFuel_max = 0.0
	nuAir_min = 0.0
	nuAir_mean = 0.0
	nuAir_max = 0.0
	nuFuel_min 0.0 
	nuFuel_mean = 0.0
	nuFuel_max = 0.0
	kAir_min = 0.0
	kAir_mean = 0.0
	kAir_max = 0.0
	kFuel_min = 0.0
	kFuel_mean = 0.0
	kFuel_max = 0.0
	fuel_flow_ir_Ux = 0.0
	fuel_flow_fr_Ux = 0.0
	fuel_flow_ir_Uy = 0.0
	fuel_flow_fr_Uy = 0.0
	fuel_flow_ir_Uz = 0.0
	fuel_flow_fr_Uz = 0.0
	fuel_flow_ir_p = 0.0
	fuel_flow_fr_p = 0.0
	air_flow_ir_Ux = 0.0
	air_flow_fr_Ux = 0.0
	air_flow_ir_Uy = 0.0
	air_flow_fr_Uy = 0.0
	air_flow_ir_Uz = 0.0
	air_flow_fr_Uz = 0.0
	air_flow_ir_p = 0.0
	air_flow_fr_p = 0.0
	energy_ir_T = 0.0
	energy_fr_T = 0.0
	T_min = 0.0
	T_mean = 0.0
	T_max = 0

	if "Time = " in line and "ExecutionTime = " not in line:
		w_f.writelines("\n\n")
		w_f.writelines(line)
	if "Tair min mean max  =" in line:
		w_f.writelines(line)
	if "Tfuel min mean max =" in line:
		w_f.writelines(line)
	if "min,mean,max(rhoAir):" in line:
		w_f.writelines(line)
	if "min,mean,max(rhoFuel):" in line:
		w_f.writelines(line)
	if "min,mean,max(muAir):" in line:
		w_f.writelines(line)
	if "min,mean,max(muFuel):" in line:
		w_f.writelines(line)
	if "min,mean,max(nuAir):" in line:
		w_f.writelines(line)
	if "min,mean,max(nuFuel):" in line:
		w_f.writelines(line)
	if "min,mean,max(kAir):" in line:
		w_f.writelines(line)
	if "min,mean,max(kFuel):" in line:
		w_f.writelines(line)
	if "Solving fuel flow" in line:
		w_f.writelines(line)
	if "Solving for Ux, Initial" in line:
		w_f.writelines(line)
	if "Solving for Uy, Initial" in line:
		w_f.writelines(line)
	if "Solving for Uz, Initial" in line:
		w_f.writelines(line)
	if "Solving for p, Initial" in line:
		w_f.writelines(line)
	if "Solving air flow" in line:
		w_f.writelines(line)
	if "Solving for T, Initial" in line:
		w_f.writelines(line)
	if "T min mean max     =" in line:
		w_f.writelines(line)

print(count_steps)