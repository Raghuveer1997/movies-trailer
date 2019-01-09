import fresh_tomatoes
import media_pyfile

edge_of_tomorrow=media_pyfile.Hollywood_Movies("Edge Of Tomorrow",
                      "A story about a man repeting his day again after he is dead",
                      "https://m.media-amazon.com/images/M/MV5BMTc5OTk4MTM3M15BMl5BanBnXkFtZTgwODcxNjg3MDE@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=yUmSVcttXnI")
#print(toy_story.storyline)

batman=media_pyfile.Hollywood_Movies("Batman v Superman",
                   "A fight between batman and superman",
                   "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                   "https://www.youtube.com/watch?v=fis-9Zqu2Ro")
#print(avatar.storyline)
#avatar.show_trailer()

avengers=media_pyfile.Hollywood_Movies("Avengers: Age of Ultron",
                     "Group of super heros band together to save Earth",
                     "https://m.media-amazon.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_QL50_SY1000_SX675_AL_.jpg",
                     "https://www.youtube.com/watch?v=JAUoeqvedMo")
#print(avengers.storyline)
#avengers.show_trailer()

transformers=media_pyfile.Hollywood_Movies("Transformers",
                         "Alien Robots saving earth from creators",
                         "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg",
                         "https://www.youtube.com/watch?v=S30VkLn5a2o")

black_panther=media_pyfile.Hollywood_Movies("Black Panther",
                         "A king with superhuman abilites rule nation of wakanda",
                         "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                         "https://www.youtube.com/watch?v=xjDjIWPwcPU")

wonder_women=media_pyfile.Hollywood_Movies("Wonder Women",
                        "A warrior princess who lived a long time saving people",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                        "https://www.youtube.com/watch?v=VSB4wGIdDwo")
dragon_ball_super=media_pyfile.Hollywood_Movies("Dragon ball Super:Broly",
                                                "Fate of three sayains who became very powerful",
                                                "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/DB_THE_MOVIE_NO._20.jpg/220px-DB_THE_MOVIE_NO._20.jpg",
                                                "https://www.youtube.com/watch?v=FHgm89hKpXU")
aquaman=media_pyfile.Hollywood_Movies("Aquaman",
                                      "A half breed of human and atlantian who becomes king",
                                      "https://upload.wikimedia.org/wikipedia/en/3/3a/Aquaman_poster.jpg",
                                      "https://www.youtube.com/watch?v=WaWnLiffxJ4")
captian_marvel=media_pyfile.Hollywood_Movies("Captian Marvel",
                                             "Captain Marvel gets caught in galactic war between two alien races",
                                             "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg",
                                             "https://www.youtube.com/watch?v=0LHxvxdRnYc")

movies=[edge_of_tomorrow,batman,avengers,transformers,black_panther,wonder_women,dragon_ball_super,aquaman,captian_marvel]
fresh_tomatoes.open_movies_page(movies)

                        
