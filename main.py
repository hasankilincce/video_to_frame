import cv2


def video_to_frame(video_path, output_path):
    video = cv2.VideoCapture(video_path)

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    print("Video FPS'i : {} ".format(fps))
    print("Video Uzunluğu : {} saniye".format(frame_count/fps))

    min_value = int(input("Başlangıç Saniyesi : "))
    max_value = int(input("Bitiş Saniyesi : "))

    process_count = (max_value - min_value) * fps
    count = 0
    counter = 1


    while video.isOpened():
        ret, frame = video.read()

        if ret:
            if fps * min_value <= count < fps * max_value:

                frame_path = output_path + "/frame{}.jpeg".format(counter)
                cv2.imwrite(frame_path, frame)
                print("İşlenen görüntü {}/{}".format(counter, process_count))
                counter += 1
            count += 1

            if counter == process_count + 1:
                break

    video.release()

    print("İşlem tamamlandı.")

video_to_frame("us.mp4", "output_path")