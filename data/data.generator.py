import pandas as pd
import numpy as np

np.random.seed(42)

#Customers
customers = pd.DataFrame({
    "customer_id": range(1, 100001),
    "gender": np.random.choice(["Male", "Female"], 100000),
    "age": np.random.randint(18, 65, 100000),
    "region_id": np.random.randint(1, 5, 100000)
})

#Products
products = pd.DataFrame({
    "product_id": range(1, 201),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], 200),
    "price": np.random.randint(10, 500, 200)
})

#Orders
orders = pd.DataFrame({
    "order_id": range(1, 300001),
    "customer_id": np.random.randint(1, 100001, 300000),
    "total_amount": np.random.randint(20, 2000, 300000)
})

#Inventory
inventory = pd.DataFrame({
    "product_id": range(1, 201),
    "stock_quantity": np.random.randint(0, 1000, 200)
})

#Save samples (GitHub-friendly)
customers.sample(5000).to_csv("customers_sample.csv", index=False)
products.to_csv("products.csv", index=False)
orders.sample(5000).to_csv("orders_sample.csv", index=False)
inventory.to_csv("inventory.csv", index=False)

print("Sample datasets generated successfully.")