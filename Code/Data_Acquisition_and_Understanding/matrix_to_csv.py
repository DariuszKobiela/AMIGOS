import scipy.io
import numpy as np
import csv
import os

target_dir = "Processed_Data"
source_dir = 'D:\AMIGOS'
for part in range(1,41):
    #create target directory
    if not os.path.exists(os.path.join(source_dir,target_dir)):
        os.mkdir(os.path.join(source_dir,target_dir))
    #participant id
    participant = part
    if participant>9:
        participant = str(participant)
    else:
        participant= "0"+str(participant)

    participant_dir = "P" + participant

    # create participant directory
    if not os.path.exists(os.path.join(source_dir,target_dir,participant_dir)):
        os.mkdir(os.path.join(source_dir,target_dir,participant_dir))

    source_file = os.path.join(source_dir,"Data_Original","Data_Original_"+participant_dir,"Data_Original_"+participant_dir+".mat")
    #open matlab matrices
    AMIGOS = scipy.io.loadmat(source_file)

    EEG = AMIGOS['EEG_DATA']
    ECG = AMIGOS['ECG_DATA']
    GSR = AMIGOS['GSR_DATA']
    VideoID_array = AMIGOS['VideoIDs']
    VideoID_list = []
    for i in VideoID_array:
        for j in i:
            for g in j:
                VideoID_list.append(g)
    # print(VideoID_list)
    #csv name: P01_VXX
    index=0
    #all rows in all videos
    for i in EEG:
        # all rows in video
        for j in i:
            VideoID = VideoID_list[index]
            print(VideoID)
            video_dir = "V_" + VideoID
            print(video_dir)
            # create video directory
            if not os.path.exists(os.path.join(source_dir, target_dir, participant_dir,video_dir)):
                os.mkdir(os.path.join(source_dir, target_dir, participant_dir,video_dir))
            target_file = participant_dir + "_V" + VideoID + "_EEG.csv"
            print(target_file)
            # create eeg file
            file = open(os.path.join(os.path.join(source_dir, target_dir, participant_dir, video_dir, target_file)), "w",
                        encoding='utf-8', newline='')
            file = csv.writer(file)
            #write headers to file
            file.writerow(
                ["Interpolated", "Raw", "AF3", "F7", "F3", "FC5", "T7", "P7", "01", "02", "P8", "T8", "FC6", "F4", "F8",
                 "AF4", "GYROX", "GYROY"])
            #sigle row
            for g in j:
                row = g[1:19]
                file.writerow(row)
            print(index)
            index = index+1
            print(index)
    index=0
    #all rows in all videos
    for i in ECG:
        # all rows in video
        for j in i:
            VideoID = VideoID_list[index]
            print(VideoID)
            video_dir = "V_" + VideoID
            print(video_dir)
            if not os.path.exists(os.path.join(source_dir, target_dir, participant_dir,video_dir)):
                os.mkdir(os.path.join(source_dir, target_dir, participant_dir,video_dir))
            target_file = participant_dir + "_V" + VideoID + "_ECG.csv"
            print(target_file)
            file = open(os.path.join(os.path.join(source_dir, target_dir, participant_dir, video_dir, target_file)), "w",
                        encoding='utf-8', newline='')
            file = csv.writer(file)
            file.writerow(
                ["ECG_RA", "ECG_LA", "X_ACCEL", "Y_ACCEL", "Z_ACCEL"])
            #single row
            for g in j:
                row = g[1:]
                file.writerow(row)
            print(index)
            index = index+1
            print(index)

    index=0
    #all rows in all videos
    for i in GSR:
        # all rows in video
        for j in i:
            VideoID = VideoID_list[index]
            print(VideoID)
            video_dir = "V_" + VideoID
            print(video_dir)
            if not os.path.exists(os.path.join(source_dir, target_dir, participant_dir,video_dir)):
                os.mkdir(os.path.join(source_dir, target_dir, participant_dir,video_dir))
            target_file = participant_dir + "_V" + VideoID + "_GSR.csv"
            print(target_file)
            file = open(os.path.join(os.path.join(source_dir, target_dir, participant_dir, video_dir, target_file)), "w",
                        encoding='utf-8', newline='')
            file = csv.writer(file)
            file.writerow(
                ["GSR_RAW", "X_ACCEL", "Y_ACCEL", "Z_ACCEL"])
            #single row
            for g in j:
                row = g[1:]
                file.writerow(row)
            print(index)
            index = index+1
            print(index)
