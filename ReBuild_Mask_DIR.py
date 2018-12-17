import os,shutil
from glob import glob

mask_paths=glob('.\\Image\\*\\')

dir_list=['T2','DWI','ADC']
for mask_path in mask_paths[:]:
	if os.path.exists(mask_path+'Mask'):
		shutil.rmtree(mask_path+'Mask')
		os.mkdir(mask_path+'Mask')
		for dir_name in dir_list:
			os.mkdir(mask_path+'Mask\\'+dir_name)
			for i in range(10):
				os.mkdir(mask_path+'Mask\\'+dir_name+'\\'+(str)(i+1))

# os.listdir('.\\Image\\')
