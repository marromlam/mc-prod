source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt

mkdir -p ${SANDBOX}
cd ${SANDBOX}

lb-run -c best Gauss/${GAUSS_VERSION} gaudirun.py \
${JOB_FILE} \
${APPCONFIGOPTS}/Gauss/Beam6500GeV-md100-${YEAR}-nu1.6.py \
${APPCONFIGOPTS}/Gauss/EnableSpillover-25ns.py \
${APPCONFIGOPTS}/Gauss/DataType-${YEAR}.py \
${APPCONFIGOPTS}/Gauss/RICHRandomHits.py \
${DECFILESROOT}/options/${EVENT_TYPE}.py \
/cvmfs/lhcb.cern.ch/lib/lhcb/GAUSS/GAUSS_${GAUSS_VERSION}/Gen/LbPythia8/options/Pythia8.py \
${APPCONFIGOPTS}/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \
${MC_PROD}/gaudi/Tags.py

cd ${MC_PROD}
