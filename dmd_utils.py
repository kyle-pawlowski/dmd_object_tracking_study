import numpy as np
import cv2
from pydmd import DMD

def getVideoFrames(filename, frames):
    framen = frames[1] - frames[0]
    video = cv2.VideoCapture(filename)
    #cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    matrix = np.empty((framen,frame_height*frame_width*3), np.dtype('uint8'))
    ret = True
    fc = 0
    while fc<frames[1] and ret:
        if fc < frames[0]:
            ret, image = video.read()
            fc+=1
            continue
        else:
            ret, image = video.read()
            #print(type(image))
            #original_image = Image.fromarray(image,'RGB')
            #original_image.show(title='original image')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            vectorized = np.reshape(image, (frame_height*frame_width*3,))
            matrix[fc-frames[0]] = vectorized
            fc+=1
    return matrix

def frame_generator(filename, window):
    frame_count = 0 
    video = cv2.VideoCapture(filename)
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    while frame_count+window <= total_frames:
        image_sequence = getVideoFrames(filename, (frame_count,frame_count+window))
        yield image_sequence

def getModes(sequence):
    dmd = DMD(svd_rank=6)
    dmd.fit(sequence.T)
    return dmd.modes
