import customtkinter as ctk
from app import AppPage
from descripion import DescriptionPage

class PricespyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pricespy - Multi Page")
        self.geometry("1920x1080")

        # Container for all pages
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary of pages
        self.frames = {}

        for F in (AppPage, DescriptionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AppPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = PricespyApp()
    app.mainloop()
