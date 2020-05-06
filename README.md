

# CycleOlogy - Milestone Project 4
***

## Table of Contents

 * List item
 *	Fuctionality of the Project
 *	User Experience 
	 *	User Stories
	 *	Design 
	 *	Wireframes
*	Technology Used 
*	Database
*	Features 
*	Testing 
*	Deployment 
*	Credits 

***
## Welcome to CycleOlogy 

![enter image description here](https://cycleology.s3-eu-west-1.amazonaws.com/media/images/LOGO-SMALL.jpg)

***
## User Experience

### User Stories

#### Public User
-	As a public user, I want to be able to view all products on any device (mobile / tablet / desktop)
-	As a public user, I want to be able to pick a product category
-	As a public user, I want to be able to pick a product from a subcategory
-	As a public user, I want to be able to search for a product
-	As a public user, I want to be able to get more information on a product
-	As a public user, I want to be able to add a product to my shopping cart
-	As a public user, I want to be able to add a quantity of the same item
-	As a public user, I want to be able view my shopping cart
-	As a public user, I want to be able to adjust the quantity in my shopping cart for a specific product
-	As a public user, I want to be able to delete an item in my shopping cart.
-	As a public user I want the able to purchase the items in my shopping cart
-	As a public user I want to be able to register as a user
-	As a public user, I want to be able to change my password
-	As a public user, I want to be able to send the company a message

#### Administer User

 - As a Administer User, I want to be able to add products
 - As a Administer User, I want to be able to delete products
 - As a Administer User, I want to be able to modify products
 - As a Administer User, I want to be able to view orders
 - As a Administer User, I want public to register

#### Developer User

 - As a Developer User, I want site to be secure
 - As a Developer User, I want site to be responsive
 - As a Developer User, I want to be error free
 - As a Developer User, I want to build a website that is scalable and that can be enhanced with further development

### Strategy

### Scope

The scope of the site was to provide a ecommerce website for a new up and coming cycle shop, and to demonstrate the skills that I learnt on the Coding Institute Full Stack Developers course, HTML, CSS, JQuery, Python, Django python,

### Structure

The Navigation bar is fixed to the top of the screen so that it’s available at all times.

The shopping cart is always visible and accessible for the user, so there is a different CSS for mobile views so that it doesn’t collapse into the mobile nav icon.

The user can select all products, or refine their query using the categories or subcategories

The search functionally allows a user to search within the name and display all products that match.

The page restricts the amount of products to 6 and there is pagination functionality to allow the user to scan through the products on other pages.

The product details page allows to user to view more information on the product

The shopping cart page allows the user to adjust / delete items and also proceed to checkout. To enhance user experience I have removed the table slider on mobile views, instead I have modified the form so that its only contains the necessary information

The checkout page allows the user to enter in their name and address for delivery, and also make a credit card payment.

The contact page allows the user to enter a message for the administrator of the website

The footer contains links to all social media

## Technology Used
###	Languages, Frameworks, Editors, Version Control

 - HTML, CSS, JS and Python 
 - Django 
 - Bootstrap Framework
 - GitHub Used to store the repository, keep version control, and push link to Heroko 
 - Heroku 

### Tools Used
- Balsamiq Used to create wireframes
- W3C HTML Validator used to check HTML code
- W3C CSS Validator used to check CSS code
- htmlformatter.com used to beautify the HTML code
- Font Awesome Icons
- Favicon Generator
- Google Chrome DevTools
- AWS Amazon
- Stripe

## Database

#### Product Details 

|Name                | Format     | 
| ------------------ | --------------- | 
|catagory | models.CharField(max_length=254, choices=PRODUCT_CATAGORY) |
|subcatagory | models.CharField(max_length=254, choices=PRODUCT_SUBCATAGORY) |
|name | models.CharField(max_length=254, default='') |
|product_summary | models.TextField(default='') |
|product_description|models.TextField(null = True, blank=True)|
|product_features|models.TextField(null = True, blank=True)|
|price|models.DecimalField(max_digits=6, decimal_places=2)|
|image1|models.ImageField(upload_to='images',null = True, blank=True)|
|image2|models.ImageField(upload_to='images',null = True, blank=True)|
|image3|models.ImageField(upload_to='images',null = True, blank=True)|


#### Checkout Order

|Name                | Format     | 
| ------------------ | --------------- | 
|full_name  |models.CharField(max_length=50, blank=False)|
|phone_number  |models.CharField(max_length=20, blank=False)|
|country |models.CharField(max_length=40, blank=False)|
|postcode |models.CharField(max_length=20, blank=True)|
|town_or_city |models.CharField(max_length=40, blank=False)|
|street_address1 |models.CharField(max_length=40, blank=False)|
|street_address2 |models.CharField(max_length=40, blank=False)|
|county|models.CharField(max_length=40, blank=False)|
|date|models.DateField()|


#### Order item
|Name                | Format     | 
| ------------------ | --------------- | 
|order   |models.ForeignKey(Order, null=False)|
|product   |models.ForeignKey(Product, null=False)|
|quantity |models.IntegerField(blank=False)|


## Testing

|Fuctionality               | Page    | User Type | Browser | Pass / Fail | Comments |
| ----| ---- | ---- |  ---- | ---- | ---- |
| a |  b | c  | d  |  e |  f |