from tkinter import*
import Signin
import Upgrade
import cv2
import matplotlib.pyplot as plt
import WindowInitializing

def logout(win):
    win.destroy()
    Signin.call()

def homepage1(name):
    root = WindowInitializing.window()
    title = Label(root, text=name, font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    upgrade_frame = Frame(root, bg="white")
    upgrade_frame.place(x=100, y=130)
    btn_upgradeProfile = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="Upgrade Profile", command=lambda :upgradedata(root,name), bg="black", fg="white").grid(row=0, column=0)
    btn_history = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="History",  bg="black", fg="white").grid(row=0, column=2)
    btn_logout = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="Logout" ,command=lambda :logout(root),  bg="black", fg="white").grid(row=0, column=3)

    login_frame = Frame(root, bg="white")
    login_frame.place(x=1100, y=130)
    btn_camera = Button(login_frame, text="camera",width=200,height=70, command=camera, image=root.camera, compound=LEFT,
                       font=("times new roman", 20, "bold"), bg="black", fg="white").grid(row=0, column=0)

    root.mainloop()

def upgradedata(win,name):
    win.destroy()
    Upgrade.callme(name)

def camera():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                image = cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                plt.imshow(image)
                plt.show()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

