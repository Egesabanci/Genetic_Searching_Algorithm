# Main Algorithm Implementation with GAM.py file

import random
from GAM import GA #genetic algorithm module from GAM.py
ins = GA() #instance from GA module

# PARAMETERS
BETWEEN = 5
NUM_OF_INDEX = 10
NUM_OF_CHROMOSOME_PER_POP = 50
POPULATION = [ins.random_vector(NUM_OF_INDEX, BETWEEN) for _ in range(NUM_OF_CHROMOSOME_PER_POP)]
BESTS = []

# TARGET VECTOR
TARGET = ins.random_vector(NUM_OF_INDEX, BETWEEN)

iteration = 0
while True:
	# if the target vector is in the population
	if TARGET in POPULATION:
		print(f'\nVECTOR HAS BEEN FOUND! --- ITERATION = {iteration + 1}')
		print(f'TARGET : {TARGET}')
		print(f'POPULATION : {POPULATION}')
		break

	# Create new population
	POPULATION = [ins.random_vector(NUM_OF_INDEX, BETWEEN) for _ in range(NUM_OF_CHROMOSOME_PER_POP - len(BESTS))]
	POPULATION = POPULATION + BESTS
	if len(BESTS) == int((NUM_OF_CHROMOSOME_PER_POP - (NUM_OF_CHROMOSOME_PER_POP / 2) - 1)):
		BESTS.remove(BESTS[0])

	# iterations
	print(f'\nITERATION {iteration + 1} --------')
	fitness = [ins.fitness(TARGET, a) for a in POPULATION]
	pop_fit = ins.population_fitness(TARGET, POPULATION)
	print(f'FITNESS OF THE ITERATION {iteration + 1}: {fitness}')
	print(f'POPULATION FITNESS OF THE ITERATION {iteration + 1}: {pop_fit}')
	
	# Get the best chromosome from population
	BEST_CHROMOSOME = ins.selection(TARGET, POPULATION)
	BESTS.append(BEST_CHROMOSOME)

	# Crossover the vectors
	POPULATION = ins.crossover(POPULATION, BEST_CHROMOSOME)

	# Mutate the chromosome - probability = %1
	POPULATION = ins.mutate(POPULATION, mutation_rate = 0.01)
	iteration += 1
