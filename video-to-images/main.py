import cv2
import os
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)
    try: 
        # creating a folder named data 
        if not os.path.exists('output'): 
            os.makedirs('output') 
    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of output') 
    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success, image = vidObj.read()

    while success:
        # Saves the frames with frame-count
        name = './output/frame' + str(count) + '.jpg'
        print ('Extracting...' + name)
        cv2.imwrite(name, image)

        # Read the next frame
        success, image = vidObj.read()

        count += 1

# Driver Code
if __name__ == '__main__':
    # Calling the function
    # Video by Taryn Elliott: https://www.pexels.com/video/an-african-penguin-preening-on-a-rocky-shore-5548176/
    FrameCapture(r"sample.mp4")
