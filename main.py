import cv2

def video_to_frame (video_path, output_path):
    video = cv2.VideoCapture(video_path)

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0

    while video.isOpened():
        ret, frame = video.read()

        if ret:
            frame_path = output_path + "/frame{}.jpeg".format(count)
            cv2.imwrite(frame_path, frame)

            count += 1

            print("İşlenen görüntü {}/{}".format(count,frame_count))

        else:
            break

    video.release()

    print("İşlem tamamlandı.")

video_to_frame("istanbul.mp4", "output_path")