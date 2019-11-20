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
            print(item)
        else:
            return None


def find_by_year(yr):
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
    """Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks.                      If no albums are found for those ranks, then an empty list is returned."""
    albums_btw_rnk = []
    for item in top_500:
        if rnk_start <= int(item['number']) and rnk_end >= int(item['number']):
            albums_btw_rnk.append(item['album'])
    return(albums_btw_rnk)

### 'All' Functions ###


def all_titles():
    # 1.append 3.list comprehension #
    titles = []
    for item in top_500:
        titles.append(item['album'])
    return titles

### Question to Answer Functions ###
