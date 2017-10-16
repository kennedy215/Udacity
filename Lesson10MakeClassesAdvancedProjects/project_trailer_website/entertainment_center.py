import webbrowser
import fresh_tomatoes
import mediab

#   List of movies on the Horroday list

night_of_the_demons = mediab.Movie("Night of the Demons",
                                   "College students throw a Halloween party in an abandoned house only to receive a nice treat!",
                                   "https://upload.wikimedia.org/wikipedia/en/a/ac/Night_of_the_Demons_poster.jpg",
                                   "https://youtu.be/XKzuj2eavtU")
pet_semetary = mediab.Movie("Pet Semetary",
                     "Father loses his son and brings him back from the dead. But is it his son?",
                     "https://upload.wikimedia.org/wikipedia/en/7/75/Pet_sematary_poster.jpg",
                     "https://youtu.be/jpjpUOXQZac")

stranger_things = mediab.Series("Stranger Things",
                               "A kid is missing and his friends discover it's because of a secret government project",
                               "http://vignette1.wikia.nocookie.net/strangerthings8338/images/0/09/Stranger_Things_Season_1.png/revision/latest?cb=20160814211924",
                               "https://youtu.be/b9EkMc79ZSU",
                                "Season 1",
                                "Episode 2")

tales_from_the_crypt = mediab.Series("Tales from the Crypt",
                                     "Terror tales from the Crypt Keeper",
                                     "https://images-na.ssl-images-amazon.com/images/I/91faByZU8OL._SL1500_.jpg",
                                     "https://youtu.be/IvpT9J7ZVOM",
                                     "Season 1",
                                     "Episode 2")
tales_from_the_darkside = mediab.Series("Tales from the Darkside",
                                        "Tales from the DARK SIDE",
                                        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/5577/5577347_sa.jpg;maxHeight=550;maxWidth=642",
                                        "https://youtu.be/QvIJFgG3sWE",
                                        "Season 1",
                                        "Episode 1"
                                        )

nightmare_on_elmstreet = mediab.Movie("Nightmare on Elmstreet",
                                      "A serial killer exacts revenge on the children of the parents that killed him",
                                      "https://upload.wikimedia.org/wikipedia/en/f/fa/A_Nightmare_on_Elm_Street_%281984%29_theatrical_poster.jpg",
                                      "https://youtu.be/dCVh4lBfW-c")

demons = mediab.Movie("Demons",
                      "People are invited to see a movie premiere named,'Demons'only to find out it isn't a movie!",
                      "https://upload.wikimedia.org/wikipedia/en/2/2b/Demonsposter1986.jpg",
                      "https://youtu.be/PwX0hOpsuec")
deathgasm = mediab.Movie("Deathgasm",
                        "Nerds, Heavy Metal and cursed music that brings about demons creates? A bad ass movie!",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/Deathgasm-poster.jpg",
                        "https://youtu.be/Cg-c7UpJZLQ")
childs_play = mediab.Movie("Child's Play",
                           "A boy's good guy doll is possessed by a dead serial killer",
                           "https://images-na.ssl-images-amazon.com/images/I/719AMX2PRKL._SY445_.gif",
                           "https://youtu.be/sjiyV8mtXiU")

return_of_the_living_dead = mediab.Movie("Return of the Living Dead",
                                         "Young and bored a group of friends decides to throw a part in the cemetary only to find out the dead is rising!",
                                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYzY0ZjJlNmMtMGU3NC00Yjk3LTk0N2ItMDNlMDVhZjA4OTFmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                         "https://youtu.be/KeSAFGWzft8")                                 
#   Sends the array to the fresh_tomatoes.py file to be displayed
movies = [night_of_the_demons, pet_semetary, stranger_things, tales_from_the_crypt, tales_from_the_darkside, nightmare_on_elmstreet, demons, deathgasm, childs_play, return_of_the_living_dead]
fresh_tomatoes.open_movies_page(movies)

#   Generates a list of information about the movies presented on the page
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

