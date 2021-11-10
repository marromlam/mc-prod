from Gauss.Configuration import *
import random

output = "DATAFILE='file:$sim_file' TYP='POOL_ROOTTREE' OPT='RECREATE'"

# Generator phase, set random numbers
number = random.random()
number2 = random.random()

# Configure Gauss
GaussGen = GenInit("GaussGen")
GaussGen.FirstEventNumber = int(number*1000)
GaussGen.RunNumber = int(number2*10000)
LHCbApp().EvtMax = int($number_of_events)
OutputStream("GaussTape").Output = str(output)
