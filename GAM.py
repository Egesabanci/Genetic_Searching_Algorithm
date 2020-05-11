"""
@author : Ege Sabancı
"""

"""
STRUCTURE OF THE ALGORITHM

-> CREATE RANDOM POP
-> FITNESS FUNCTION
-> CROSSOVER
-> MUTATION
-> SELECTION
"""
import random

class GA(object):

	# create random vector
	def random_vector(self, lenght, between):
		self.lenght = lenght
		self.between = between
		vector = [random.randint(0, self.between) for _ in range(self.lenght)]
		return vector

	# fitness function
	def fitness(self, target, vector):
		self.target = target
		self.vector = vector
		fitness = 0
		for i in range(len(self.target)):
			if self.target[i] == self.vector[i]:
				fitness += 1
		return fitness

	def population_fitness(self, target, population):
		self.population = population
		self.target = target
		fitness = 0
		pop_fitness = [self.fitness(self.target, chromosome) for chromosome in self.population]
		fitness = sum(pop_fitness)
		return fitness

	# mutation - default = %10 probability
	def mutate(self, population, mutation_rate = 0.1):
		self.population = population
		self.mutation_rate = mutation_rate
		mutate = 1
		if random.uniform(0, 1) < self.mutation_rate:
			for i in range(len(self.population)):
				for a in range(len(self.population[i])):
					self.population[i][a] += mutate
					self.population[i][a] = self.population[i][a] % 2
		return self.population

	# select best vector from population
	def selection(self, target, pop):
		self.target = target
		self.pop = pop
		best_vector = self.pop[0]
		for i in range(len(self.pop)):
			if self.fitness(self.target, self.pop[i]) > self.fitness(self.target, best_vector):
				best_vector = self.pop[i]
		return best_vector 

	# crossover method
	def crossover(self, population, c_vector):
		self.population = population
		self.c_vector = c_vector
		choices = [0, 1]
		for i in range(len(self.population)):
			random_num = random.choice(choices)
			if random_num == 1:
				pop_slice = self.population[i][:int(len(self.population[i]) / 2)]
				vec_slice = self.c_vector[int(len(self.c_vector) / 2):]
				self.population[i] = pop_slice + vec_slice
			else:
				pop_slice = self.population[i][int(len(self.population[i]) / 2):]
				vec_slice = self.c_vector[:int(len(self.c_vector) / 2)]
				self.population[i] = pop_slice + vec_slice
		return self.population
