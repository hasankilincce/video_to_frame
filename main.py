import cv2

min_value = int(input("Başlangıç Saniyesi : "))
max_value = int(input("Bitiş Saniyesi : "))

def video_to_frame(video_path, output_path, min_value, max_value):
    video = cv2.VideoCapture(video_path)

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    count = 0

    while video.isOpened():
        ret, frame = video.read()

        if ret:
            if fps * min_value <= count <= fps * max_value:

                frame_path = output_path + "/frame{}.jpeg".format(count)
                cv2.imwrite(frame_path, frame)
                print("İşlenen görüntü {}/{}".format(count, frame_count))

            count += 1

        else:
            break

    video.release()

    print("İşlem tamamlandı.")

video_to_frame("istanbul.mp4", "output_path", min_value, max_value)