import customtkinter as ctk 
class AddPage(ctk.CTkFrame): 
     def __init__(self, parent, controller=None): 
         super().__init__(parent) 

         #gui thingy
         
        search_entry = ctk.CTkEntry(top_bar, width=400, height=35, placeholder_text="paste link")
        search_entry.pack(side="left", padx=(10, 10), pady=10)

        search_button = ctk.CTkButton(top_bar, text="🔍", width=40)
        search_button.pack(side="left", pady=10)

        # Content Frame
        content_frame = ctk.CTkFrame(app, fg_color="white")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Left - Image placeholder
        image_label = ctk.CTkLabel(content_frame, text="🧻", font=ctk.CTkFont(size=100))
        image_label.grid(row=0, column=0, padx=20, sticky="n")

        # Middle - Product Info
        product_text = (
    "Quilton 3-Ply Toilet Tissue 48 Pack\n(1 x 48 Rolls)\n\n"
    "Brand: Quilton\n"
    "Special feature: septic_safe, flushable, embossed\n"
    "Unit count: 48 Count\n"
    "Sheet count: 180\n"
    "Ply rating: 3-Ply\n"
    "Material feature: Biodegradable\n"
    "Colour: White\n"
    "Scent: Unscented\n"
    "Item form: Roll with Sheets\n"
    "Size: 48 count"
)
        info_label = ctk.CTkLabel(content_frame, text=product_text, justify="left", font=ctk.CTkFont(size=14))
        info_label.grid(row=0, column=1, padx=20, sticky="nw")

        # Right - Price box
        price_box = ctk.CTkFrame(content_frame, width=200, height=200, corner_radius=15)
        price_box.grid(row=0, column=2, padx=20, sticky="ne")
        price_box.pack_propagate(False)

        price_label = ctk.CTkLabel(price_box, text="$21.60", font=ctk.CTkFont(size=18, weight="bold"))
        price_label.pack(pady=(15, 5))

        avg_label = ctk.CTkLabel(price_box, text="price avg: $22.30", font=ctk.CTkFont(size=12))
        avg_label.pack()

        date_label = ctk.CTkLabel(price_box, text="11/06/2025", font=ctk.CTkFont(size=12))
        date_label.pack(pady=(0, 10))

        def open_link():
         webbrowser.open("https://example.com/product")

        link_button = ctk.CTkButton(price_box, text="Link", width=120, command=open_link)
        link_button.pack(pady=(0, 10))

app.mainloop()

         
