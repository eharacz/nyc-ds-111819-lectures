### Searching Functions ###

def find_by_name(our_data,name):
    """Takes in a string that represents the name of an album. Should return a dictionary with the correct album, or return None."""
    for album in our_data:
        if album['album'] == name:
            return album
    return None
            
            
def find_by_rank(our_data,rank):
    """Takes in a number that represents the rank in the list of top albums and returns the album with that rank. If there is no album with that rank, it returns None."""
    for album in our_data:
        if album['number'] == str(rank):
            return album
    return None
        
        
def find_by_year(our_data,year):
    """Takes in a number for the year in which an album was released and returns a list of albums that were released in that year. If there are no albums released in the given year, it returns an empty list."""
    return [album for album in our_data if album['number'] == str(year)]

def multiple_years(our_data, start, end):
    """Takes in a start year and end year. Returns a list of all albums that were released on or between the start and end years. If no albums are found for those years, then an empty list is returned."""
    count = start
    album_list = []
    while count <= end:
        album_list.append(find_by_year(our_data,count))
        count += 1

def multiple_ranks(our_data,start, end):
    """Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks. If no albums are found for those ranks, then an empty list is returned."""
    count = start
    album_list = []
    while count <= end:
        album_list.append(find_by_rank(count))
        count += 1


#### "All" Functions ###


def all_titles(our_data):
    """Returns a list of titles for each album."""
    return [album['album'] for album in our_data]

def all_artists(our_data):
    """Returns a list of artist names for each album."""
    return [album['artist'] for album in our_data]

    
    
### Questions to Answer Functions ###

def most_popular_artist(our_data):
    """Returns the artist with the highest amount of albums on the list of top albums."""
    counter_dict = {}
    for artist in all_artists(our_data):
        if artist in counter_dict:
            counter_dict[artist] += 1
        else:
            counter_dict[artist] = 1
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys) 
    return artist_lists  
  most_popular_artist(our_data)

def histogram_decades(our_data):
    """Returns a histogram with each decade pointing to the number of albums released during that decade."""
    decade_dict = {}
    for album in our_data:
        decade = int(album['year'])//10
        if decade in decade_dict:
            decade_dict[decade] += 1
        else:
            decade_dict[decade] = 1
    return decade_dict

# !pip install plotly
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
hist_decades = histogram_decades(our_data)


init_notebook_mode(connected=True)
iplot([{'type':'bar','x' : ['1950s','1960s','1970s','1980s','1990s','2000s','2010s'],'y': list(hist_decades.values())}])


def histogram_genres(our_data):
    """Returns a histogram with each genre pointing to the number of albums that are categorized as being in that genre."""
    genre_list = []
    for album in our_data:
        genre_list.extend(genre.strip() for genre in album['genre'].split(','))
    genre_dict = {}
    for genre in genre_list:
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    return genre_dict

genre_hist = histogram_genres(our_data)
print(genre_hist)

iplot([{'type':'bar','x':list(genre_hist.keys()),'y':list(genre_hist.values()),'name':'Number of albums by genre'}])

# Next Steps #
















