import os
for action in os.listdir('/Users/zhongqian/Desktop/DeepLearning/Final_project/UCF-101/'):
    if action == '.DS_Store':
        continue
    path = '/Users/zhongqian/Desktop/DeepLearning/Final_project/UCF-101/'+action
    for group in os.listdir(path):
        index = group.split('_')[-1]
        if index == 'c01.avi':
            filename = path+'/'+group
            command = 'python read_frames_fast.py --video '+filename
            os.system(command)