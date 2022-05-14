import pafy,cv2,os,time,imutils,shutil,img2pdf,glob,base64
import streamlit as st
#constants 
FRAME_RATE = 3                   # no.of frames per second that needs to be processed, fewer the count faster the speed
WARMUP = FRAME_RATE              # initial number of frames to be skipped
FGBG_HISTORY = FRAME_RATE * 15   # no.of frames in background object
VAR_THRESHOLD = 16               # Threshold on the squared Mahalanobis distance between the pixel and the model to decide whether a pixel is well described by the background model.
DETECT_SHADOWS = False            # If true, the algorithm will detect shadows and mark them.
MIN_PERCENT = 0.1                # min % of diff between foreground and background to detect if motion has stopped
MAX_PERCENT = 3                  # max % of diff between foreground and background to detect if frame is still in motion

def get_frames(url):
    '''A func to return the frames from a video located at urlthis function skips frames as defined in FRAME_RATE'''
    video = pafy.new(url)
    video_path=video.getbest(preftype="mp4")
    vs = cv2.VideoCapture(video_path.url)
    if not vs.isOpened():
        raise Exception(f'unable to open file {video_path}')
    total_frames = vs.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_time = 0
    frame_count = 0
    while True:
        vs.set(cv2.CAP_PROP_POS_MSEC, frame_time * 1000)  
        frame_time += 1/FRAME_RATE
        (_, frame) = vs.read()
        if frame is None:
            break
        frame_count += 1
        yield frame_count, frame_time, frame
    vs.release()
	
def detect_unique_screenshots(video_url, output_folder_screenshot_path):
    ''' Only Identify and save unique images '''
    fgbg = cv2.createBackgroundSubtractorMOG2(history=FGBG_HISTORY, varThreshold=VAR_THRESHOLD,detectShadows=DETECT_SHADOWS)
    captured = False
    start_time = time.time()
    (W, H) = (None, None)
    screenshoots_count = 0
    for frame_count, frame_time, frame in get_frames(video_url):
        orig = frame.copy() 
        frame = imutils.resize(frame, width=600) 
        mask = fgbg.apply(frame)

        if W is None or H is None:
            (H, W) = mask.shape[:2]

        p_diff = (cv2.countNonZero(mask) / float(W * H)) * 100

        if p_diff < MIN_PERCENT and not captured and frame_count > WARMUP:
            captured = True
            filename = f"{screenshoots_count:03}_{round(frame_time/60, 2)}.png"
            path = os.path.join(output_folder_screenshot_path, filename)
            cv2.imwrite(path, orig)
            screenshoots_count += 1

        elif captured and p_diff >= MAX_PERCENT:
            captured = False
    return 

def initialize_output_folder():
    '''Clean the output folder if already exists'''
    root_dir=os. getcwd()
    output_dir=root_dir + "\output"
    if os.path.exists(output_dir):
        st.write("removing output dir" )
        st.write(output_dir)
        shutil.rmtree(output_dir)
        os.makedirs(output_dir,exist_ok=True)
    else:
        os.makedirs(output_dir,exist_ok=True)
    return output_dir

def convert_screenshots_to_pdf(output_folder_screenshot_path):
    ''' Convert PNG Image to PDF '''
    output_pdf_path = output_folder_screenshot_path + '\demo.pdf'
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(sorted(glob.glob(f"{output_folder_screenshot_path}/*.png"))))
    st.write('Pdf Created!')
    st.write('pdf saved at: ' + output_pdf_path)
    

if __name__ == "__main__":
    video_url = st.text_input('Enter URL of any youtube video')
    root_dir=os.getcwd()
    output_dir=root_dir + "\output"
    output_pdf_path = output_dir + '\demo.pdf'

    if st.button("convert"): 
        root_dir=os.getcwd()
        output_dir=root_dir + "\output"
        output_folder_screenshot_path = initialize_output_folder()
        detect_unique_screenshots(video_url,output_folder_screenshot_path)
        convert_screenshots_to_pdf(output_folder_screenshot_path)

    with open(output_pdf_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()    
    st.download_button(label="Download_PDF",data=PDFbyte,file_name="download_converted_file.pdf",mime='application/octet-stream')
