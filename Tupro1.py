#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as numpy
import math
import random

    
    def buatIndiv(cromosomLength):
        indivBaru = []
        for i in range(cromosomLength):
            indivBaru.append(random.randint(0,1))
        return indivBaru
    
    def buatPopulasi(pjgcromosom, indivBaru, self):
        minimum = self.section[0]
        maximum = self.section[1]
        randomCoefficients = numpy.random.random(self.numberOfPopulationMembers)
        population = minimum + (randomCoefficients * (maximum - minimum))
        return population
    
    def cariFenotip(indiv,bX1,uX1,bx2,ux2):
        X1 = 0
        X2 = 0
        divX1 = 0
        divX2 = 0
        multiX1 = 0
        multiX2 = 0
        
        for i < range(len(indiv)):
            if i < len(indiv):
                divX1 = divX1+2**-(i+1)
                multiX1 = multiX1 + indiv[i]*(2**-(i+1))
            else:
                divX2 = divX2+2**-(i-2)
                multiX2 = multiX2+indiv[i]*(2**-(i-2))
                
                X1 = bX1 + (uX1-bX1)/divX1 * multiX1
                X2 = bX2 + (uX2-bX2)/divX2 * multiX2
                
                return X1,X2
    def mutasi(self):
        minimalPopulationX = numpy.min(self.populasiX)
        minimalPopulationY = numpy.min(self.populasiY)
        self.populasiX += minimalPopulationX * (self.probability * numpy.random.normal(0, 0.0001, len(self.populasiX)))
        self.populasiY += minimalPopulationY * (self.probability * numpy.random.normal(0, 0.0001, len(self.populasiY)))

    def fitness(populations):
        hasil= []
        a= 5
        for i in range(choromosomeLength):
            c = populations[i]
            h = f(c['x1'], c['x2'])
            fit = 1 / (h + a)
            result.append({
                'index': i,
                'h': h,
                'fit': fit
            })
        return hasil

     def get_parrent(populations, fit_res):
        sorted_fit = sorted(fit_res, key=lambda x: x['fit'], reverse=True) 
        parent1 = populations[sorted_fit[0]['index']]
        parent2 = populations[sorted_fit[1]['index']]
        return parent1, parent2
    
    def crossover(parrent):
        p1, p2 = parrent
        i = random.randint(0, 1)
        if i == 0:
            return {
            'x1': p1['x1'],
            'x2': p2['x2']
        }else:
        return {
            'x1': p2['x1'], 
            'x2': p1['x2']
        }
    
    def besstGen(self):
        functionValues = self.function(self.populasiX, self.populasiY)
        sortedIndexes = functionValues.argsort()
        amountOfBestValues = int(len(functionValues) * self.percentOfBestOnesToLive)
        bestPopulationX = self.populasiX[sortedIndexes[:amountOfBestValues]]
        bestPopulationY = self.populasiY[sortedIndexes[:amountOfBestValues]]
        return [bestPopulationX, bestPopulationY]
    
    def Minimum():
        minX = self.populasiX[minimumValueIndex]
        minY = self.populasiY[minimumValueIndex]
        return [minX, minY]
    
    def main():
        GA = buatPopolasi(6,10)
        print(*GA, sep="\n")
        indiv = [1,1,1,0,0,0]
        a, b = cariFenotip(indiv,-3,3,-2,2)
        print(a,b)
        h = crossover(0.5, 0.5)
        print(h)
        hasil = Minimum(GA, -3, 3, -2, 2)
        print(hasil)
        bility = bestGen(GA, -3, 3, -2, 2, 1)
        print(bility)
        parent_select = get_parent(GA,Minimum)

