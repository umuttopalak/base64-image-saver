import base64
import io
import json
import os
import tkinter as tk
from tkinter import Button, Canvas, Frame, Label, Scrollbar, filedialog

from PIL import Image, ImageTk


class ImageSelectorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Selector")
        self.geometry("450x500")

        self.canvas = Canvas(self)
        self.scroll_y = Scrollbar(
            self, orient="vertical", command=self.canvas.yview)

        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')

        self.select_button = Button(
            self, text="Select Images", command=self.on_select_images)
        self.select_button.pack(side='bottom', fill='x')

        self.convert_button = Button(
            self, text="Convert To Base64", command=self.convert_images, state='disabled')
        self.convert_button.pack(side='bottom', fill='x')

        self.save_button = Button(
            self, text="Save File", command=self.save_base64_data, state='disabled')
        self.save_button.pack(side='bottom', fill='x')

        self.convert_to_image_button = Button(
            self, text="Convert To Image", command=self.convert_to_image)
        self.convert_to_image_button.pack(side='bottom', fill='x')

        self.images = []
        self.file_paths = []
        self.image_datas = []

    def convert_to_image(self):
        json_file = filedialog.askopenfilename(
            title="Select JSON File", filetypes=[("JSON Files", ".json")])

        if not json_file:
            return

        save_directory = filedialog.askdirectory(
            title="Select Directory to Save Images")

        if not save_directory:
            save_directory = os.getcwd()

        with open(json_file, "r") as f:
            data = json.loads(f.read())

        for item in data:
            file_name = item.get("file_name")
            base64_data = item.get("data")

            if file_name and base64_data:
                image_data = base64.b64decode(base64_data)

                image = Image.open(io.BytesIO(image_data))

                save_path = os.path.join(save_directory, file_name)
                image.save(save_path)

                print(f"Saved {file_name} to {save_path}")
            else:
                print("Invalid data in JSON")

    def update_button_states(self):
        if self.file_paths:
            self.convert_button.config(state='normal')
        else:
            self.convert_button.config(state='disabled')

        if self.image_datas:
            self.save_button.config(state='normal')
        else:
            self.save_button.config(state='disabled')

    def convert_images(self):
        self.image_datas.clear()
        if self.file_paths:
            for file_path in self.file_paths:
                base64_data = self.image_to_base64(file_path)
                self.image_datas.append(
                    {"file_name": file_path.split('/')[-1], "data": base64_data})
            print("Conversion Complete.")
        self.update_button_states()

    def image_to_base64(self, image_path):
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')

            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_byte = buffered.getvalue()

        img_base64 = base64.b64encode(img_byte)
        return img_base64.decode('utf-8')

    def on_select_images(self):
        self.file_paths = list(filedialog.askopenfilenames(
            title="Select Images", filetypes=[("Image Files", ".png .jpg .jpeg .gif")]))
        for file_path in self.file_paths:
            self.show_image(file_path)
        self.update_button_states()

    def show_image(self, filepath):
        img = Image.open(filepath)
        img.thumbnail((400, 400))
        photo_img = ImageTk.PhotoImage(img)
        self.images.append(photo_img)
        label = Label(self.frame, image=photo_img)
        label.pack(pady=10)
        delete_button = Button(self.frame, text='Remove', command=lambda: self.delete_image(
            label, delete_button, filepath))
        delete_button.pack()

    def delete_image(self, label, button, file_path):
        label.pack_forget()
        button.pack_forget()
        self.file_paths.remove(file_path)
        self.image_datas = [
            data for data in self.image_datas if data["file_name"] != file_path.split('/')[-1]]
        self.update_button_states()

    def save_base64_data(self):
        if self.image_datas:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json", filetypes=[("JSON Files", "*.json")])
            if file_path:
                with open(file_path, 'w') as file:
                    json.dump(self.image_datas, file, indent=4)
                print(f"Data saved to {file_path}.")
        else:
            print("No data to save.")


if __name__ == '__main__':
    app = ImageSelectorApp()
    app.mainloop()
