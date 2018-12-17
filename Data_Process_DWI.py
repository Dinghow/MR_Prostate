
# coding: utf-8

# In[1]:


import os
from shutil import copytree, ignore_patterns


# In[2]:


def logException(path,reason):
    with open('file_process_log.txt','a') as fileobject:
        fileobject.write('\n Exception: '+path+' '+reason)
        print('Exception: '+path+' '+reason)


# In[3]:


# Set the paths
base_path = "..\\data\\"


# In[4]:
START_STR='T2_TSE_TRA_FS'
START_STR='EP2D_DIFF_TRA_B0_B800_B1200_B1500'
START_STR='EP2D_DIFF_TRA_B0_B800_B1200_B1500_0'

folder_list = os.listdir(base_path)

# Consider the folder '.DS_Store', if on windows, please remove related code
for folders in folder_list[:]:
    if not os.path.isdir(folders):
        if not folders == '.DS_Store':
            print('Current folder:'+str(folders))
            second_path = base_path + folders
            second_list = os.listdir(second_path)
            # print (second_list)
            if(len(second_list)>1): #if this patient has more than one folders, throw exception
                logException(second_path, 'more than one folders')
            else:
                for second_folders in second_list:
                    if not second_folders == '.DS_Store':
                        print(second_folders)
                        third_path = second_path + '\\'+second_folders
                        third_list = os.listdir(third_path)
                        for third_folders in third_list:
                            if third_folders.startswith(START_STR):
                                file_path = third_path+'\\'+third_folders
                                file_list = os.listdir(file_path)
                                print(len(file_list))
                                # print (file_list)
                                if(len(file_list) <> 80):
                                    logException(file_path, 'more than 80 IMA files in a folder')
                                else:
                                    print(base_path+folders)
                                    #copytree(base_path+folders, 'Qulified_Patient\\'+folders)
                                    copytree(file_path,'Qulified_DWI_Patient\\'+folders+'\\'+third_folders)
