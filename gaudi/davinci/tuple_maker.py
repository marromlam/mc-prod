from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
from Configurables import DaVinci
from GaudiConf import IOHelper

# Stream and stripping line we want to use
stream = 'AllStreams'
line = '$strippingline'

dtt = DecayTreeTuple("DVTuple")
dtt.Inputs = ['/Event/{0}/Phys/{1}/Particles'.format(stream, line)]
# dtt.Decay = '[B_s0 -> mu+ mu- K+ K-]cc'
dtt.Decay = 'B_s0 -> ^(J/psi(1S) -> ^mu+ ^mu-) ^(phi(1020) -> ^K+ ^K-)'

# Configure DaVinci
DaVinci().UserAlgorithms += [dtt]
DaVinci().InputType = '$extension'.upper()
DaVinci().TupleFile = '$output_file'
DaVinci().HistogramFile = 'DV_histograms.root'
DaVinci().PrintFreq = 1000
DaVinci().DataType = '$year'
DaVinci().Simulation = True
# Only ask for luminosity information when not using simulated data
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().EvtMax = -1
# TODO: Template these
DaVinci().CondDBtag = 'sim-20170721-2-vc-md100'
DaVinci().DDDBtag = 'dddb-20170721-3'

# Use the local input data
IOHelper().inputFiles([ '$input_file' ], clear=True)

