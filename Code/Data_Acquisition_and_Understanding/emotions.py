import csv
import os
import shutil

target_dir = "Divided_Data"
source_dir = 'D:\AMIGOS'

#create target directory
if not os.path.exists(os.path.join(source_dir, target_dir)):
    os.mkdir(os.path.join(source_dir, target_dir))
emotions_dirs = ['neutral','disgust','happiness','surprise','anger','fear','sadness']

#create emotion directory
for dir in emotions_dirs:
    if not os.path.exists(os.path.join(source_dir, target_dir,dir)):
        os.mkdir(os.path.join(source_dir, target_dir,dir))

with open('D:\AMIGOS\emotions.csv', 'r',encoding='utf-8', newline='') as source_file:
    source_file = csv.reader(source_file,delimiter=';')
    next(source_file)
    for row in source_file:
        userID = int(row[0])
        if userID > 9:
            userID = "P"+str(userID)
        else:
            userID = "P0" + str(userID)
        videoID = 'V_'+str(row[1])
        video2 = 'V'+str(row[1])
        print(userID," ",videoID)
        #neutral
        if row[2] == '1':
            #copy files to target directory
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[0]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[0]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[0]))
        #disgust
        if row[3] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[1]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[1]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[1]))
        #happiness
        if row[4] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[2]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[2]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[2]))
        #surprise
        if row[5] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[3]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[3]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[3]))
        #anger
        if row[6] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[4]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[4]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[4]))
        #fear
        if row[7] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[5]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[5]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[5]))
        #sadness
        if row[8] == '1':
            shutil.copy(os.path.join(source_dir,'Processed_Data',userID,videoID,userID + "_" + video2 + "_EEG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[6]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_ECG.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[6]))
            shutil.copy(os.path.join(source_dir, 'Processed_Data', userID, videoID, userID + "_" + video2 + "_GSR.csv"),
                        os.path.join(source_dir,target_dir,emotions_dirs[6]))