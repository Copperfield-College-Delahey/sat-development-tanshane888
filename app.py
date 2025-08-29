import customtkinter as ctk

class AppPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Top bar
        top_frame = ctk.CTkFrame(self, fg_color="grey", corner_radius=0)
        top_frame.pack(fill="x", padx=10, pady=(10, 0))

        logo = ctk.CTkLabel(top_frame, text="Pricespy", font=ctk.CTkFont(size=20,), text_color="black")
        logo.pack(side="left", padx=10)

        search_entry = ctk.CTkEntry(top_frame, width=400, placeholder_text="paste link")
        search_entry.pack(side="left", padx=20)

        # Product title
        name = ctk.CTkLabel(self, text="Product", font=ctk.CTkFont(size=24, weight="bold"))
        name.pack(anchor="w", padx=20, pady=(20, 10))

        # Product card frame
        card_frame = ctk.CTkFrame(self)
        card_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Sample product
        product = ("a", "3.00", "4.00")

        card = self.create_product_card(card_frame, *product)
        card.pack(padx=10, pady=10)

    def create_product_card(self, parent, title, price, avg_price):
        frame = ctk.CTkFrame(parent, width=370, height=280)
        frame.pack_propagate(False)

        img_placeholder = ctk.CTkLabel(frame, text="🖥️", font=ctk.CTkFont(size=70))
        img_placeholder.pack(pady=(5, 0))

        title_label = ctk.CTkLabel(frame, text=title, wraplength=180, font=ctk.CTkFont(size=12))
        title_label.pack(pady=(5, 0))

        price_label = ctk.CTkLabel(frame, text=price, font=ctk.CTkFont(size=14, weight="bold"))
        price_label.pack()

        avg_price_label = ctk.CTkLabel(frame, text=f"price avg: {avg_price}", font=ctk.CTkFont(size=11))
        avg_price_label.pack()

        # Switch to description page
        link_button = ctk.CTkButton(
            frame, 
            text="Link", 
            width=80, 
            command=lambda: self.controller.show_frame("DescriptionPage")
        )
        link_button.pack(pady=(5, 5))

        return frame
