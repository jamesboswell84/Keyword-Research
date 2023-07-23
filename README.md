# Keyword Categoriser

## Introduction

- This script helps with keyword categorisation by automatically adding pre-defined categories into your keyword data
- For the pre-defined categories, it supports using Google Keyword Planner's "Refine keywords" feature, which uses machine learning to find entities and modifiers e.g. brands, products, types, conditions and more
- Unfortunately, Google's machine learning can't identify every entity or modifier, but it can pull out some categories for about 80% of your keywords, so it will save you lots of time

## Instructions

For your first run, you need a csv file with your categories, and a good headstart here is to 'scrape' the categories from Google Keyword Planner's "Refine keywords" panel. These instructions will tell you how to do this:
- Download and install the Table Capture Chrome extension
- Go to Keyword Planner > Discover new keywords and enter up to 10 root keywords, to get your keyword ideas
- In the keyword ideas window, you should see the "Refine keywords" panel on the right. Use this to remove unwanted keywords e.g. brands. Then change your date dropdown to "All available" (why not get more data if it's available). Then download it as csv
- While still keeping your keyword ideas window open, go to the "Refine keywords" panel again, make sure you click "Expand all", then scroll down your refine keywords list and click all of the "VIEW X MORE" links to ensure all possible options are visible in the panel
- Right-click on the top category heading text (usually this is "Brand or Non-Brand") and launch the Table Capture workshop (Table Capture > Table Capture - Launch workshop). You should see the workshop panel appear across the bottom of the screen and the category heading (probably "Brand or Non-Brand") has been highlighted.
- Click 6 times on the "Select parent element" (left-hand side of the workshop) button. The Preview Data table should show your categories (e.g. Brand or Non-Brand, Product, Color, Type etc) down the left column. 
- Click the "Break columns" link (right-hand side of the workshop, to the right of where it says "Preview Data")
- Click the "Copy table data to the clipboard"
- Paste the data into Excel and then save as csv
- Upload the categories csv file as requested
- Upload your keyword data csv file as requested
- Download your categorised keywords!
- OPTIONAL: Download your categories (allows you to manually add categories to it then re-upload to update your keyword data)

## How it works

- The script tidies up the categories csv (Table Capture copy of the Keyword Planner "Refine keywords" panel is a mess)
- It then iterates through category columns, turning them into separate lists of entities and modifiers
- For each category, it then extracts the entities/modifiers from the Keyword column in the keyword data into a new column for that category
