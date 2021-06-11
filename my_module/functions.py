from random import choice


def mood_finder(mood_insight):
    
    ''' Collects information regarding the user's primary mood and their preferred music type.
    
    Parameters
    ----------
    mood_insight : list
        list of 2 strings which are questions that will be used to elicit user input regarding preference.  
    
    Returns
    -------
    mood_info : list
        list of 2 strings which represent user mood and music type preference as labels.
    '''
    
    mood_info = []

    for item in mood_insight:
        response = input(item) # The input function collects user input as per the options presented in the questions.
        
        # The following asserts ensure the inputs are from the presented choices and throw up an error with guidance otherwise.
        assert isinstance(response, str), 'Input must be a string!'
        assert response in ['Happy', 'Calm', 'Sad', 'Frustrated', 'Romantic', 'Exploratory',
                        'Chill', 'Intense', 'Groovy', 'Uplifting', 'Surprise Me!'], 'Input must be one of the presented options, exactly as they are shown above!'
        mood_info.append(response) 
        
    return mood_info


def music_recommender(mood_info, music_sampler):
    
    ''' Presents a K-Pop music recommendation based on the user's primary mood and music type preference.
    
    Parameters
    ----------
    mood_info : list
        List of 2 strings which represent user mood and music type preference as labels.
    music_sampler : dict
        Dictionary containing 24 keys representing combinations of the primary moods and music types. Each key has 3 values, which in this context are the music recommendation links. 
    
    Returns
    -------
    recommendation : str 
        YouTube link to the music recommendation.
    '''
            
    for music_category in music_sampler:
        if mood_info[0] in music_category and mood_info[1] in music_category:
            recommendation = choice(music_sampler[music_category]) #Randomly selects one of the three links (values). 
            
    # The rest of the code in this function is to facilitate the 'Surprise Me!' option.
    mood_all_music_types = [] 
        
    for music_category in music_sampler:
        if mood_info[0] in music_category:
            mood_all_music_types.append(music_category) # List now contains labels of all music types for the given mood. 
            
    surprise_key = choice(mood_all_music_types) # Label of the randomly chosen music type from the given mood. 
            
    if mood_info[1] == 'Surprise Me!':
            recommendation = choice(music_sampler[surprise_key])
            
    return recommendation


def playlist_interest(playlist_insight, playlist_choice):
    
    ''' Collects information regarding user interest in a playlist and presents it if they are interested.
    
    Parameters
    ----------
    playlist_insight : str
        Question to gather information regarding interest in a playlist recommendation.
    playlist_choice : str
        Question to gather information regarding the platform of choice. 
    
    Returns
    -------
    output : str
        If user is interested in a playlist, output is a link. If not, it is a thanks and bye statement. 
    '''
    print ('Please enter input choice exactly as it is presented in the given choices!')
    
    if input(playlist_insight) == 'Yes':
        print ('\n\nAlright, coming up :)')
        
        if input(playlist_choice) == 'YouTube':  
            output = ' https://www.youtube.com/playlist?list=PLOHoVaTp8R7dfrJW5pumS0iD_dhlXKv17 ' 
        else:
            output = ' https://open.spotify.com/playlist/37i9dQZF1DX9tPFwDMOaN1?si=ceede75a665c45b0 '
            
        print ('\n\nHope you have fun grooving along! See you later :)')
        
    else:
        output = ('Hope you got to listen to a nice song. See you later :)')
        
    return output
