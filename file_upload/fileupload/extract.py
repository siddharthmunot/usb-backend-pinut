import zipfile,os,shutil
from .models import Content, EkFile

def extractit(path_of_file):

    #ekstep file uploaded path obtained using file.path
    file_path=path_of_file
    print 'WE GON EXTRACT THE FILE AT ' + file_path
    zip_ref=zipfile.ZipFile(file_path,'r')

    index=file_path.find(".ecar")

    #folder name
    folder=file_path[:index]
    print 'WE GON MAKE A FOLDAH CALLED ' + folder

    #create a folder for the ekstep file uploaded uisng its own name
    os.makedirs(folder)

    #ekstep file uploaded folder which contains the unzip version of the ekstep file uploaded
    zip_ref.extractall(folder)
    zip_ref.close()

    #move the ecar file to ekstep file folder starting with the name do_
    for filename in os.listdir(folder):
        if(not filename.endswith(".json")):
            break
    #filename rn has the name of the folder that begins with do_
    index=file_path.rfind('/')
    file_name=file_path[index+1:]
    shutil.copy2(file_path,folder+"/"+filename+"/"+file_name)

    #change the name of manifest file
    change_name=""
    for filename in os.listdir(folder):
        if(filename.endswith(".json")):
            continue
        else:
            change_name=filename
    print change_name

    #renames the manifest file inside the ekstep file uploaded folder
    os.rename(folder+"/manifest.json",folder+"/"+change_name+".json")

    index=file_path.find("/ecar_files")
    content_path=file_path[:index]
    content_path+="/content"
    content_object = Content(ekfile = EkFile.objects.get(slug = file_path[file_path.rfind('/')+1:]), folder_file = filename, json_file = change_name + ".json")
    content_object.save()

    #files list 

    #move the contents of the ekstep file uploaded folder

    for filename in os.listdir(folder):
        print filename
        try:
            shutil.move(folder+"/"+filename,content_path)
        except Exception as e:
            print e
            print "-"*50 + "This file already exists" + "-"*50
            break
    
    #remove's the ekstep file uploaded folder which is empty right now 
    shutil.rmtree(folder)
    #name of the folder which we got after extracting .ecar file
    return change_name
    
