### Searching Functions ###


def find_by_name(album):
    """Takes in a string that represents the name of an album. Should return a dictionary with the correct album, or return None."""
    for item in top_500:
        if album == item['album']:
            return item
        else:
            return None


def find_by_rank(num):
    """Takes in a number that represents the rank in the list of top albums and returns the album with that rank. If there is no album with that rank, it returns None."""
    for item in top_500:
        if str(num) == item['number']:
            return item
            print(item)
        else:
            return None


def find_by_year(yr):
    """Takes in a number for the year in which an album was released and returns a list of albums that were released in that year. If there are no albums released in the given year, it returns an empty list."""
    years = []
    for item in top_500:
        if str(yr) == item['year']:
            years.append(item)
    return years


def find_by_years(yr_start, yr_end):
    """Takes in a start year and end year. Returns a list of all albums that were released on or between the start and end years. If no albums are found for those years, then an empty list is returned"""
    albums_btw_yrs = []
    for item in top_500:
        if yr_start <= int(item['year']) and yr_end >= int(item['year']):
            albums_btw_yrs.append(item['album'])
    return(albums_btw_yrs)


def find_by_ranks(rnk_start, rnk_end):
    """Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks. If no albums are found for those ranks, then an empty list is returned."""
    albums_btw_rnk = []
    for item in top_500:
        if rnk_start <= int(item['number']) and rnk_end >= int(item['number']):
            albums_btw_rnk.append(item['album'])
    return(albums_btw_rnk)

### 'All' Functions ###


def all_titles():
    """Returns a list of titles for each album."""
    # 1.append
    titles = []
    for item in top_500:
        titles.append(item['album'])
    return titles

### Question to Answer Functions ###
