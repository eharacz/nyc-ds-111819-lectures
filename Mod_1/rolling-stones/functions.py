### Searching Functions ###

def find_by_name(album):
    for item in top_500:    
        if album == item['album']:
            return item
        else:
            return None
            
            
def find_by_rank(num):
    for item in top_500:    
        if str(num) == item['number']:
            return item
            print (item)
        else:
            return None
        
        
def find_by_year(yr):
    years = []
    for item in top_500:    
        if str(yr) == item['year']:
            years.append(item)
    return years

def find_by_years(yr_start, yr_end):
    def find_by_years(yr_start, yr_end):
    """Takes in a start year and end year. Returns a list of all albums that were released on or between the start and end years.        If no albums are found for those years, then an empty list is returned"""
    albums_btw_yrs=[]
    for item in top_500:    
        if str(yr_start) <= item['year'] and str(yr_end) >=  item['year']:
            albums_btw_yrs.append(item['album'])
    return(albums_btw_yrs)

def find_by_ranks(rnk_start,rnk_end):
    """Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks.                      If no albums are found for those ranks, then an empty list is returned."""
    albums_btw_rnk=[]
    for item in top_500:    
        if str(rnk_start) <= item['number'] and str(rnk_end) >=  item['number']:
            albums_btw_rnk.append(item['album'])
    return(albums_btw_rnk)



#### Searching Functions ###


def all_titles():
    # 1.append 3.list comprehension #
    titles = []
    for item in top_500:
        titles.append(item['album'])
    return titles
    #3.List Comprehension albums = [item['album']: for item in top_500 #or# albums2 = {item['album']: item['year'] for item in   top_500}

    
    
### Questions to answer / functions ###

def artist_mostalb(collection):
    #Artists with the most albums - Returns the artist with the highest amount of albums on the list of top albums#
   artists = {}
   for album in collection:
       if album['artist'] in artists:
           artists[album['artist']] += 1
       else:
           artists[album['artist']] = 1
   print(artists)
   #map(lambda album: artists[album['artist']] += 1 if artists[album['artist']] else artists[album['artist']] = 1, collection)
   return max(artists, key = artists.get)
    




















