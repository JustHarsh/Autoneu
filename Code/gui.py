from tkinter import Label, Button, Tk, Entry
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from execute import update_label, insert_path_to_db
from tkinter import END

# future steps - patient ID, patient Name


class AutoneuWindow:
    def __init__(self, win):
        self.filepath = ''
        self.file_path_prompt = Button(win, text='Upload x-ray',
                                       font=('Monospace', 15))
        self.file_path_prompt.bind('<Button-1>', self.ask_file)
        self.file_path_prompt.place(x=220, y=551)
        self.btn1 = Entry(win)
        self.btn1.place(x=330, y=550)
        self.btn = Button(win, text='Click to diagnose',
                          font=('Monospace', 15, 'bold'))
        self.btn.place(x=315, y=615)
        self.btn.bind('<Button-1>', self.predict_label)
        self.bg_img(win)

    def ask_file(self, _):
        self.filepath = fd.askopenfilename()
        self.btn1.delete(0, END)
        self.btn1.insert(0, self.filepath)

    def bg_img(self, win):
        self.bg_image = Image.open(r"./bg_image_forApp.jpeg")
        self.bg_image = self.bg_image.resize((720, 480))
        _photo = ImageTk.PhotoImage(self.bg_image)
        img_label = Label(win, image=_photo)
        img_label.photo = _photo
        img_label.place(x=0, y=0)
        img_label.pack()

    def show_img(self):
        test_image = image.load_img(self.filepath, target_size=(256, 256))
        plt.imshow(test_image)
        plt.show()

    def predict_label(self, _):
        test_image = image.load_img(
            self.filepath, target_size=(64, 64))  # loading image
        # converting image to an array of values
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        cnn = tf.keras.models.load_model(
            './Code/saved_model/SavedModel.h5')  # loading cnn
        result = cnn.predict(test_image)  # predict class of the image
        insert_path_to_db(self.filepath)
        update_label(self.filepath, int(result[0][0]))
        if int(result[0][0]) == 1:
            prediction = 'Positive'
            colour = 'red'
        else:
            prediction = 'Negative'
            colour = 'blue'

        lbl = Label(window, text='Diagnosis: '+prediction, fg=colour,
                    font=('Monospace', 14, 'bold'))
        lbl.place(x=312, y=660)  # Result -> x = 323

        window.after(500, self.show_img)


window = Tk()
window['background'] = '#E5E4E2'
prediction_window = AutoneuWindow(window)
window.geometry("720x720")
window.title('Autoneu')
window.mainloop()
