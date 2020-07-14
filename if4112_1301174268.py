#Add library
from numpy.random import seed
from numpy.random import randint
from random import random

def decode(code):
  arrCode = code.split(" ");
  print(arrCode);
  rule = [0]*15;

  if(arrCode[0] == "Rendah"):
    rule[0] = 1;
  elif(arrCode[0] == "Normal"):
    rule[1] = 1;
  elif(arrCode[0] == "Tinggi"):
    rule[2] = 1; 
		
  if(arrCode[1] == "Pagi"):
    rule[3] = 1;
  elif(arrCode[1] == "Siang"):
    rule[4] = 1;

  elif(arrCode[1] == "Sore"):
    rule[5] = 1;
  elif(arrCode[1] == "Malam"):
    rule[6] = 1;
		
		
  if(arrCode[2] == "Berawan"):
    rule[7] = 1;
  elif(arrCode[2] == "Rintik"):
    rule[8] = 1;
  elif(arrCode[2] == "Hujan"):
    rule[9] = 1;
  elif(arrCode[2] == "Cerah"):
    rule[10] = 1;
		
  if(arrCode[3] == "Rendah"):
    rule[11] = 1;
  elif(arrCode[3] == "Normal"):
    rule[12] = 1;
  elif(arrCode[3] == "Tinggi"):
    rule[13] = 1;
		
	
  if(arrCode[4] == "Ya"):
    rule[14] = 1;
  else:
    rule[14] = 0;
  print(rule);
  return rule;

def loadData(fileName):
  f = open(fileName, "r");
  i = 0;
  dataTest = [];
  line = f.readline();
  while( line != ""):
    i = i + 1;
    line = line.replace("\n", "")
    print(i , line);
    dataTest.append(decode(line));
    line = f.readline();
  f.close();
  return dataTest;


def gen_population(count):
  populations = []
  for i in range(count);
    chromosome = []
    for b in range(bit_count);
      chromosome.append(random.randint(0,1));
    populations.append(chromosome);
  return populations;

def getResult(chromosome , data):
  ruleCount = len(chromosome)/15;
  elseAnswer = int(chromosome[len(chromosome)-1] == 0);
  valid = False;
  rule = 0;
  while(valid==False):
    if(rule >= ruleCount):
      break;
    crPos = rule*15;
    sesi = data[0] and chromosome[crPos + 0];
    sesi = sesi or (data[1] and chromosome[crPos + 1]);
    sesi = sesi or (data[2] and chromosome[crPos + 2]);
    if(sesi==0):
      rule = rule + 1;
      continue;
    sesi = data[3] and chromosome[crPos + 3];
    sesi = sesi or (data[4] and chromosome[crPos + 4]);
    sesi = sesi or (data[5] and chromosome[crPos + 5]);
    sesi = sesi or (data[6] and chromosome[crPos + 6]);
    if(sesi==0):
      rule = rule + 1;
      continue;
    sesi = data[7] and chromosome[crPos + 7];
    sesi = sesi or (data[8] and chromosome[crPos + 8]);
    sesi = sesi or (data[9] and chromosome[crPos + 9]);
    sesi = sesi or (data[10] and chromosome[crPos + 10]);
    if(sesi==0):
      rule = rule + 1;
      continue; 
    sesi = data[11] and chromosome[crPos + 11];
    sesi = sesi or (data[12] and chromosome[crPos + 12]);
    sesi = sesi or (data[13] and chromosome[crPos + 13]);
    if(sesi==0):
      rule = rule + 1;
      continue;
    valid = true;


  if(valid):
    return chromosome[(rule*15) + 14];
  else:

    return elseAnswer;

def getFitnessValue(chromosome):
  correct = 0;
 
 
  for i in range( 0 , len(dataTest)): 
    resultAnser = getResult(chromosome , dataTest[i]);
    
    if(resultAnser == dataTest[i][14]):
      correct = correct + 1;
  
  return correct/(len(dataTest)*1.0);

def get_parrent(populations, fit_res):
  sorted_fit = sorted(fit_res, key=lambda x: x['fit'], reverse=True): 
  parent1 = populations[sorted_fit[0]['index']];
  parent2 = populations[sorted_fit[1]['index']];
  return parent1, parent2;
  
def getRandom2Point(chromosome):
  a=0;
  b=0;
  while(a==b):
    a = randint(0,len(chromosome.gen));
    b = randint(0,len(chromosome.gen));

  if(a>b):
    return [b,a];
  else:
    return [a,b];

def convertPointToArea(Point,rangeMin):
  ruleAt = Point//15;
  pos = Point%15;
  if(pos < 3 and rangeMin>=3):
    return [ruleAt*15+0 , ruleAt*15+2];
  elif(pos <7 and rangeMin>=4):
    return [ruleAt*15+3 , ruleAt*15+6];
  elif(pos < 11 and rangeMin>=4):
    return [ruleAt*15+7 , ruleAt*15+10];
  elif(pos < 14 and rangeMin>=3):
    return [ruleAt*15+11 , ruleAt*15+13];
  elif(pos == 14 and rangeMin>=1):
    return [ruleAt*15+14 , ruleAt*15+14];
  else:
    return None;

