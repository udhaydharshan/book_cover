# Ex.06 Book Front Cover Page Design
# Date:13.12.2025
# AIM:
To design a book front cover page using HTML and CSS.

# DESIGN STEPS:
## Step 1:
Create a Django Admin project.

## Step 2:
Create an app in the Django interface.

## Step 3:
Create a folder named 'static' in the app folder.

## Step 4:
Create a new HTML file in the static folder.

## Step 5:
Write the HTML code with relevant CSS properties.

## Step 6:
Choose the appropriate style and color scheme.

## Step 7:
Insert the images in their appropriate places.

## Step 8:
Publish the website in the LocalHost.

# PROGRAM:
views.py
```
from django.shortcuts import render


def fp(request):
    return render(request, 'cover/fp.html')
```
urls.py
```
from django.contrib import admin
from django.urls import path
from cover import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fp, name='home'),
]
```
fp.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Quest Through Uncharted Realms</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: "Georgia", serif;
            background: floralwhite;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        .book-container {
            width: 420px;
            height: 600px;
            padding: 20px;
            position: relative;
            color: white;
            background-color: white;
            background-image: url("{% static 'images/bookbg.png' %}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            

        }


        .top-title {
            font-size: 14px;
            font-weight: bold;
        }

        .main-title {
            font-size: 28px;
            font-weight: 900;
            text-align: center;
            margin-top: 80px;
            line-height: 1.3;
        }

        .sub-text {
            text-align: center;
            font-size: 14px;
            margin-top: 10px;
        }

        .special-edition {
            font-size: 16px;
            font-weight: bold;
            margin-top: 239px;
        }

        .authors {
            width: 100%;
            position: absolute;
            bottom: 15px;
            left: 0;
            font-size: 15px;
            font-weight: bold;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
        }

        .top {
            border: 0;
            height: 2px;
            background-color: white;
            margin-top: 10px;
            position: absolute;
            width: 39%;
            left: 10px;
        }

        .inner-border {
            position: absolute;
            top: 10px;
            left: 10px;
            right: 10px;
            bottom: 10px;
            border: 3px solid #f3efef;
            pointer-events: none;
        }

        .photo-box {
            position: absolute;
            right: 20px;
            bottom: 30px;
            width: 120px;
            height: 120px;
            border: 2px solid #fff;
            background: #fff;
        }

        .photo-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>

</head>

<body>

    <div class="book-container">
        <div class="inner-border"></div>

        <div class="top-title">NATURE</div>

        <div class="main-title">Quest Through Uncharted Realms</div>

        <div class="sub-text">The Complete Expeditionary Notes of a World Traveler</div>

        <div class="special-edition">Collector's Edition</div>
        <hr class="top">

        <div class="photo-box"><img src="{% static 'images/photo.png' %}" alt="Author"></div>

        <div class="authors">
            <span>Neil Gaiman</span>
        </div>

    </div>

</body>

</html>
```
# OUTPUT:
![alt text](<Screenshot 2025-12-13 103108.png>)
# RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
