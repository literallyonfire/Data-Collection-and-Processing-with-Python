import requests_with_caching #edited requests module created by runestone academy

def get_movies_from_tastedive(search_q, search_type = 'movies', limit=5):
    ''' Takes a movie search query and returns the top five related movies using tastedive api. 
    Args:
        search_q(str): The Search query consisting of a movie title. Eg: 'Black Panthers'
        search_type(str): Specifiy which type of media you are looking for. Eg: Movies, Podcasts, Music etc
        limit(str or int): Specify the limit of related movies you would like to receive. Default is 5
    Returns:
        js(dict): json formatted dictionary consisting of related movies of search_query
    '''
    search_url = 'https://tastedive.com/api/similar'#Base Url for TasteDive Api
    
    #Parameters for the request
    params = {}
    params['q'] = str(search_q)
    params['type'] = str(search_type)
    params['limit'] = limit
    
    #Requesting related movies from tastedive api
    result = requests_with_caching.get(search_url, params=params)
    
    #Convert it from string to json
    movie_results = result.json()
    return movie_results

def extract_movie_titles(movie_results):
    ''' Takes movie_results returned from get_movies_from_tastedive function or tastedive api and returns a list of related movie names
    Args:
        movie_results(dict): data returned from tastedive api
    Returns:
        related_list(list): list of related movie names pulled from input
    '''
    movies_dict = movie_results
    related_list = [movie['Name'] for movie in movies_dict['Similar']['Results']]
    return relted_list

def get_related_titles(movie_list):
    '''Takes a list of movies as input and gets five related movies for each movie in the list of movies. Then returns it into one gaint list.
       Returned list only contains unique values.
    Args:
       movie_list(list): List of movies. The function takes this as input and gathers 5 recommendations.
    Returns:
        new_movie_list(list): 5 recommendations gathering from tastedive api based on the input.
    '''
    new_movie_list = []
    for movie in movie_list:
        js = get_movies_from_tastedive(movie)
        related_movies_list = extract_movie_titles(js)
        for movie in related_movies_list:
            if movie not in new_movie_list:
                new_movie_list.append(movie)
    return new_movie_list

def get_movie_data(movie_title, r_data_type='json'):
    ''' Takes a movie title as search query and returns a dictionary with information pulled from omdbapi about the movie.
    Args:
        movie_title(str): The title of the movie you want to get data for. 
        r_data_type(str): The format of data you want to receive. Eg: json, xml etc. Default is json.
    Returns:
        js(dict): dictionary filled with information about the movie.
    '''
    #Base url for Omdbapi
    search_url = 'http://www.omdbapi.com/'
    
    #Parameters for the request
    params = {}
    params['t'] = movie_title
    params['r'] = r_data_type
    
    #Gathering information from the request
    result = requests_with_caching.get(search_url, params=params)
    js = result.json()
    return js

def get_movie_rating(omdb_dict):
    ''' Takes a movie json dictionary from omdbapi and returns its rotten tomatoes score. 
    '''
    rotten_score = 0
    for rating_dict in omdb_dict['Ratings']:
        #print(rating_dict)
        if rating_dict['Source'] is 'Rotten Tomatoes':
            value_str = rating_dict['Value'][:-1]
            rotten_score = int(value_str)
    return rotten_score

def get_sorted_recommendations(movie_list):
    ''' The main function for getting recommendations. Takes a list of your favorite movies.
        Based on results from omdbapi and tastedive api, generates top five recommendations for you.
        Upon ties in rotten tomatoe score, the function breaks ties by sorting in reverse alphabetical order.
        Eg: ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
    '''
    #Gets related movies to movies in movie_list
    related_list = get_related_titles(movie_list)
    #empty rotten tomatoes score keeper
    score_list = []
    
    #for each movie in related_list, finds and appends the rotten tomatoes score into score_list.
    for movie in related_list:
        omdb_data = get_movie_data(movie)
        score = get_movie_rating(omdb_data)
        score_list.append(score)
        
    #zips related movies with its rotten tomatoe score
    related_list = zip(related_list, score_list) #Eg: [('Black Panters', '79')]
    
    #Sorts the list first by alphabetical order
    related_list = sorted(related_list, key = lambda movie_name: movie_name[0])
    #Sorts again in reverse numerical order. So the movies with the greatest score is at position 0. 
    related_list = sorted(related_list, key= lambda movie_score: movie_score[1], reverse=True)
    
    return [movie_name for movie_name,movie_score in related_list]


# Created as part of University of Michigan's Data Collection and Processing with Python course. 
# Put on github as a reference for myself and to act as a guide for future learners of the course. 
# As usual, made with <3 by u/literallyonfire