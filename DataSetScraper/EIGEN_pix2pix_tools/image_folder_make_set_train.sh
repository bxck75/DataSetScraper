#!/bin/bash
##########################################################################
#                                                                        #
#									 #

#
#
##########################################################################
# from folder to pix2pix set and train/test
# usage :./p2p_on_folder.sh <images folder> <epochs to train>
# bash image_folder_make_set_train.sh $MYHOME/data/steenmarter 5
# it wil make : 
#  -- <image_folder>_resize (resized pix2pix training set)
#  -- <image_folder>_train (training metrics) beside the original folder

# index.html in the train folder has the evaluation of the training and test

# set root tmp folder
input_img_folder=${1}
training_epochs=${2}
prep=${3} #  True or False wil switch prepping off if this is already done
root_tmp_folder='p2p_process_tmp'
root_data_folder='/root/Bureaublad/data/'
TF_CPP_MIN_LOG_LEVEL='3'  # or any {'0', '1', '2'}'

function process {
	#remove old tmp files if any...
	sudo rm -r /tmp/${root_tmp_folder}
	# Resize source images
	python tools/process.py --input_dir ${input_img_folder} --operation resize --output_dir /tmp/${root_tmp_folder}/_resized
	# Create images with blank centers
	python tools/process.py --input_dir /tmp/${root_tmp_folder}/_resized --operation blank --output_dir /tmp/${root_tmp_folder}/_blank
	# Combine resized images with blanked images side by side
	python tools/process.py --input_dir /tmp/${root_tmp_folder}/_resized --b_dir  /tmp/${root_tmp_folder}/_blank --operation combine --output_dir  /tmp/${root_tmp_folder}/_resized/_combined
	# Split into train/val set
	python tools/split.py --dir /tmp/${root_tmp_folder}/_resized/_combined
	# make dir and copy final images
	sudo mkdir -p ${input_img_folder}_resize
	cp -rf /tmp/${root_tmp_folder}/_resized/_combined/ ${input_img_folder}_resize/
}

function train {
	# Training pix2pix
	x=$1
	echo "[Start training....]"
	# xterm_sizes="55x10+0+${x}"
	xterm_style="-misc-fixed-medium-r-normal--10-*-*-*-*-*-iso8859-15"
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "tensorboard --port 6001 --logdir=${input_img_folder}_train" & 
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "chromium --no-sandbox http://debian:6001" &
	# ((x+=185))
	xterm_sizes="55x35+0+${x}"
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "python pix2pix.py --mode train --output_dir ${input_img_folder}_train --max_epochs ${training_epochs} --input_dir ${input_img_folder}_resize/_combined/train --which_direction BtoA" &
}

function test {
	#Testing model trained so far
	x=$1
	echo "[Start testing....]"
	xterm_style="-misc-fixed-medium-r-normal--10-*-*-*-*-*-iso8859-15"
	xterm_sizes="55x55+335+${x}"
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "tensorboard --port 6002 --logdir=${input_img_folder}_test" & disown
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "chromium --no-sandbox http://debian:6002" &
	# ((x+=185))
	xterm_sizes="55x55+335+${x}"
	xterm -fn $xterm_style -geometry $xterm_sizes -hold -e "python pix2pix.py --mode test --output_dir ${input_img_folder}_test --input_dir ${input_img_folder}_resize/_combined/val --checkpoint ${input_img_folder}_test" &
}

function show_t_t {
	# Show Training summary html
	xterm -geometry "5x5x5x5" -e "chromium --no-sandbox ${input_img_folder}_train/index.html" & disown 
	# Show Testing summary html
	xterm -geometry "5x5x5x5" -e "chromium --no-sandbox ${input_img_folder}_test/index.html" & disown
}

function clean {
	#remove tmp files
	sudo rm -r /tmp/${root_tmp_folder}
}


# Workflow sequence 
if [[ $prep == 1 ]]; then
	process
fi
wait
train 1000
wait
test 1000
wait
clean

