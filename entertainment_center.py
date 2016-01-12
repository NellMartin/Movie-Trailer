import fresh_tomatoes
import media

# Movies instances with movie title, storyline, poster image URL, movie trailer URL, and review URL.

exmachina = media.Movie("Exmachina",  
                        "A young programmer is selected to participate in a breakthrough experiment.",  
                        "https://upload.wikimedia.org/wikipedia/he/1/1b/Ex_Machina_Poster.jpg",
                        "https://www.youtube.com/watch?v=XYGzRB4Pnq8",
                        "http://www.rottentomatoes.com/m/ex_machina/")

imitation_game = media.Movie("The Imitation Game", 
                             """The Imitation Game is a 2014 American historical drama thriller
                             film directed by Morten Tyldum.""",
                             "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
                             "https://www.youtube.com/watch?v=nuPZUUED5uk",
                             "http://www.rottentomatoes.com/m/the_imitation_game/?search=imitation%20game")

automata = media.Movie("Automata",
                       "Automata is a 2014 science fiction action film starring Antonio Banderas.",
                       "https://upload.wikimedia.org/wikipedia/en/6/65/Automata_poster.jpg",
                       "https://www.youtube.com/watch?v=Wh_wmaOZcWo",
                       "http://www.rottentomatoes.com/m/automata/?search=automata")

trascendence = media.Movie("Trascendence",
                           """Transcendence is a 2014 science fiction film directed by cinematographer"
                           Wally Pfister, and written by Jack Paglen.""",
                           "https://upload.wikimedia.org/wikipedia/en/e/ef/Transcendence2014Poster.jpg",
                           "https://www.youtube.com/watch?v=VCTen3-B8GU",
                           "http://www.rottentomatoes.com/m/transcendence_2014/")

beautiful_mind = media.Movie("A Beautiful Mind",
                             """A Beautiful Mind is a 2001 American biographical drama film based on the
                            life of John Nash, a Nobel Laureate in Economics.""",
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                             "https://www.youtube.com/watch?v=UT4Oq_dOofY",
                             "http://www.rottentomatoes.com/m/beautiful_mind/?search=beautiful%20mind")

interstellar = media.Movie("Interstellar",
                           "Interstellar is a 2014 epic science fiction film directed by Christopher Nolan.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E",
                           "http://www.rottentomatoes.com/m/interstellar_2014/")

# A list of the intances are stored in the movies list.
movies = [exmachina, imitation_game, automata, trascendence, beautiful_mind, interstellar]

# The file fresh_tomatoes.py renderizes the html to show the movies trailer website.
fresh_tomatoes.open_movies_page(movies)
