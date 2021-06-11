''' This script contains all the questions created to gather user input and the music sampler containing all the recommendations as per the primary mood and music type combinations. '''

# In the music_sampler dictionary below, there are 6 primary moods (happy, calm, sad, frustrated, romantic, and exploratory) and 4 music types (chill, intense, groovy, and uplifting) per each mood. Each combination is an individual key, and has three values (music recommendations) associated with it. This sampler is define outside the scope of the function in order to enable the ease of adding in additional entries in the future. 
music_sampler = {'Happy_Chill':[' https://www.youtube.com/watch?v=WyiIGEHQP8o ',' https://www.youtube.com/watch?v=IdssuxDdqKk ', ' https://www.youtube.com/watch?v=5MUtmsNDL9g '],
                 'Happy_Intense':[' https://www.youtube.com/watch?v=qfVuRQX0ydQ ', ' https://www.youtube.com/watch?v=CyzEtbG-sxY ', ' https://www.youtube.com/watch?v=qvByCuIsVe0 '],
                 'Happy_Groovy':[' https://www.youtube.com/watch?v=MAWM7Y9Wnd0 ', ' https://www.youtube.com/watch?v=AtNBhPxVwh0 ', ' https://www.youtube.com/watch?v=bUKWmDodsMw '],
                 'Happy_Uplifting':[' https://www.youtube.com/watch?v=lNvBbh5jDcA ', ' https://www.youtube.com/watch?v=p9LLoijPQfg ', ' https://www.youtube.com/watch?v=kpewpapC9r8 '],
                 'Calm_Chill':[' https://www.youtube.com/watch?v=R9VDPMk5ls0 ', ' https://www.youtube.com/watch?v=dz_W3yD0Ip0 ', ' https://www.youtube.com/watch?v=oxr-iKJEgAU '],
                 'Calm_Intense':[' https://www.youtube.com/watch?v=nt4f4pPCEFs ', ' https://www.youtube.com/watch?v=Z7yNvMzz2zg ', ' https://www.youtube.com/watch?v=MkTUnBiAmOE '],
                 'Calm_Groovy':[' https://www.youtube.com/watch?v=9VyUD_tBYq4 ', ' https://www.youtube.com/watch?v=gvdACvfuGFA ', ' https://www.youtube.com/watch?v=OGsIwEIhqpY '],
                 'Calm_Uplifting':[' https://www.youtube.com/watch?v=CKZvWhCqx1s ', ' https://www.youtube.com/watch?v=pa86DMlUpHg ', ' https://www.youtube.com/watch?v=3p7s7Rjh4fg '],
                 'Sad_Chill': [' https://www.youtube.com/watch?v=k-U9YOXG4Qg ', ' https://www.youtube.com/watch?v=vecSVX1QYbQ ', ' https://www.youtube.com/watch?v=MevmaoP4pEU '],
                 'Sad_Intense':[' https://www.youtube.com/watch?v=T271Va9sSA8 ', ' https://www.youtube.com/watch?v=amnspvOH-EE ', ' https://www.youtube.com/watch?v=-gZC9hC1PDQ '],
                 'Sad_Groovy':[' https://www.youtube.com/watch?v=LYAkY8Dh9CU ', ' https://www.youtube.com/watch?v=zFT3f9biz68 ', ' https://www.youtube.com/watch?v=-kcG8UjJAeM '],
                 'Sad_Uplifting':[' https://www.youtube.com/watch?v=s4jHQXd-7gg ', ' https://www.youtube.com/watch?v=j69PEX9bzRY ', ' https://www.youtube.com/watch?v=ov3NRyoIEQ4 '],
                 'Frustrated_Chill':[' https://www.youtube.com/watch?v=5LbFdY6vGsQ ', ' https://www.youtube.com/watch?v=h-wATDal7_0 ', ' https://www.youtube.com/watch?v=4UX7CplWAPo '],
                 'Frustrated_Intense':[' https://www.youtube.com/watch?v=TQTlCHxyuu8 ', ' https://www.youtube.com/watch?v=1yxEmmYQdl8 ', ' https://www.youtube.com/watch?v=FCsLikmxhV0 '],
                 'Frustrated_Groovy':[' https://www.youtube.com/watch?v=ZbIs7AOZ8Ls ', ' https://www.youtube.com/watch?v=2U2DBjPJgI4 ', ' https://www.youtube.com/watch?v=0b-EatqUvb4 '],
                 'Frustrated_Uplifting':[' https://www.youtube.com/watch?v=0EUrRy9Rs1M ', ' https://www.youtube.com/watch?v=tOpTQ3Fuf9s ', ' https://www.youtube.com/watch?v=KAPXc0M4tLg '],
                 'Romantic_Chill':[' https://www.youtube.com/watch?v=2d-7vGTMw5Q ', ' https://www.youtube.com/watch?v=tpj_UOd98iI ', ' https://www.youtube.com/watch?v=NmW5g5diTMQ '],
                 'Romantic_Intense':[' https://www.youtube.com/watch?v=X7d6Dt17yHk ', ' https://www.youtube.com/watch?v=eOOsAeOx5a0 ', ' https://www.youtube.com/watch?v=_hFarg-Obuc '],
                 'Romantic_Groovy':[' https://www.youtube.com/watch?v=DTcKkcyS410 ', ' https://www.youtube.com/watch?v=-EfjXQgE1e8 ', ' https://www.youtube.com/watch?v=8M3WUaeIbOk '],
                 'Romantic_Uplifting':[' https://www.youtube.com/watch?v=o52lx-ILy_w ' , ' https://www.youtube.com/watch?v=G7NW70kOURQ ', ' https://www.youtube.com/watch?v=aASPZ-QdXMo '],
                 'Exploratory_Chill':[' https://www.youtube.com/watch?v=QZRXNIhb_UQ ', ' https://www.youtube.com/watch?v=bEp5yuouu5Y ', ' https://www.youtube.com/watch?v=u4iDL3c0T1c '],
                 'Exploratory_Intense':[' https://www.youtube.com/watch?v=F9CrRG6j2SM ', ' https://www.youtube.com/watch?v=a-E8PXVJy6k ', ' https://www.youtube.com/watch?v=eTuR-e6aLRo '],
                 'Exploratory_Groovy':[' https://www.youtube.com/watch?v=CxnJf0tWu48 ', ' https://www.youtube.com/watch?v=E787kCVAeL8 ',  ' https://www.youtube.com/watch?v=UuV2BmJ1p_I '],
                 'Exploratory__Uplifting':[' https://www.youtube.com/watch?v=PQOJJ037ys8 ', ' https://www.youtube.com/watch?v=X-iJZ0gfKPo ', ' https://www.youtube.com/watch?v=Svmb3MvlNoM ']}

# mood_insight is a list that contains the questions designed to gain user mood and music type preference. The input() function takes in responses to questions that are created in a multiple choice format with set choices. 
mood_insight = ['Hi! Welcome to Vibe - the mood based K-Pop music recommender :) \n\n Note: Please input your preferences EXACTLY as they are presented in the options.\n\n Firstly, how are you primarily feeling? \nHappy\nCalm\nSad\nFrustrated\nRomantic\nExploratory\n\n',
                '\nWhat kind of music are you open to now? \nChill\nIntense\nGroovy\nUplifting\nSurprise Me!\n\n']

# The following two strings are used in the playlist_interest() function.
playlist_insight = 'Now that you have a feel, would you like a link to a frequently updated K-Pop playlist? \n\nYes\nNo\n\n'
playlist_choice = 'What is your platform of choice? \n\nYouTube\nSpotify\n\n'
