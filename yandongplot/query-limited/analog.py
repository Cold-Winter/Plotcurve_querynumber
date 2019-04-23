iterlist = []
for line in open('ql_therm_adv.log'):
	if 'early stopping at iteration' in line:
		iternum = int(line.split()[-1])
		iterlist.append(iternum)
print(iterlist)
