
# ecommerce_data = [
#     {
#         "order_id": "O1001",
#         "customer_name": "Ravi Kumar",
#         "city": "Hyderabad",
#         "product": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 799,
#         "quantity": 2,
#         "total_amount": 1598,
#         "payment_method": "UPI",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1002",
#         "customer_name": "Sneha Reddy",
#         "city": "Bangalore",
#         "product": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1999,
#         "quantity": 1,
#         "total_amount": 1999,
#         "payment_method": "Credit Card",
#         "order_status": "Shipped"
#     },
#     {
#         "order_id": "O1003",
#         "customer_name": "Arjun Singh",
#         "city": "Mumbai",
#         "product": "Running Shoes",
#         "category": "Fashion",
#         "price": 2499,
#         "quantity": 1,
#         "total_amount": 2499,
#         "payment_method": "Cash on Delivery",
#         "order_status": "Processing"
#     },
#     {
#         "order_id": "O1004",
#         "customer_name": "Priya Sharma",
#         "city": "Delhi",
#         "product": "Smart Watch",
#         "category": "Electronics",
#         "price": 3499,
#         "quantity": 1,
#         "total_amount": 3499,
#         "payment_method": "Debit Card",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1005",
#         "customer_name": "Kiran Patel",
#         "city": "Chennai",
#         "product": "Laptop Backpack",
#         "category": "Accessories",
#         "price": 1299,
#         "quantity": 3,
#         "total_amount": 3897,
#         "payment_method": "UPI",
#         "order_status": "Shipped"
#     }
# ]

# #print customer names who is using UPI payment method 
# #print customer names who is purchasing quantity more than 1
# #print customer names who is purchasing other than electornics category

# for data in ecommerce_data:                             
#     if data['payment_method'] == 'UPI':
#         print(data['customer_name'], data['payment_method'])
#     if data['quantity'] > 1:
#         print(data['customer_name'], data['quantity'])
#     if data['category'] != 'Electronics':
#         print(data['customer_name'],data['category'])





def get_tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count
print(get_tuple_length((1, 2, 3, 4, 5)))


