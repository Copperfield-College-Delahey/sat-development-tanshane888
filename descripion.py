import customtkinter as ctk 

#app setup
app = ctk.CTk()
app.title("Pricespy")
app.geometry("1000x600")

#Top thing
top_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=0)
top_frame.pack(fill="x", padx=10, pady=(10, 0))

#Logo 
logo = ctk.CTkLabel(top_frame, text="Pricespy", font=ctk.CTkFont(size=20, weight="bold"), text_color="blue")
logo.pack(side="left", padx=10)

#Search bar
search_entry = ctk.CTkEntry(top_frame, width=500, placeholder_text="paste link")
search_entry.pack(side="left", padx=20)

#Product Card Layout 
card_frame = ctk.CTkFrame(app, fg_color="transparent")
card_frame.pack(fill="both", expand=True, padx=20)

#frame
frame = ctk.CTkFrame(app, fg_color="white", corner_radius=0)
frame.pack(fill="both", expand=True, padx = 20, pady = 10)

#wowww picturee
image = ctk.CTkLabel(
    frame,
    text="📷",
    font=ctk.CTkFont(size=100),
    text_color="black"
)
image.grid(row=0, column=0, rowspan=2, padx=20, sticky="n")

# Product Info
info_frame = ctk.CTkFrame(frame, fg_color="white")
info_frame.grid(row=0, column=1, sticky="nw")

title = ctk.CTkLabel(info_frame, text="Random Product Name XYZ", font=ctk.CTkFont(size=18, weight="bold"), text_color="black")
title.pack(anchor="w", pady=(0, 10))

details = {
    "Brand": "BrandX",
    "Special feature": "safe, flushable, cool"
}

for key, value in details.items():
    line = f"{key}: {value}"
    lbl = ctk.CTkLabel(info_frame, text=line, font=ctk.CTkFont(size=14), text_color="black")
    lbl.pack(anchor="w")

# Price Info Box
price_frame = ctk.CTkFrame(frame, fg_color="white", border_width=2, border_color="black", corner_radius=15)
price_frame.grid(row=0, column=2, padx=20, sticky="n")

price_label = ctk.CTkLabel(price_frame, text="$19.99", font=ctk.CTkFont(size=20, weight="bold"), text_color="green")
price_label.pack(pady=(10, 5))

avg_label = ctk.CTkLabel(price_frame, text="price avg: $21.50\n02/07/2025", font=ctk.CTkFont(size=12), text_color="gray")
avg_label.pack(pady=5)

link_button = ctk.CTkButton(price_frame, text="Link", width=100, fg_color="white", text_color="orange", border_color="orange", border_width=1, hover_color="#ffe6cc")
link_button.pack(pady=10)

app.mainloop()
