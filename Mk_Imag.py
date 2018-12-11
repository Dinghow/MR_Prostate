import os
from glob import glob
# import shutil.copytree
import shutil



path='E:\\Process_Data\\Image\\'

patient_folders=glob(path+'*')

# print (patient_folders)


def mk_mask_dir(path):
	# os.mkdir(path+'\\'+'Image')
	# shutil.rmtree(path+'\\'+'Image')
	# shutil.rmtree(path+'\\'+'Mask')
	shutil.copytree(path+'\\',path+'\\'+'Image\\')
	os.mkdir(path+'\\'+'Mask')
	for i in range(10):
		os.mkdir(path+'\\'+'Mask\\'+(str)(i+1))
	delete_dir=os.listdir(path)
	# print (delete_dir)
	for dir in delete_dir:
		if dir <>'Image' and dir <>'Mask':
			shutil.rmtree(path+'\\'+dir)
			# print (dir)
			# print ('delete')
for folder in patient_folders:
	mk_mask_dir(folder)