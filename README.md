Inventory Management System (Python Tkinter)
Overview
A GUI‑based Inventory Management System built with Python’s Tkinter library. It enables users to manage product records efficiently, including adding, viewing, searching, deleting, extracting items, and counting total products. The system is lightweight, user‑friendly, and suitable for small to medium inventory tasks.

Features
Add Product with validation for ID, price, and quantity

View Products in a formatted listbox

Search Product by ID with detailed information

Delete Product from the system

Extract Item to reduce stock quantity

Count Products to display total product count

Clear Fields for fresh input

Technology Stack
Python 3.x

Tkinter (GUI framework)

Messagebox for notifications

Project Structure
Product Class: Defines product attributes (ID, name, category, price, quantity)

Functions:

add_product() → Adds new product

view_products() → Displays product list

search_product() → Finds product by ID

delete_product() → Removes product record

extract_product() → Deducts stock quantity

count_products() → Shows total product count

clear_fields() → Clears input fields

Main Window: Tkinter GUI with labels, entry fields, buttons, and a listbox

User Interface
Title: Inventory Management System

Input Fields: Product ID, Name, Category, Price, Quantity, Extract Quantity

Buttons: Add Product, View Products, Search Product, Delete Product, Extract Item, Clear Fields, Count Products

Listbox: Displays product records in tabular format

Usage
Run the script with Python 3

Enter product details in the input fields

Use buttons to perform operations

View results in the listbox or message pop‑ups

Future Enhancements
Persistent storage using JSON or SQLite

Advanced search and filtering options

Export inventory data to CSV/Excel

Role‑based access with authentication
