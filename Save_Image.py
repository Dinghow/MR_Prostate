import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage
import pydicom,os
from glob import glob



def plot_series_nodule(case_path,save_img_path):
    reader = sitk.ImageSeriesReader()
    series_ids = reader.GetGDCMSeriesIDs(case_path)
    # print ('*****************************')
    # print (series_ids)

    dicom_names = reader.GetGDCMSeriesFileNames(case_path,series_ids[0])

    # dicom_names=filter_dicom_names(case_path)

    # print ('==================')
    # print (dicom_names)
    # write_log(dicom_names)
    # print (len(dicom_names))
    # print ('=====================')
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    # print (image)
    img_array = sitk.GetArrayFromImage(image) # z, y, x
    # origin_xyz = np.array(image.GetOrigin()) # x, y, z
    # spacing_xyz =np.array(image.GetSpacing())  # x, y, z
    # print (origin_xyz,spacing_xyz)
    # print (img_array.shape)
    # sitk.WriteImage(image, 'abc.mhd') 


    for i in range(img_array.shape[0]):
        if i<9:
            slice_name='slice_00'+(str)(i+1)
            # print (slice_name)
        else:
            slice_name='slice_0'+(str)(i+1)
    	scipy.misc.imsave(save_img_path+'\\'+(str)(slice_name)+'.jpg', img_array[i])


# dcm_folders=os.listdir('.\\Qulified_Patient')
dcm_folders=glob('.\\Qulified_Patient\\*\\*\\')



for dcm_folder in dcm_folders[:]:
	print (dcm_folder)

	dcm_name=dcm_folder.strip().split('\\')[-3]
	print (dcm_name)
	dcm_series=dcm_folder.split('\\')[-2]

	dcm_folder_path='.\\Image\\'+dcm_name
	dcm_series_path='.\\Image\\'+dcm_name+'\\'+dcm_series

	if not os.path.exists(dcm_folder_path):
		os.mkdir(dcm_folder_path)
	if not os.path.exists(dcm_series_path):
		os.mkdir(dcm_series_path)
	save_img_path=dcm_folder.replace('Qulified_Patient','Image')

	plot_series_nodule(dcm_folder,save_img_path)
	# print (dcm_name)