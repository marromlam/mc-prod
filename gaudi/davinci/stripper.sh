source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt


mkdir -p ${SANDBOX}
cd ${SANDBOX}

lb-run DaVinci/${DAVINCI_VERSION} gaudirun.py ${JOB_FILE}


cd ${MC_PROD}
