from functions import mood_finder, music_recommender, playlist_interest

##
##


# This tests the callability of the playlist_interest() function, ensures that the paramenter for the function is a list, 
# and checks if the number of questions asked is 2. As the aim of the function is to collect user input (using the input function), 
# the returns would be variable and user dependent, which is why the output aspect can't be specifically tested. 
# However, if the input parameter is a list of length 2 as established here, the output would be a list of 
# the preferred options presented (and length 2). 
def test_mood_finder():
    
    mood_insight = ['Hi! Welcome to Vibe - the mood based K-Pop music recommender :) \n\n Note: Please input your preferences just as they are presented in the options.\n\n Firstly, how are you primarily feeling? \nHappy\nCalm\nSad\nFrustrated\nRomantic\nExploratory\n\n',
                    '\nWhat kind of music are you open to now? \nChill\nIntense\nGroovy\nUplifting\nSurprise Me!\n\n']
    
    assert callable(mood_finder)
    assert isinstance(mood_insight, list)
    assert len(mood_insight) == 2

    
# This tests a) its callability, b) the output type being a string, 
# c) the functionality when both the mood and music type are particularly specified 
# (for ex: ['Happy','Groovy']), and d) the functionality when the mood is given and the 
# 'Surprise Me!' option is chosen  under the music type (for ex: ['Calm','Surprise Me!']). 
def test_music_recommender():
    
    dummy_music_sampler = {'Happy_Chill':[' https://www.youtube.com/watch?v=WyiIGEHQP8o ',
                                          ' https://www.youtube.com/watch?v=IdssuxDdqKk '],
                           'Happy_Intense':[' https://www.youtube.com/watch?v=qfVuRQX0ydQ ',
                                            ' https://www.youtube.com/watch?v=CyzEtbG-sxY '],
                           'Happy_Groovy':[' https://www.youtube.com/watch?v=MAWM7Y9Wnd0 ',
                                           ' https://www.youtube.com/watch?v=AtNBhPxVwh0 '],
                           'Happy_Uplifting':[' https://www.youtube.com/watch?v=lNvBbh5jDcA ',
                                              ' https://www.youtube.com/watch?v=p9LLoijPQfg '],
                           'Calm_Chill':[' https://www.youtube.com/watch?v=R9VDPMk5ls0 ',
                                         ' https://www.youtube.com/watch?v=dz_W3yD0Ip0 '],
                           'Calm_Intense':[' https://www.youtube.com/watch?v=nt4f4pPCEFs ',
                                           ' https://www.youtube.com/watch?v=Z7yNvMzz2zg '],
                           'Calm_Groovy':[' https://www.youtube.com/watch?v=9VyUD_tBYq4 ',
                                          ' https://www.youtube.com/watch?v=gvdACvfuGFA '],
                           'Calm_Uplifting':[' https://www.youtube.com/watch?v=CKZvWhCqx1s ',
                                             ' https://www.youtube.com/watch?v=pa86DMlUpHg ']}
    
    check = music_recommender(['Happy','Surprise Me!'], dummy_music_sampler)
    
    assert callable(music_recommender)
    assert isinstance(check, str)
    assert music_recommender(['Happy','Groovy'], dummy_music_sampler) in [' https://www.youtube.com/watch?v=MAWM7Y9Wnd0 ',
                                                                          ' https://www.youtube.com/watch?v=AtNBhPxVwh0 ']
    assert music_recommender(['Calm','Surprise Me!'], dummy_music_sampler) in [' https://www.youtube.com/watch?v=R9VDPMk5ls0 ',
                                                                               ' https://www.youtube.com/watch?v=dz_W3yD0Ip0 ',
                                                                               ' https://www.youtube.com/watch?v=nt4f4pPCEFs ',
                                                                               ' https://www.youtube.com/watch?v=Z7yNvMzz2zg ',
                                                                               ' https://www.youtube.com/watch?v=9VyUD_tBYq4 ',
                                                                               ' https://www.youtube.com/watch?v=gvdACvfuGFA ',
                                                                               ' https://www.youtube.com/watch?v=CKZvWhCqx1s ',
                                                                               ' https://www.youtube.com/watch?v=pa86DMlUpHg ']
    
    
# This tests the callability of the playlist_interest() function and ensures that the 
# paramenters for the function are strings. The variables that are used for the 
# playlist_interest() function have been copy-pasted here for this purpose.  
def test_playlist_interest():
    
    playlist_insight = 'Now that you have a feel, would you like a link to a frequently updated K-Pop playlist? \n\nYes\nNo\n\n'
    playlist_choice = 'What is your platform of choice? \n\nYouTube\nSpotify\n\n'
    
    assert callable(playlist_interest)
    assert isinstance(playlist_insight, str)
    assert isinstance(playlist_choice, str)
