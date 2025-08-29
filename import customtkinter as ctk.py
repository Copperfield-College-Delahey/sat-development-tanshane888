import customtkinter as ctk

# App setup
app = ctk.CTk()
app.title("Pricespy")
app.geometry("1920x1080")

# ─── Top Bar ─────────────────────────────────────────────
top_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=0)
top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)  # main content expands

# Logo
logo = ctk.CTkLabel(top_frame, text="Pricespy",
                    font=ctk.CTkFont(size=24), text_color="blue")
logo.pack(side="left", padx=20)

# Search bar
search_entry = ctk.CTkEntry(top_frame, width=500,
                            placeholder_text="paste link",
                            font=ctk.CTkFont(size=14))
search_entry.pack(side="left", padx=20)

# Navigation buttons
btn_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
btn_frame.pack(side="right", padx=20)
list_btn = ctk.CTkButton(btn_frame, text="Product List")
list_btn.pack(side="left", padx=5)
detail_btn = ctk.CTkButton(btn_frame, text="Product Detail")
detail_btn.pack(side="left", padx=5)

# ─── Page Container ─────────────────────────────────────────────
page_container = ctk.CTkFrame(app)
page_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
page_container.grid_rowconfigure(0, weight=1)
page_container.grid_columnconfigure(0, weight=1)

# ─── Page 1: Product Detail ─────────────────────────────────────
detail_page = ctk.CTkFrame(page_container)
detail_page.grid(row=0, column=0, sticky="nsew")

frame = ctk.CTkFrame(detail_page, height=400)
frame.pack(fill="both", expand=True, pady=10)

frame.grid_columnconfigure(1, weight=1)

# Product image
image = ctk.CTkLabel(frame, text="📷", font=ctk.CTkFont(size=150),
                     text_color="black", width=200, height=200)
image.grid(row=0, column=0, rowspan=2, padx=30, pady=30, sticky="n")

# Product Info
info_frame = ctk.CTkFrame(frame)
info_frame.grid(row=0, column=1, sticky="nw", padx=20, pady=30)

title = ctk.CTkLabel(info_frame, text="Random Product Name XYZ",
                     font=ctk.CTkFont(size=26, weight="bold"),
                     text_color="black")
title.pack(anchor="w", pady=(0, 20))

details = {"Brand": "BrandX", "Special feature": "safe, cool"}
for key, value in details.items():
    lbl = ctk.CTkLabel(info_frame, text=f"{key}: {value}",
                       font=ctk.CTkFont(size=16), text_color="black")
    lbl.pack(anchor="w", pady=4)

# Price Info Box
price_frame = ctk.CTkFrame(frame, fg_color="white", border_width=2,
                           border_color="green", corner_radius=15,
                           width=350, height=650)
price_frame.grid(row=0, column=2, padx=30, pady=30, sticky="n")

price_label = ctk.CTkLabel(price_frame, text="$19.99",
                           font=ctk.CTkFont(size=36, weight="bold"),
                           text_color="red")
price_label.pack(pady=(30, 10))

avg_label = ctk.CTkLabel(price_frame,
                         text="price avg: $21.50\n02/07/2025",
                         font=ctk.CTkFont(size=14), text_color="black")
avg_label.pack(pady=15)

link_button = ctk.CTkButton(price_frame, text="Link", width=150, height=50,
                            font=ctk.CTkFont(size=16), fg_color="red")
link_button.pack(pady=(15, 30))

# ─── Page 2: Product List (placeholder for now) ─────────────────
list_page = ctk.CTkFrame(page_container)
list_page.grid(row=0, column=0, sticky="nsew")

list_label = ctk.CTkLabel(list_page, text="Product List Page",
                          font=ctk.CTkFont(size=28, weight="bold"))
list_label.pack(pady=50)

# ─── Page Switching ───────────────────────────────────────────
frames = {"Detail": detail_page, "List": list_page}

def show_frame(name):
    frames[name].tkraise()

list_btn.configure(command=lambda: show_frame("List"))
detail_btn.configure(command=lambda: show_frame("Detail"))

# Show default page
show_frame("Detail")

app.mainloop()
