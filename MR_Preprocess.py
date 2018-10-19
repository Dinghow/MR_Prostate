import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import scipy.ndimage
import pydicom
from glob import glob

#standard data
case_path='C:\\Users\\hehe\\Desktop\\dcm\\BAO_XUN_YIN_100312588\\PELVIS_PROSTATE_PROGRAM_20111121_101613_906000\\T2_TSE_TRA_FS_0005'
case_path='C:\\Users\\hehe\\Desktop\\dcm\\BAO_XUN_YIN_100312588\\PELVIS_PROSTATE_PROGRAM_20111121_101613_906000\\b-1500'


# case_path='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\HUYONGSHENG_50172302\\PELVIS_PROSTATE_PROGRAM_20150129_135211_921000\\T2_TSE_TRA_FS_0003'
# case_path='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\HUYONGSHENG_50172302\\PELVIS_PROSTATE_PROGRAM_20150129_135211_921000\\b-1500'


# case_path='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\ZHUQINGQUAN_100665572\\PELVIS_PROSTATE_PROGRAM_20140509_084125_546000\\T2_TSE_TRA_FS_0002'

# case_path='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\LIU_HANG_GONG_100371672\\PELVIS_PROSTATE_PROGRAM_20120502_115455_734000\\T2_TSE_TRA_FS_0003'
# case_path='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\HUYONGSHENG_50172302\PELVIS_PROSTATE_PROGRAM_20150129_135211_921000\\T2_TSE_TRA_FS_0003'


case_path_mhd='C:\\Users\\hehe\\Desktop\\dcm\\xian-ai\\aaa.mhd'


nodule_coord=(-29.79,-59.49,-66.97)

nodule_coord=(4.10,-54.13,36.89)
# -19.42,-100.33,39.10


nodule_coord=(nodule_coord[0]*(-1),nodule_coord[1]*(-1),nodule_coord[2])

def filter_dicom_names(case_path):
    dicom_names=[]
    img_files_path=glob(case_path+'\\*.IMA')
    img_files_path.sort()
    # print (img_files_path)
    dicom_index=img_files_path[0].split('\\')[-1].split('.')[4]



    for i in range(len(img_files_path)):

    #     print (img_files_path[i].split('\\')[-1].split('.')[4])

        img_file_name=img_files_path[i].split('\\')[-1]

        series_id=img_files_path[i].split('\\')[-1].split('.')[4]

        if series_id <> dicom_index or i==0:
            dicom_index=series_id
            dicom_names.append(img_files_path[i])
    print (dicom_names)
    dicom_names=tuple(dicom_names)
    
    return dicom_names

    
def write_log(file_names):
    with open('log.txt','a+') as f:
        f.writelines('==========================\n')
        f.writelines(file_names)
        f.writelines('\n==========================\n')


def resample(image, original_spacing, new_spacing=[4.5,4.5,4.5],order=3):
    # Determine current pixel spacing
    spacing = np.array((original_spacing[2],original_spacing[1],original_spacing[0]), dtype=np.float32)
    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = spacing / real_resize_factor
    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, order=order, mode='nearest', prefilter=False)
    return image, new_spacing

def plot_series_nodule(nodule_coord):
    reader = sitk.ImageSeriesReader()
    series_ids = reader.GetGDCMSeriesIDs(case_path)
    # print ('*****************************')
    # print (series_ids)

    dicom_names = reader.GetGDCMSeriesFileNames(case_path,series_ids[0])

    dicom_names=filter_dicom_names(case_path)

    print ('==================')
    print (dicom_names)
    write_log(dicom_names)
    print (len(dicom_names))
    print ('=====================')
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    # print (image)
    img_array = sitk.GetArrayFromImage(image) # z, y, x
    origin_xyz = np.array(image.GetOrigin()) # x, y, z
    spacing_xyz =np.array(image.GetSpacing())  # x, y, z
    print (origin_xyz,spacing_xyz)
    print (img_array.shape)
    # sitk.WriteImage(image, 'abc.mhd') 


    for i in range(img_array.shape[0]):

    	scipy.misc.imsave('.\\Image\\'+(str)(i)+'.jpg', img_array[i])


    center_xyz = (nodule_coord[0], nodule_coord[1], nodule_coord[2])

    index_coord=image.TransformPhysicalPointToIndex (center_xyz)
    print (index_coord)

    # index_coord=(320,262,3)

    import matplotlib.patches as patches

    fig,ax=plt.subplots(1)
    ax.imshow(img_array[index_coord[2]], cmap=plt.cm.gray)

    ax.add_patch(
        patches.Rectangle(
            (index_coord[0]-20, index_coord[1]-20),   # (x,y)
            40,          # width
            40,          # height
            linewidth=1, edgecolor='r', facecolor='none'
        )
    )
    plt.show()

    return img_array,spacing_xyz

def plot_mhd_nodule(nodule_coord):

    image=sitk.ReadImage(case_path_mhd)
    img_array = sitk.GetArrayFromImage(image) # z, y, x
    # print (image)
    print (img_array.shape)
    for i in range(img_array.shape[0]):

    	scipy.misc.imsave('.\\Image\\'+(str)(i)+'.jpg', img_array[i])


    center_xyz = (nodule_coord[0], nodule_coord[1], nodule_coord[2])

    index_coord=image.TransformPhysicalPointToIndex (center_xyz)
    # print (index_coord)

    # index_coord=(320,262,3)

    import matplotlib.patches as patches

    fig,ax=plt.subplots(1)
    ax.imshow(img_array[index_coord[2]], cmap=plt.cm.gray)

    ax.add_patch(
        patches.Rectangle(
            (index_coord[0]-20, index_coord[1]-20),   # (x,y)
            40,          # width
            40,          # height
            linewidth=1, edgecolor='r', facecolor='none'
        )
    )
    plt.show()

    # return img_array,spacing_xyz



# plot_mhd_nodule(nodule_coord)
# print ('================================')





img_array,spacing_xyz=plot_series_nodule(nodule_coord)

# resample_img,resample_spcing=resample(img_array,spacing_xyz)


# print (resample_spcing)

# print (resample_img.shape)


# for j in range(resample_img.shape[0]):
#     scipy.misc.imsave('.\\Resample_Img\\'+(str)(j)+'.jpg', resample_img[j])
