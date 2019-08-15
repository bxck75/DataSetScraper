#!/bin/bash
######################################################################
##     Workflow image rip to dataset by Boudewijn Kooij 2019        ##
####################BEGIN ARGPARSE####################################

dirname $0
ROOT_PATH='/root/terra_1TB/BACKUP_TOP_APPS/tool1/DataSetScraper'
###########################HELPER#####################################
showHelp() {
	echo " 
		Usage:    
        
        bash 1a_TrainSet.sh [ --help ] 
                --data-set 'face_portrait' # folder in datasets folder
                --debug


		-h, --help          Display help
		-d, --debug         Debug mode.
		-d, --data-set      Dataset to train on

		
        Example: bash 1a_TrainSet.sh --data-set 'mugshot'
        "

	exit 1
}
################################PARSING#################################
function showlist(){
	ls datasets/
}
while [[ $# -gt 0 ]]; do
    key="$1"
    case "$key" in
        # Will catch either -d or --debug
        -d|--debug)
        DEBUG=1
        ;;
        # Will catch either -h or --help
        -h|--help)
        HELP=1
        ;;
         # Will catch -d value or --data-set value
        -d|--data-set)
        shift # past the key and to the value
        DATA_SET="$1"
        ;;
        # # Will catch -o value or --output-folder value
        # -o|--output-folder)
        # shift # past the key and to the value
        # OUTPUT_FOLDER="$1"
        # ;;
        # # Will catch -m value or --max-results value        
        # -m|--max-results)
        # shift # past the key and to the value
        # MAX_RESULTS="$1"
        # ;;
        *)
        # Do whatever you want with extra options
        echo "Unknown option '$key'"
        ;;
    esac
    # Shift after checking all the cases to get the next option
    shift
done
####################END ARGPARSE#####################################
if [[ $HELP == 1 ]]; then
	showHelp
	showlist
fi
# wc -l | `ls datasets/$DATA_SET`
cd EIGEN_pgan/
python train.py 'datasets/'$DATA_SET | tee  training_log.txt

# '/root/terra_1TB/BACKUP_TOP_APPS/tool1/DataSetScraper/EIGEN_pgan/train.py' 
# TRAIN!!!!
# python train.py $ROOT_PATH'/datasets/'$OUTPUT_FOLDER  | tee  training_log.txt