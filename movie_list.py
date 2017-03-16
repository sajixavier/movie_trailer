import fresh_tomatoes
import media


# creating a new movie instance for movie "Terminator"
terminator = media.Movie("Terminator",
                         "A cyborg assassin is sent back in time to "
                         "kill Sarah, a waitress, in a bid to stop her "
                         "son who will wage a long war against his enemy "
                         "in the future unless the course of history "
                         "is altered.",
                         "https://s-media-cache-ak0.pinimg.com"
                         "/originals/10/b2/7f"
                         "/10b27fc133f7eb3a8c1751d92fd9054d.jpg",
                         "https://www.youtube.com/watch?v=lwSysg9o7wE")

# creating a new movie instance for movie "Kung Fu Panda"
kung_fu_panda = media.Movie("Kung Fu Panda",
                            "Po finds himself selected as the Dragon "
                            "Warrior. The Furious Five, residing in "
                            "the barracks, and he take on the "
                            "responsibility to battle against "
                            "the inimical "
                            "forces in the Valley of Peace.",
                            "https://upload.wikimedia.org/wikipedia"
                            "/en/7/76/Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

# creating a new movie instance for movie "Avengers"
avengers = media.Movie("The Avengers",
                       "S.H.I.E.L.D. leader Nick Fury is compelled "
                       "to launch the 'Avengers Initiative' when "
                       "Loki poses a threat to planet Earth. "
                       "Will Nick Fury's squad of superheroes "
                       "prove themselves equal to the task?",
                       "https://upload.wikimedia.org/wikipedia"
                       "/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# creating a new movie instance for movie "Fast and Furious"
fast_furious = media.Movie("Fast and Furious",
                           "The Fast and the Furious is an American "
                           "franchise based on a series of action "
                           "films that is largely concerned with "
                           "illegal street racing and heists, and "
                           "includes material in various other media that "
                           "depict characters and situations from the films",
                           "http://www.standbyformindcontrol.com"
                           "/wp-content/uploads/2014/04"
                           "/fullhd-hizli-ve-ofkeli-1-fast-and-"
                           "furious-1-turkce-dublaj-izle.jpg",
                           "https://www.youtube.com/watch?v=uisBaTkQAEs")

# creating a new movie instance for movie "The Revenant"
revenant = media.Movie("The Revenant",
                       "Hugh Glass, a legendary frontiersman, is "
                       "severely injured in a bear attack and is "
                       "abandoned by his hunting crew. He uses his "
                       "skills to survive and take revenge on his "
                       "companion who betrayed him.",
                       "https://upload.wikimedia.org/wikipedia/en"
                       "/b/b6/The_Revenant_2015_film_poster.jpg",
                       "https://www.youtube.com/watch?v=LoebZZ8K5N0")

# creating a new movie instance for movie "Django Unchained"
django_unchained = media.Movie("Django Unchained",
                               "When Django, a slave, is freed, he "
                               "joins forces with a bounty hunter to "
                               "rescue his wife, who has been captured "
                               "by a hard-hearted plantation owner.",
                               "https://images-na.ssl-images-amazon.com"
                               "/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkF"
                               "tZTcwODg1MDU4OA@@._V1_UY1200_CR90,"
                               "0,630,1200_AL_.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")

# creating a list of movie instances
movies = [terminator, kung_fu_panda, avengers,
          fast_furious, revenant, django_unchained]

# calling the movie library "fresh_tomatoes"
fresh_tomatoes.open_movies_page(movies)
