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
        
        bash 1_Img2Set.sh [ --help ] 
                                                    --search-key 'alien portrait' 
                                                    --max-results 1000 
                                                    --debug
		-h, --help              Display help
		-d, --debug         	debug mode.
		-s, --search-key        search key for images
		-m, --max-results       Set max results
		-o, --output-o      Where does the dataset go?
		
        Example: bash 1_Img2Set.sh --output-folder 'mugshot' --max-results 200 --search-key 'mugshot'
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



# scrape images
cd $ROOT_PATH/EIGEN_ImageCollector
python $ROOT_PATH/EIGEN_ImageCollector/GetImages.py "${SEARCH_KEY}" $MAX_RESULTS | tee  scrape_log.txt

# capture faces 
cd $ROOT_PATH/EIGEN_capture_faces
#rip all faces from images in folder
folder="${SEARCH_KEY}"
to_replace=' '
replacement="+"
folder_clean=${folder//$to_replace/$replacement}
# echo "capturing to "$folder_clean
# echo 'getting images from '$ROOT_PATH'/EIGEN_ImageCollector/ripped_images/'$folder_clean
# loop over images and get faceboxes
for i in `ls $ROOT_PATH/EIGEN_ImageCollector/ripped_images/$folder_clean`; do 
	python $ROOT_PATH/EIGEN_capture_faces/capture_faces.py $ROOT_PATH/EIGEN_ImageCollector/ripped_images/$folder_clean/$i | tee  capture_log.txt
done

# Resize face images to same size
cd $ROOT_PATH/tools
bash resize.sh $ROOT_PATH'/EIGEN_Face_Capture/output' | tee  resize_log.txt

# # make final dir under construct
# echo mkdir -p /root/terra_1TB/BACKUP_TOP_APPS/tool1/DataSetScraper/image_data/$folder_clean
# # moveshit to final dit
# mv /root/terra_1TB/BACKUP_TOP_APPS/tool1/DataSetScraper/EIGEN_capture_faces/detected_faces_resized $ROOT_PATH/image_data/$folder_clean
# echo $ROOT_PATH'/datasets/'$OUTPUT_FOLDER #out
# echo $ROOT_PATH'/image_data/'$folder_clean #in

# Make dataset
cd $ROOT_PATH/EIGEN_progressive_growing_of_gans
python $ROOT_PATH/EIGEN_progressive_growing_of_gans/dataset_tool.py \
        create_from_images \
        $ROOT_PATH'/datasets/'$OUTPUT_FOLDER \
        $ROOT_PATH'/EIGEN_capture_faces/detected_faces_resized' | tee  dataset_log.txt

echo $ROOT_PATH'/datasets/'$OUTPUT_FOLDER

# #clear old images
sudo rm -r $ROOT_PATH/EIGEN_capture_faces/detected_faces/*
sudo rm -r $ROOT_PATH/EIGEN_capture_faces/detected_faces_resized/*
sudo rm -r $ROOT_PATH/EIGEN_ImageCollector/ripped_images/* 



