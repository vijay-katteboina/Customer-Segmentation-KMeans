"""
==========================================================
Customer Segmentation using K-Means Clustering

Author  : Vijay Katteboina
Course  : Master of Computer Applications (MCA)
College : Loyola Academy Degree & PG College

Description:
This desktop application predicts the customer cluster
using a trained K-Means Machine Learning model.
==========================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
from predict import predict_customer

# ==========================
# Create Main Window
# ==========================

root = tk.Tk()
root.title("Customer Segmentation using K-Means")
root.geometry("650x850")
root.resizable(False, False)
root.configure(bg="#F5F5F5")

# ==========================
# Title
# ==========================

title = tk.Label(
    root,
    text="Customer Segmentation using K-Means",
    font=("Arial", 22, "bold"),
    fg="#003366",
    bg="#F5F5F5"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Machine Learning Project using K-Means Clustering",
    font=("Arial", 12),
    fg="gray",
    bg="#F5F5F5"
)
subtitle.pack()

info = tk.Label(
    root,
    text="Dataset : Mall Customer Segmentation Dataset\nAlgorithm : K-Means Clustering",
    font=("Arial",10),
    fg="gray",
    bg="#F5F5F5",
    justify="center"
)
info.pack(pady=10)

# ==========================
# Gender
# ==========================

tk.Label(
    root,
    text="Gender",
    font=("Arial", 12, "bold"),
    bg="#F5F5F5"
).pack(pady=(20,5))

gender = ttk.Combobox(
    root,
    values=["Male", "Female"],
    state="readonly",
    width=30
)

gender.current(0)
gender.pack()

# ==========================
# Age
# ==========================

tk.Label(
    root,
    text="Age",
    font=("Arial",12,"bold"),
    bg="#F5F5F5"
).pack(pady=(15,5))

age = tk.Entry(root, width=35)
age.pack()

# ==========================
# Annual Income
# ==========================

tk.Label(
    root,
    text="Annual Income (k$)",
    font=("Arial",12,"bold"),
    bg="#F5F5F5"
).pack(pady=(15,5))

income = tk.Entry(root, width=35)
income.pack()

# ==========================
# Spending Score
# ==========================

tk.Label(
    root,
    text="Spending Score (1-100)",
    font=("Arial",12,"bold"),
    bg="#F5F5F5"
).pack(pady=(15,5))

score = tk.Entry(root, width=35)
score.pack()
age.focus()
# ==========================
# Prediction Function
# ==========================

def predict():

    try:

        g = gender.get()
        a = int(age.get())
        i = int(income.get())
        s = int(score.get())

        # ---------------- Validation ----------------

        if a <= 0:
            messagebox.showerror(
                "Invalid Age",
                "Age must be greater than 0."
            )
            return

        if i <= 0:
            messagebox.showerror(
                "Invalid Income",
                "Income must be greater than 0."
            )
            return

        if s < 1 or s > 100:
            messagebox.showerror(
                "Invalid Spending Score",
                "Spending Score must be between 1 and 100."
            )
            return

        # -------- Predict Cluster --------

        cluster = predict_customer(g, a, i, s)

        # -------- Customer Details --------

        customer_info = {

            0: (
                "Careful Customers",
                "Offer personalized discounts and loyalty rewards."
            ),
            1: (
                "Standard Customers",
                "Recommend regular offers and seasonal promotions."
            ),
            2: (
                "Target Customers",
                "Promote premium products and exclusive memberships."
            ),
            3: (
                "High Value Customers",
                "Provide VIP benefits and premium services."
            ),
            4: (
                "Budget Customers",
                "Offer affordable products and discount coupons."
            )
        }

        customer_type, recommendation = customer_info.get(
            cluster,
            ("Unknown", "No recommendation available.")
        )

        result.config(

        text=f"""
        ✅ Prediction Successful

        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        Cluster Number : {cluster}

        Customer Type :
        {customer_type}

        Recommendation :
        {recommendation}

        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """,

            fg="#006400"

        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter only numeric values."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# ==========================
# Clear Function
# ==========================

def clear():

    gender.current(0)
    age.delete(0, tk.END)
    income.delete(0, tk.END)
    score.delete(0, tk.END)

    result.config(
        text="Prediction result will appear here.",
        fg="gray"
    )

# Press Enter to Predict
root.bind("<Return>", lambda event: predict())

# ==========================
# Buttons
# ==========================

button_frame = tk.Frame(root,bg="#F5F5F5")
button_frame.pack(pady=15)

predict_btn = tk.Button(

    button_frame,
    text="Predict",
    font=("Arial",13,"bold"),
    width=12,
    bg="green",
    fg="white",
    command=predict

)

predict_btn.grid(row=0,column=0,padx=10)

clear_btn = tk.Button(

    button_frame,
    text="Clear",
    font=("Arial",13,"bold"),
    width=12,
    bg="red",
    fg="white",
    command=clear
)

clear_btn.grid(row=0,column=1,padx=10)

# ==========================
# Separator
# ==========================

tk.Label(
    root,
    text="════════════════════════════════════════════════════",
    font=("Arial",10),
    bg="#F5F5F5",
    fg="gray"
).pack(pady=5)

# ==========================
# Result
# ==========================

result = tk.Label(
    root,
    text="Prediction result will appear here.",
    font=("Arial",14,"bold"),
    bg="#F5F5F5",
    fg="gray",
    justify="center"
)

result.pack(pady=10)

# ==========================
# Footer
# ==========================

tk.Label(
    root,
    text="────────────────────────────────────────────────────────",
    font=("Arial",10),
    bg="#F5F5F5",
    fg="gray"
).pack(pady=5)

footer = tk.Label(
    root,
    text="Developed by Vijay Katteboina\nMCA Department | Loyola Academy Degree & PG College",
    font=("Arial",10,"italic"),
    bg="#F5F5F5",
    fg="#555555",
    justify="center"
)

footer.pack(pady=10)

# ==========================
# Run Window
# ==========================
def on_close():
    if messagebox.askyesno(
        "Exit",
        "Do you want to exit the application?"
    ):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()