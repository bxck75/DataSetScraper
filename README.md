# DataSetScraper
workflow image rip to dataset

# capture faces 
cd EIGEN_capture_faces
for i in `ls 'EIGEN_ImageCollector/downloads/portrait'`;do 
	python capture_faces.py 'EIGEN_ImageCollector/downloads/portrait/'$i; 
	sudo rm 'EIGEN_ImageCollector/downloads/portrait/'$i
	rest=wc -l `ls EIGEN_ImageCollector/downloads/portrait`
	echo $rest
done
# resize to same size
cd /root/Bureaublad/TOP_APS/EIGEN_pix2pix_tools
bash resize.sh 'EIGEN_capture_faces/detected_faces'

# make dataset
cd /root/Bureaublad/TOP_APS/EIGEN_progressive_growing_of_gans
python dataset_tool.py create_from_images 'datasets/portrait' 'EIGEN_capture_faces/detected_face_resized' 

# train set
python train.py 'datasets/ms13'
