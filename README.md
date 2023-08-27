# UdemyProjects
9 projects from the "Django Masterclass" course

In order of appearance:

1. Web Based CV Generator opens a form that the user fills with data and returns (directly downloads) a pdf file with the result
- it needs wkhtmltopdf on your device in order the conversion to work (https://github.com/wkhtmltopdf/wkhtmltopdf)

2. Web Based Site Scraper that searches for link in format https://www.example.com and returns all valid links
- scraping is done via requests and beautiful soup
- all results are clickable and lead to a new tab with the results
- the "delete" button clears all records from the db
- bootstrap is used for the "design"
- custom form is used for the search bar in order to show appropriate errors in case of ivalid input

3. Food Menu App that shows a list of foods and their prices and also which user added the current item
- the models are connected by foreign key or OneToOneField
- the food model has CRUD funtionality
- used pillow to save images as files
- bootstrap for the design
- some class based views are used instead of FBV
- Signals used in order to connect the profile and the user models