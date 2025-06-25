import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Pricespy")
app.geometry("900x600")

# Top Bar
top_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=0)
top_frame.pack(fill="x", padx=10, pady=(10, 0))

#Logo 
logo = ctk.CTkLabel(top_frame, text="Pricespy", font=ctk.CTkFont(size=20, weight="bold"), text_color="#3B3B3B")
logo.pack(side="left", padx=10)

# Search bar
search_entry = ctk.CTkEntry(top_frame, width=500, placeholder_text="paste link")
search_entry.pack(side="left", padx=20)

#Product name
name = ctk.CTkLabel(app, text="Product List", font=ctk.CTkFont(size=24, weight="bold"))
name.pack(anchor="w", padx=20, pady=(20, 10))

#Product Card Layout 
card_frame = ctk.CTkFrame(app, fg_color="transparent")
card_frame.pack(fill="both", expand=True, padx=20)

# Sample product data (title, price, avg price)
products = [
    ("a","3.00","4.00"),
    ("b","3.00","4.00"),
    ("c","9.00","8.00"),
    ("d","5.00","9.00"),
    ("e","6.00","7.00"),
    ("f","7.50","3.00"),
    ("g","4.50","2.00"),
    ("h","9.99","4.00"),
    ("i","1.00","1.00")
]

# Function to create product cards
def create_product_card(parent, title, price, avg_price):
    frame = ctk.CTkFrame(parent, width=250, height=200, corner_radius=10)
    frame.pack_propagate(False)

    img_placeholder = ctk.CTkLabel(frame, text="🖥️", font=ctk.CTkFont(size=30))
    img_placeholder.pack(pady=(5, 0))

    title_label = ctk.CTkLabel(frame, text=title, wraplength=180, font=ctk.CTkFont(size=12))
    title_label.pack(pady=(5, 0))

    price_label = ctk.CTkLabel(frame, text=price, font=ctk.CTkFont(size=14, weight="bold"))
    price_label.pack()

    avg_price_label = ctk.CTkLabel(frame, text=f"price avg: {avg_price}", font=ctk.CTkFont(size=11))
    avg_price_label.pack()

    link_button = ctk.CTkButton(frame, text="Link", width=80)
    link_button.pack(pady=(5, 5))

    return frame

# Grid layout
for i in range(2):
    for j in range(3):
        idx = i * 3 + j
        card = create_product_card(card_frame, *products[idx])
        card.grid(row=i, column=j, padx=10, pady=10)

app.mainloop()
