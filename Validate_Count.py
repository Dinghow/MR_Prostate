import os

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

base_path = "..\\data\\"

t2_files=os.listdir('E:\\Process_Data\\Qulified_T2_Patient\\')

adc_files=os.listdir('E:\\Process_Data\\Qulified_ADC_Patient\\')

dwi_files=os.listdir('E:\\Process_Data\\Qulified_DWI_Patient\\')


print (len(t2_files))

print (len(adc_files))

print (len(dwi_files))

# print (len(set(t2_files) & set(adc_files)))
print (Diff(adc_files,t2_files))
print (Diff(t2_files,dwi_files))