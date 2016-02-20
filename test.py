from simulation import Simulation

sum = 0
for i in range(100):
	sim = Simulation(8)
	sum += sim.run()
print("Final balance: " + str(sum))