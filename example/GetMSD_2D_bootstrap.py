import scipy
import sys
import random
import re


TrajNum = int(sys.argv[1]) 
timestep = float(sys.argv[2])  ### OR BINWIDTH
BootstrapNum = int(sys.argv[3])


dr2   = {}
AllSteps = []
for id in range(1,TrajNum+1) :
   ID = "{0:02}".format(id)
   print "reading Traj", ID
   dr2[ID] = {}
   Time  = []
   Xcoor = []
   Ycoor = []
   FileIn = open("Traj"+ID+".dat")
   Lines = FileIn.readlines()
   for line in Lines :
      Words = line.split()
      Time.append(float(Words[0]))
      Xcoor.append(float(Words[1]))      
      Ycoor.append(float(Words[2]))      

   for i in range(len(Xcoor)-1) :
      for j in range(i,len(Xcoor)) :
         step = round((Time[j]-Time[i])/timestep)
         if step >= 0 :
            if step not in AllSteps :
               AllSteps.append(step)
            if step in dr2[ID].keys() :
               dr2[ID][step].append((Xcoor[j]-Xcoor[i])**2 + (Ycoor[j]-Ycoor[i])**2)
            else :
               dr2[ID][step] = [(Xcoor[j]-Xcoor[i])**2 + (Ycoor[j]-Ycoor[i])**2]



AllSteps.sort(key=float)
dr2_tot = {}
for step in AllSteps :
   dr2_tot[step] = []

for boot in range(BootstrapNum) :
   print "running bootstrap round", boot+1, "/", BootstrapNum  

   dr2_sample = {}
   for step in AllSteps :
      dr2_sample[step] = []

   TrajList = []
   for j in range(TrajNum) :
      TrajList.append(random.choice(range(1,TrajNum+1)))

   for trajid in range(len(TrajList))  :
      ID = "{0:02}".format(TrajList[trajid])
      for step in dr2[ID].keys() :
         dr2_sample[step].extend(dr2[ID][step]) 

   for step in dr2_sample.keys() :
      if len(dr2_sample[step]) > 0 :
         dr2_tot[step].append(scipy.average(dr2_sample[step]))

            

FileOut    = open("MSD_2D_bootstrap_TrajNum"+str(TrajNum)+"_timestep"+str(timestep)+".dat", 'w')
for step in AllSteps :
   b = scipy.percentile(dr2_tot[step],95)
   a = scipy.percentile(dr2_tot[step],5)
   print>>FileOut, step, "\t", "{0:.4f}".format(scipy.average(dr2_tot[step])), "\t",  "{0:.4f}".format(b), "\t", "{0:.4f}".format(a)
FileOut.close()


