## Fresh Tomatoes - Top 10 Horrorday Halloween Movies

This program features the **top 10 horror movies** that are perfect for October.
This template also gives you the ability to create you own list!


## How It Works

To see the generated list all you do is open fresh_tomatoes.html in your browser!
If you'd like add your own list read the directions below.

    *the website's fresh tomatoes template was provided by [Udacity](www.Udacity.com))*


## Requirements

You must have python 2.7 installed. For further instructions please click [here](https://www.python.org/download/releases/2.7/)

## Directions

### How to Run Application

**Step 1:** Using Terminal:
Type `python entertainment_center.py`

**Step 2:** Using the Python IDLE:
Select Run from the IDLE menu,
Click `Run Module` from the dropdown list


### How to Modify Application

**Directions** to add a _movie_:

**Step 1:** Open entertainment_center.py. This is how you change the movie.

Change `night_of_the_demons` to a movie or tv show you'd like to add into the list. Be sure to keep
it lower case and seperate the different words with an underscore.

**Step 2:** If you want to add a movie Be sure not to change this code: `= mediab.Movie`. If you'd like to make a TV show then change `= mediab.Movie` into `= mediab.Series` Also, write in between the ""(quotes)
line 1 represents the movie _title_ so Change `"Night of the Demons",` to the movie title you desire.
line 2 is the _story line_ So change the story line.
line 3 is the link to the picture of the poster work. Goto google and google the name of the movie on wiki movie. Then click in the wiki movie website and click on the poster. copy the url when your clicked into the image. paste the url between the quotes of the 3rd line.
`"https://upload.wikimedia.org/wikipedia/en/a/ac/Night_of_the_Demons_poster.jpg",`
line 4 goto YouTube search for your chosen movie's trailer and copy and paste the code between the quotes.

```
night_of_the_demons = mediab.Movie("Night of the Demons",
                                   "College students throw a Halloween party in an abandoned house only to receive a nice treat!",
                                   "https://upload.wikimedia.org/wikipedia/en/a/ac/Night_of_the_Demons_poster.jpg",
                                   "https://youtu.be/XKzuj2eavtU")
```

If you are adding a TV show you have to add line 5 and 6.

Line 5 is Season so you have to write `Season 1` the corosponding number must be the season that
pertains to the season of your show.
Line 6 is the Episode you have to write 'Episode 1' the corosponding number must be the season that
pertains to your show.
**Step 3**

Go into the array and switch out night_of_the_demons with the following name of your movie. Make sure you write it exactly how you wrote it. For example `night_of_the_demons =`
```
movies = [night_of_the_demons, pet_semetary, stranger_things, tales_from_the_crypt, tales_from_the_darkside, nightmare_on_elmstreet, demons, deathgasm, childs_play, return_of_the_living_dead]
fresh_tomatoes.open_movies_page(movies)
```

**Step 4**

Replace `night_of_the_demons.show_info()` with the exact name you gave the movie! So `your_movie.show_info()`

```
night_of_the_demons.show_info()
pet_semetary.show_info()
stranger_things.show_info()
tales_from_the_crypt
tales_from_the_darkside.show_info()
nightmare_on_elmstreet.show_info()
demons.show_info()
deathgasm.show_info()
childs_play.show_info()
return_of_the_living_dead.show_info()
```
Afterwards your finished! Run the code and you'll see your new list generate! If you want to
change the other titles repeat the steps given on a different movie in the list!


## Liscence

### MIT License

Copyright (c) 2017 Kennedy.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
