**[Warning] The tool is no longer fully functional due to new security measures implemented by Willhaben. With my API reader you can bypass this, but I currently don't have the time to implement it.**

# Willhaben Grabber
> This is a simple grabber written in Python which helps you to grab products from Willhaben.at

## General info
The tool generates a search link based on user input and filters the number of possible products from the results page.Afterwards you enter a number of products to be grabbed and the tool creates a results folder and grabs the products. For each product the title, price, description, location and all images are downloaded. Additionally all images will be cropped and all metadata will be deleted.

## Technologies
* Used Python Version: Python 3.7
* Used Libarys: os, sys, random, time, colorama, bs4, PIL, math 

## Setup
To install all requiered Libarys use following commands:
* `pip install -r requirements.txt`

## Code Examples
Example of usage:
`python3 Willhaben_Grabber.py`

## Inspiration
I started the project out of boredom. If you have suggestions for improvement feel free to contact me!

## Contact
Created by [@Ramy-Zemo](https://github.com/ramy-zemo)
Discord: Ramo#1337
