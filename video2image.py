import cv2
import os
import sys
import argparse

def video2image(video_path,image_path,fps):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("can not open video")
        return
    total_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = video.get(cv2.CAP_PROP_FPS)
    color_channels = video.get(cv2.CAP_PROP_CHANNEL)
    image_size = (video.get(cv2.CAP_PROP_FRAME_WIDTH),video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Video Information:")
    print(f"  Total Frames: {total_frame}")
    print(f"  Original FPS: {original_fps}")
    print(f"  Color Channels: {color_channels}")
    print(f"  Image Size: {image_size}")

    interval = int(original_fps / fps)
    os.makedirs(image_path,exist_ok=True)
    frame_id = 0
    frame_skip = 0
    sucess, image = video.read()
    while sucess:
        sys.stdout.write(f"\rExtracting frame {frame_skip}/{total_frame}")
        cv2.imwrite(os.path.join(image_path,f'frame_{frame_id}.png'),image)
        frame_id += 1
        for _ in range(interval-1):
            frame_skip += 1
            sucess,image = video.read()
            if not sucess:
                break
    video.release()
    print("Done !")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frame from video, you should specify \
                                     video path , image_save path , and fps")
    parser.add_argument("--video_path", type=str,help="path to video",default="./video.mp4")
    parser.add_argument("--output_dir",type=str,help="image save path",default="./frames")
    parser.add_argument("--fps",type=int,help="extract how many frames for one second",default=10)
    args = parser.parse_args()

    video2image(args.video_path,args.output_dir,args.fps)
