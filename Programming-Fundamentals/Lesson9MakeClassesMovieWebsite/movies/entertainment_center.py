import fresh_tomatoes
import media 

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/tN1A2mVnrOM")
avatar = media.Movie("Avatar",
                     "A marine falls goes to another planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock",
                             "Using Rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtu.be/XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://youtu.be/c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://youtu.be/FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                           "A real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://youtu.be/FovFG3N_RSU")

#added module for quiz
demons = media.Movie("Demons",
                     "young friends are invited to a movie theater only to be trapped",
                     "https://upload.wikimedia.org/wikipedia/en/2/2b/Demonsposter1986.jpg",
                     "https://youtu.be/PwX0hOpsuec")
#print(demons.title)
#demons.show_trailer()

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, demons]
fresh_tomatoes.open_movies_page(movies)
