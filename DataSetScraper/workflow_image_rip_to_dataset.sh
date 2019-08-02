#!/bin/bash
######################################################################
##     workflow image rip to dataset by Boudewijn Kooij 2019        ##
####################BEGIN ARGPARSE####################################
ROOT_PATH='/root/terra_1TB/BACKUP_TOP_APPS/DataSetScraper'
echo $ROOT_PATH

###########################HELPER#####################################
showHelp() {
	echo "  
		Usage: bash workflow_image_rip_to_dataset.sh [ -h ] --search-key 'alien portrait' --max-results 1000 --debug
        Usage:  bash workflow_image_rip_to_dataset.sh --output-folder 'aliensfaceportrait' --max-results 100 --search-key 'alien face portrait'
        
		-h, --help              Display help
		-d, --debug         	debug mode.
		-s, --search-key        search key for images
		-m, --max-results       Set max results
		-o, --output-folder     Where does the dataset go?
		"
	exit 1
}
################################PARSING#################################
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
        # Will catch -o value or --output-folder value
        -o|--output-folder)
        shift # past the key and to the value
        OUTPUT_FOLDER="$1"
        ;;
        # Will catch -m value or --max-results value        
        -m|--max-results)
        shift # past the key and to the value
        MAX_RESULTS="$1"
        ;;
         # Will catch -s value or --search-key value
        -s|--search-key)
        shift # past the key and to the value
        SEARCH_KEY="$1"
        ;;
        *)
        # Do whatever you want with extra options
        echo "Unknown option '$key'"
        ;;
    esac
    # Shift after checking all the cases to get the next option
    shift
done
if [[ $HELP == 1 ]]; then
	showHelp
fi

####################END ARGPARSE#####################################
# exit 1
# #clear old images
sudo rm $ROOT_PATH/EIGEN_capture_faces/detected_faces/*
sudo rm $ROOT_PATH/EIGEN_capture_faces/detected_faces_resized/*
# sudo rm -r $ROOT_PATH/EIGEN_ImageCollector/ripped_images/*

# scrape images
cd $ROOT_PATH/EIGEN_ImageCollector
python GetImages.py "${SEARCH_KEY}" $MAX_RESULTS

# capture faces 
cd $ROOT_PATH/EIGEN_capture_faces
#rip all faces from images in folder
folder=$SEARCH_KEY
to_replace=' '
replacement="+"
folder_clean=${folder//$to_replace/$replacement}
# loop over images and get faceboxes
for i in `ls $ROOT_PATH'/EIGEN_ImageCollector/ripped_images/'$folder_clean`; do 
	python capture_faces.py $ROOT_PATH'/EIGEN_ImageCollector/ripped_images/'$folder_clean'/'$i
done

# Resize face images to same size
cd /root/Bureaublad/TOP_APS/EIGEN_pix2pix_tools
bash resize.sh $ROOT_PATH'/EIGEN_capture_faces/detected_faces'

# Make dataset
cd $ROOT_PATH/EIGEN_progressive_growing_of_gans
python dataset_tool.py create_from_images 'datasets/'$OUTPUT_FOLDER $ROOT_PATH'/EIGEN_capture_faces/detected_faces_resized' 
echo $OUTPUT_FOLDER
python train.py $OUTPUT_FOLDER