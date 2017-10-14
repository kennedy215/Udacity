import fresh_tomatoes
import media

demons = media.Movie("Demons",
                     "People were invited to a private screening only to be trapped in the theater",
                     "https://upload.wikimedia.org/wikipedia/en/2/2b/Demonsposter1986.jpg",
                     "https://youtu.be/PwX0hOpsuec"
                     )
return_of_the_living_dead = media.Movie("Return of the Living Dead",
                                        "Friends throw a party in the cemetary only to find a big surprise",
                                        "https://upload.wikimedia.org/wikipedia/en/3/3a/The_Return_of_the_Living_Dead_%28film%29.jpg",
                                        "https://youtu.be/KeSAFGWzft8")
night_of_the_demons = media.Movie("Night of the Demons",
                                  "college students throw a house party in an abandoned house only to find something sinister",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Night_of_the_Demons_poster.jpg",
                                  "https://youtu.be/XKzuj2eavtU")

killer_klowns_from_outer_space = media.Movie("Killer Klowns From Outter Space",
                               "Invasion of Klowns from Space",
                               "https://upload.wikimedia.org/wikipedia/en/7/7e/Killer_Klowns_from_Outer_Space_%281988%29_poster.jpg",
                               "https://youtu.be/cVQ3AGzeB_0")

movies = [demons,return_of_the_living_dead,night_of_the_demons,killer_klowns_from_outer_space]
fresh_tomatoes.open_movies_page(movies)
