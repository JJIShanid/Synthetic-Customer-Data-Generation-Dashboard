# Synthetic-Customer-Data-Generation-Dashboard
## 📌 Project Overview
This project demonstrates **GAN-based synthetic data generation** for customer analytics and a **Streamlit dashboard** to visualize the generated dataset.  
It ensures **data privacy** while enabling businesses to train models, test dashboards, and analyze patterns without using real customer data.

---
<img width="1910" height="972" alt="p1" src="https://github.com/user-attachments/assets/5349ca5b-729c-4472-ad69-49ab33e5f6e8" />

## ✅ Key Features
✔ **Generative AI with GAN** – Creates realistic, privacy-safe synthetic customer data.  
✔ **Customizable Data** – Similar structure to real telecom churn datasets.  
✔ **Interactive Streamlit Dashboard** – Visual storytelling with:  
   - Data preview & summary  
   - Exploratory Data Analysis (EDA) visuals  
   - Correlation heatmap  
✔ **Download Option** – Export synthetic dataset in CSV format.  

---
<img width="1913" height="959" alt="p2" src="https://github.com/user-attachments/assets/eafbae27-0f48-432b-8025-e04e1405cc79" />

## 🛠 Tech Stack
- **Python 3.9+**
- **PyTorch** – For GAN model training
- **Pandas & NumPy** – Data handling
- **Matplotlib & Seaborn** – Visualization
- **Streamlit** – Interactive dashboard

---

## 📂 Project Structure
Gen Ai Analytics/
│
├── data/
│ └── synthetic_customer_data.csv # Generated dataset
├── models/
│ ├── gan_generator.pth # Saved GAN generator
│ └── gan_discriminator.pth # Saved GAN discriminator
├── notebooks/
│ └── gan_customer_data.ipynb # GAN training & data generation
├── dashboard/
│ └── app.py # Streamlit dashboard
└── README.md # Project documentation

yaml
Copy code

---

## ⚡ How It Works
1. **Train GAN Model** → Generates synthetic customer data.
2. **Save Generated Dataset** → Stored as `synthetic_customer_data.csv`.
3. **Launch Streamlit Dashboard** → Visualize & download synthetic data.

---

## ▶ Run the Dashboard
```bash
cd "C:\Users\asus\Desktop\Masters Project & Thesis\Master Projects\Gen Ai Analytics\dashboard"
streamlit run app.py
Author

Ishan
MSc Data Science – Business Analytics | SRH University, Germany
