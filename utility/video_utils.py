import cv2 

def read_video(video_path) :
    capture = cv2.VideoCapture(video_path) 
    frames = [] 
    while True :
        ret , frame = capture.read() 
        if not ret :
            break 
        frames.append(frame) 
    return frames 

def save_video(ouput_frames, output_path) :
    coordinate= cv2.VideoWriter_fourcc(*'XVID')
    outp = cv2.VideoWriter(output_path , coordinate , 24 , (ouput_frames[0].shape[1],ouput_frames[0].shape[0]))
    for frame in ouput_frames :
        outp.write(frame) 
    outp.release()