def getOtherPoint(Points):
  other = [];
  other.append(Points);
  rangeMin = Points[1]-Points[0]+1;
  a = convertPointToArea(Points[0],rangeMin);
  if(a!= None):
    other.append(a);
  a = convertPointToArea(Points[1],rangeMin);
  if(a!= None):
    other.append(a);
  return other;

def crossTypeA(parentA , parentB , pointA , pointB):
  child = []
  maximum = (pointB[0]) + (pointA[1]-pointA[0]+1)+(len(parentB) - 1 - pointB[1]);
  print(maximum);
  maximum = maximum - (maximum%15);
  
  for i in range(0,pointB[0]):
    print("B",i)
    child.append(parentB[i]);
    maximum -= 1;
    if(maximum==0):
      print(1 , len(child));  
      return child;

  for i in range(pointA[0],pointA[1]+1):
    print("A",i)
    child.append(parentA[i]);
    maximum -= 1;
    if(maximum==0):
      print(2 , len(child));
      return child;
  
  for i in range(pointB[1]+1,len(parentB)):
    print("B",i)
    child.append(parentB[i]);
    maximum -= 1;
    if(maximum==0):
      print(3 , len(child));
      return child;
  
  print(4 , len(child));
  return child;

def crossTypeB(parentA , parentB , pointB):
  i=0;
  child = [];
  while(i < len(parentB)):
    if(diantara(pointB , i)):
      child.append(parentB[i]);
    else:
      child.append(parentA[i]);
    i = i+ 1;
  return child;


def diantara(points , point):
  return point >= points[0] and point <= points[1];

def crossover(parentA , parentB , pointA , otherPoint):
  pointB = otherPoint[randint(0,len(otherPoint))];
  if(len(parentA) < len(parentB)):
    temp = parentB;
    parentB = parentA;
    parentA = temp;
  print(pointA , pointB)
  childA = crossTypeA(parentB  ,parentA , pointA , pointB);
  childB = crossTypeB(parentA , parentB , pointB);
  return [childA , childB];

def mutate(child):
  for i in range(0,len(child)):
    if(random() < mutationProb):
      child[i] = int(child[i]==0);
  return child;

def getLowestFitnessIndex():
  min = 1;
  idx = 0;
  for i in range(0,len(populasi)):
    if(populasi[i].fitness < min):
      min = populasi[i].fitness;
      idx=i;
    elif(populasi[i].fitness == min and random() < 0.2):
      idx=i;
  return idx;

def getHighestFitnessIndex():
  min = 0;
  idx = 0;
  for i in range(0,len(populasi)):
    if(populasi[i].fitness > min):
      min = populasi[i].fitness;
      idx=i;
    elif(populasi[i].fitness == min and random() < 0.2):
      idx=i;
  return idx;

def insertToPopulation(child):
  fitnessPoint = getFitnessValue(child);
  idxL = getLowestFitnessIndex();
  if(populasi[idxL].fitness > fitnessPoint):
    return;
  
  populasi[idxL].fitness = fitnessPoint;
  populasi[idxL].gen = child;
  print("Replace index :",idxL,fitnessPoint)



dataTest = None;
populasiCount = 10;
populasi = [None] * populasiCount;
totalFitness = 0;
mutationProb = 0.01;
limit = 10000;
print("Loading data please wait...\n");
dataTest = loadData("datatest.txt");
print("\nLoading data complete, data test have been saved");

#generate populasi
print("Generating first generation in population");
generatePopulasi();
print("Complete...");
print("Calculating fitness value");
for i in range(0 , populasiCount):
  populasi[i].fitness = getFitnessValue(populasi[i].gen);
  print(populasi[i].fitness);
print("Complete...");
loop = 0;
while(loop < limit):
  totalFitness = 0;
  for i in range(0 , populasiCount):
    totalFitness = totalFitness + populasi[i].fitness;
  print("Selecting Parent");
  parent = [0,0];
  while(parent[0] == parent[1]):
    parent[0]=getParent(totalFitness);
    parent[1]=getParent(totalFitness);
  print("parent",parent);
  print("Complete...");
  print("Get 2 Random Point");
  shortestParent = getShortestParent(parent);
  point = getRandom2Point(populasi[parent[shortestParent]]);
  otherPoints = getOtherPoint(point);
  print("Promary Point",point,"Other Point",otherPoints);
  print("Complete...");
  print("Duplicate Crossover and Generate Child");
  child = crossover(populasi[parent[0]].gen,populasi[parent[1]].gen,point , otherPoints);
  print("Child A len : ",len(child[0]));
  print("Child B len : ",len(child[1]));
  print("Complete...");
  print("Mutation");
  child[0] = mutate(child[0]);
  child[1] = mutate(child[1]);
  print("Complete...");
  print("Survivor");
  insertToPopulation(child[0]);
  insertToPopulation(child[1]);
  print("Complete...");
  loop += 1;

idx = getHighestFitnessIndex();
print("Best Result :",idx);
print("Fitness :",populasi[idx].fitness);
print("Gen :");
print(populasi[idx].gen);
print();
print("Menjawab datauji");
dataUji = loadData("datauji.txt");
f = open("result.txt", "w")
for i in range( 0 , len(dataUji)):
  resultAnswer = getResult(populasi[idx].gen , dataUji[i]);
  print(i,resultAnswer);
  f.write(str(resultAnswer)+"\n");

f.close()
  


