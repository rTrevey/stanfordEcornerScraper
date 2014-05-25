README
####
stanfordEcorner.py is a class used for scraping lectures from the Stanford Entrepreneurship Corner website.  
It takes a url of a lecture (from the website) and returns an object with:
-Date
-Title
-Speaker
-Organization they are from
-And a True/False value depending on whether subitles/transcripts are available
-A method which returns the transcripts as a string

This could be used to create a database if iterated over a list of lectures, etc.
