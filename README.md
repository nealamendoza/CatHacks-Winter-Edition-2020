# Cat Hacks
## Project: SafeSpace

### Kyle Java: Worked on the Front-End, Back-End, and Databases
### Neala Mendoza: Worked on the Front-End and designs of the website
### Anish Dhandore: Worked on the Front-End and Back-End

## Inspiration

The internet is a great place and resource for young kids and teens to learn all kinds of information, as well as learn about the events and news going around them. While it is true the internet is a great tool, there are many webpages that may be inappropriate for the younger audience. Our team wanted to build a website that would help make the internet a safer place. Many websites are filled with profanity and vulgar language that kids, teens, and students should not be exposed to.

## What it does

SafeSpace is a great website for identifying if a website is suitable for kids or not. The user will enter the URL of a website into our website scanner. Then, the website will scan for any profanity or vulgar language in the URL that the user provided. After scanning the URL, the scanner will return information about the website, and let the user know if it is safe for kids to view, if it contained any inappropriate words it would alert the user and tell them how many were found in the website. Finally, the URL and data would be imported to the database.

## How we built it

The Front-End was built using HTML, CSS, and the Bootstrap library. The Back-End was built with Python and Flask. For our database, to hold information, we used MongoDB.

## Challenges we ran into

Our team did not know how to use a database, it was not even in our original plan. We were inspired to use one after attending the Python Web Programming Workshop at CatHacks after learning about Redis. Our team tried to use Redis but it would not work for us, so we had to find a different solution.

## Accomplishments that we're proud of

One accomplishment we are proud of is developing a web scraping algorithm that would detect if a website contained any vulgar language, and counted how many inappropriate words there were in a website, if there were any present.

As mentioned before, none of us knew how to use a database and we struggled with Redis. So, we used another database called MongoDB. After watching several videos and reading through the documentation we were able to implement that in our program.

This leads to our other accomplishment, which was making the website faster. While we are proud of our web scraping algorithm, it was a little bit slow. It wasn't too noticeable but it did take a couple of seconds for the web scraper to go through the entire HTML file. We thought it would be faster to look up if the URL has been added to the database, that way we do not have to use the web scraping algorithm. If the URL was found in the database, the website would just return information about that URL, that way it does not need to go through our web scraping algorithm.  We would only use the web scraping algorithm if the URL was not in the database, and after using the web scraping function we would add that URL and its attributes.

## What we learned

We learned more about Beautiful Soup and what we can do with web scraping. We also strengthen our knowledge in Flask and Python. A big thing we all learned was how to use MongoDB, and learning how to send, delete, and retrieve data through Python.

## What's next for SafeSpace

Adding an AI that would detect if images in the website would be appropriate or not. Deciding if a website was appropriate or not by the text is a good start, but many webpages have images and videos all over them. So, it would be a great feature to detect if images in a website were suitable for the younger audience or not.
