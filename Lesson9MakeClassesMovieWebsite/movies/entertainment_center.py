import media 

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/tN1A2mVnrOM")
avatar = media.Movie("Avatar",
                     "A marine falls goes to another planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
demons = media.Movie("Demons",
                     "young friends are invited to a movie theater only to be trapped",
                     "https://upload.wikimedia.org/wikipedia/en/2/2b/Demonsposter1986.jpg",
                     "https://youtu.be/PwX0hOpsuec"
                     )


print(avatar.title)
demons.show_trailer()
