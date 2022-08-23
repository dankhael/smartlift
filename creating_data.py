import cv2


def create_images(video):

    current_frame = 0
    while True:
        done, frame = video.read()

        cv2.imshow("output", frame)
        cv2.imwrite("./dataset/images/" + "frame" + str(current_frame) + ".jpg", frame)
        current_frame += 1

        if cv2.waitKey(1) and 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


video = cv2.VideoCapture("dataset/videos/neto_1.mp4")

create_images(video)
