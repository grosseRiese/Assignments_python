# -*- coding: utf-8 -*-

import cv2
import glob
import numpy as np
from PIL import Image
import os
import pickle
import json,io
import matplotlib.pyplot as plt
###########################################################

def antal_plus(M):
    plus = 0
    
    for i in range(2, 580):
        for j in range(2 , 760 ):
            
            if (M[i,j] == 128 and M[i-1,j]== 128 and M[i-2,j] == 128
                and M[i,j-1] == 128 and M[i,j-2]==128 and M[i+1,j]==128
                and M[i+2,j]==128 and M[i,j+1]==128 and M[i,j+2]==128):
                
                plus = plus + 1
                
    return plus
    #print(f" Plus: {M} ")
    
##########################################################

def count_plus_in_all():
    #Using os library to walk through folders
    source_folder = r'C:/Users/omrdh/Desktop/My_ WorkSpace _file/Uni & Schools/GU-Gothenburg university 2021/Matematik program 180hp/V_termin_2022/Python_Extra_Exercises/Lab_moments/Laboration_IV/Bilder'#/01_5DC
    count = 0    
    tupl =()
    general_name = ''
    for root, dirs, files in os.walk(source_folder):
    
        sub_string='Bilder'
        #print("sub_string: ",root.find(sub_string))
        string_root = root[174:]
        #print(string_root)
        
        for name in files:
           count += 1
           
           path = os.path.join(root, name)
           
           im = Image.open(path)
           M = np.asarray(im)
           
           #antal_plus(M)
           general_name = string_root
           tupl += ({"id":f"{count}" , "path-name": f"{os.path.join(root, name)}","sub-file":f"{string_root}","green-plus": antal_plus(M),"img-name":f"{name}"},)  #cz its uple must have in the end ' , '
           
    print("Tuple: " ,tupl)      #Tuple:immutable:cannt change

    # Serializing json 
    json_object = json.dumps(tupl, indent = 4)
    L = {"Number of images" : f"{count}"}
    jsn_obj_num = json.dumps(L,indent = 4)
    
    # Writing to sample.json
    with open("json_data.json", "w") as outfile:
        outfile.writelines('{')
        outfile.writelines('\"files name\" :' + json_object)
        outfile.writelines(',')
        outfile.writelines('\"Antal imgs\": [' + jsn_obj_num + ']')
        outfile.writelines('}')
     
    #print(f"Count all imgs: {count}")
    #print(f"Arr of imgs: {arr}")
   
#count_plus_in_all()   


###################################################
def histogram_pyplot(a):    
    #print(a)
    arr=[]
    for v in range(0,400,3):
        arr.append(v)
        
    #print (arr) 
   
    # Creating histogram
    fig, ax = plt.subplots(figsize =(10, 6))
    ax.hist(a, bins = arr,density=True, facecolor='teal', alpha=0.75) #bins=[0,.,.,.,. etc]
    plt.xlabel("fördelningen av Antal-plus")
    # Show plot
    plt.show()
    
########################

def read_file(): 
    
    with open('json_data.json','r') as json_file:
        js_dat = json_file.read()
        obj = json.loads(js_dat)
        
        antal_img = obj['Antal imgs'][0]['Number of images']
        print('1- Totala antalet bilder: ' , antal_img)
        
    sum_pls = 0
    grn_plus = []
    my_obj={}
    small2,stor2 = 0,0
    
    tple = ()
    tpleII = ()
    
    smal_sub_file=""
    smal_pic_name=""
    
    big_sub_file=""
    big_pic_name=""
    
    for ob in obj["files name"]:  
        sum_pls += ob["green-plus"]
        grn_plus.append(ob["green-plus"])
        
        small2 = np.min(grn_plus)
        stor2 = np.max(grn_plus)
        
        
        if(ob.get("green-plus") == small2 ):
            sub_file = ob.get("sub-file")
            pic_name = ob.get("img-name")
            #print(f"2- Minsta antalet plus: {small2} , är i filen: {sub_file}/ {pic_name} ")  
           
            tple += ({"small-subfile":f"{sub_file}","pic_name": f"{pic_name}"},)
            
        if(ob.get("green-plus") == stor2 ):
            sub_file = ob.get("sub-file")
            pic_name = ob.get("img-name")
            #print(f"3- Största antalet plus: {stor2} , är i filen: {sub_file}/ {pic_name} ")
            
            tpleII += ({"big-subfile":f"{sub_file}","pic_name_big": f"{pic_name}"},)
        
        
            
    for itm in tple:
        smal_sub_file = itm["small-subfile"]
        smal_pic_name = itm["pic_name"]
        #print(smal_sub_file,smal_pic_name)
    
    for it in tpleII:
        big_sub_file = it["big-subfile"]
        big_pic_name = it["pic_name_big"]
        #print(big_sub_file,big_pic_name)
        
   
    print(f"2- Minsta antalet plus: {small2} , är i filen: {smal_sub_file} / {smal_pic_name} ")  
    print(f"3- Största antalet plus: {stor2} , är i filen: {big_sub_file} / {big_pic_name} ") # det finns 2 styckna id=301 och id=201 
    print("4- Medelvärdet av antalet plus: ", np.floor(sum_pls/int(antal_img)) )
    print("5- Totala antalet plus: ", sum_pls)
    
    histogram_pyplot(grn_plus)
    
read_file()
    
###################################################

