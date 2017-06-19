import os
import cv2


def video2frames(video_path, frame_dir, start_idx=0, ext='jpg'):
    if not os.path.isfile(video_path):
        raise IOError('video file "{}" not found'.format(video_path))
    vcap = cv2.VideoCapture(video_path)
    if not os.path.isdir(frame_dir):
        os.makedirs(frame_dir)
    converted = 0
    while True:
        ret, img = vcap.read()
        if not ret:
            break
        file_idx = converted + start_idx
        filename = os.path.join(frame_dir, '{:06d}.{}'.format(file_idx, ext))
        cv2.imwrite(filename, img)
        converted += 1


def main():
    with open('filelist.txt', 'r') as f:
        video_list = [line.rstrip('\n') for line in f]
    for vid in video_list:
        print('processing video {}.mp4'.format(vid))
        video2frames('videos/{}.mp4'.format(vid), 'frames/{}'.format(vid))


if __name__ == '__main__':
    main()
