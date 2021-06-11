# COGS-18-Final-Project
COGS 18 Final Project: Mood-Based Music Recommender (K-Pop ver.)

This recommender takes in user mood and basic music choice and presents a recommendation that matches the specified preferences. Then, if the user is interested, it also provides a recommendation to a general K-Pop playlist either on Spotify or YouTube, again on the basis of user preference.

Details
I generated a dictionary called music_sampler which currently has 24 keys. These 24 keys are combinations of the 6 primary moods (i.e. happy, calm, sad, frustrated, romantic, and exploratory) and 4 basic/arbitrary music types (i.e. chill, intense, groovy, and uplifting). Thus, each key is one mood-music type combination (ex: Happy_Intense). In this dictionary, each key has 3 associated values, meaning that each category has 3 possible recommendations (6 x 4 x 3 = 72 recommendations in total).This has been designed to enable the following functionalities:
a) Inbuilt randomness: Given a particular category, the recommender is built to present one of the 3 available options under it. This has been done to ensure that users re-taking the recommender with the same preferences would have a chance to enjoy more music rather than being limited to one particular song.
b) Surprise Me!: To make things fun, I wrote code to facilitate a 'Surprise Me!' option. If the user indicates this option under the music type preference, this uses information regaring their primary mood to present them with a recommendation from a radom music category under the given mood. For instance, a user input of [Calm, Surprise Me!] would present a recommendation from 1 of the values of the 4 'Calm' subcategories (i.e 1 out of 12 options).
The randomness is achieved through the use of the choice method from the random module.

The music_sampler dictionary and the questions designed to elicit user responses regarding mood and playlist interest are stored in a script and need to be imported (scripts/my_script.py).
The functions also need to be imported from a module (my_module/functions.py).

The mood_finder function uses the input feature to collect information regarding the user's mood and music choice based on the questions posed through the mood_insight list. An for-loop iterates over the questions in mood_insight list, and the responses are appended into a list - mood_info which is designed to be in a [mood, music_type] format (ex: ['Chill', 'Groovy']). Then, the music_recommender function uses mood_info to make the respective recommendation. A for-loop iterates over the keys of the music_sampler dictionary and a conditional statement searches for the category label that contains the same information as that held in mood_info. A recommendation is made using the choice method from the random module. Finally, the playlist_interest function suggests a playlist based on interest. Conditional statements are used here to determine interest and return the appropriate outputs.


Hope you have fun using this recommender!
