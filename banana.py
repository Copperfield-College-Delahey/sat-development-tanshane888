import customtkinter as ctk 

#app setup
app = ctk.CTk()
app.title("Pricespy")
app.geometry("1920x1080")

#Top thing
top_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=0)
top_frame.pack(fill="x", padx=10, pady=(10, 0))

#Logo 
logo = ctk.CTkLabel(top_frame, text="Pricespy", font=ctk.CTkFont(size=24, weight="bold"), text_color="#1f538d")
logo.pack(side="left", padx=20)

#Search bar
search_entry = ctk.CTkEntry(top_frame, width=500, placeholder_text="paste link", font=ctk.CTkFont(size=14))
search_entry.pack(side="left", padx=20)

#Main content frame (removed duplicate card_frame)
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

#Product card frame
frame = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=15, height=400)
frame.pack(fill="both", expand=True, pady=10)

# Configure grid weights
frame.grid_columnconfigure(1, weight=1)

#Product image
image = ctk.CTkLabel(
    frame,
    text="📷",
    font=ctk.CTkFont(size=150),
    text_color="#666666",
    width=200,
    height=200
)
image.grid(row=0, column=0, rowspan=2, padx=30, pady=30, sticky="n")

# Product Info
info_frame = ctk.CTkFrame(frame, fg_color="transparent")
info_frame.grid(row=0, column=1, sticky="nw", padx=20, pady=30)

title = ctk.CTkLabel(info_frame, text="Random Product Name XYZ", font=ctk.CTkFont(size=26, weight="bold"), text_color="black")
title.pack(anchor="w", pady=(0, 20))

details = {
    "Brand": "BrandX",
    "Special feature": "safe, flushable, cool"
}

for key, value in details.items():
    line = f"{key}: {value}"
    lbl = ctk.CTkLabel(info_frame, text=line, font=ctk.CTkFont(size=16), text_color="#555555")
    lbl.pack(anchor="w", pady=4)

# Price Info Box
price_frame = ctk.CTkFrame(frame, fg_color="white", border_width=2, border_color="#1f538d", corner_radius=15, width=350, height=650)
price_frame.grid(row=0, column=2, padx=30, pady=30, sticky="n")

price_label = ctk.CTkLabel(price_frame, text="$19.99", font=ctk.CTkFont(size=36, weight="bold"), text_color="#00AA00")
price_label.pack(pady=(30, 10))

avg_label = ctk.CTkLabel(price_frame, text="price avg: $21.50\n02/07/2025", font=ctk.CTkFont(size=14), text_color="#666666")
avg_label.pack(pady=15)

link_button = ctk.CTkButton(price_frame, text="Link", width=150, height=50, font=ctk.CTkFont(size=16, weight="bold"), fg_color="#FF6B35", hover_color="#E55A2B")
link_button.pack(pady=(15, 30))

app.mainloop()