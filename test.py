from simulation import Simulation

f = open("data.dat", 'w')
sum_balance = 0
min_balance = 0
min_running_balance = 0
for i in range(1000):
	sim = Simulation(8)
	res = sim.run()
	sum_balance += res
	min_balance = min(min_balance, res)
	min_running_balance = min(min_running_balance, sum_balance)
	f.write(str(res) + "\n")

print("Final balance: " + str(sum_balance))
#print("Min running balance: " + str(min_running_balance))
#print("Min balance: " + str(min_balance))