from mozscape import Mozscape
# import Optimization_Return_Functions as orf
# previously where
# keys were used to get data
import time
# an Instance of the Optimization_Return_Functions class

# arguments are required to use this tool
moz_client = Mozscape('', '')

"""Through constructors for each selection option -- we can use same url
for all functions"""


"""Begin cols= Calls & desired data Returns"""


def return_canonical_url(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=4)
    return data['uu']
    # this function uses the key within itself
    # uses no outside objects


def return_external_links(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=549755813888)
    return data['ued']  # int
    #  for the URL


def return_external_root_domain_links(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=2251799813685248)
    return data['ped']  # int
# ARDL


# these newly assigned variables came in dictionary form
# you still need the ['key'] to return the desired data
# extract_external_links['ped'] = number/desired data


def return_c_blocks_linked(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=36028797018963968)
    return data['pib']  # int


def return_score_domain_authority(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=68719476736)
    return data['pda']  # int


def return_time_last_crawled(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=144115188075855872)
    return data['ulc']  # epoch format timestamp - Unix


def return_total_root_domain_links(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=8589934592)
    return data['puid']  # int


"""Normalized Moz Rank Score"""


def return_score_normalized_moz_rank(url):
    time.sleep(1.5)
    data = moz_client.urlMetrics(url, cols=65536)
    return data['pmrp']
    # this returns only normal moz rank for root domain
