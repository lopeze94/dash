from mozscape import Mozscape
# import Optimization_Return_Functions as orf
# previously where
# keys were used to get data
import time
# an Instance of the Optimization_Return_Functions class

"""Always Remember Cooper's Lecture On Modularization"""


moz_client = Mozscape('mozscape-5ff03d5969', '5d698b4a4945ff9af6d3392fb495a563')

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

#  for assign_and_return_competitor_normalized_root_domain_moz_trust()
#  we are
#  only returning normalized score


"""

These are now inside Optimization_Return_Functions.py

Begin Return Statements With ['keys']

NOTE: These statements are under revision for modular..
They require being executed through the
above corresponding functions ONLY




def return_competitor_amount_external_links(data):
    return data['ued']
    # Returns number of external links to the URL,
    # including nofollowed links


def return_competitor_amount_root_domain_links(data):
    return data['ped']
    #  Returns number of external links to the root domain,
    #  including nofollowed links


def return_competitor_amount_c_blocks(data):
    return data['pib']  # int
    #  Returns number of links from the same C class IP addresses.


def return_competitor_score_domain_authority(data):
    return data['pda']  # int 0/100 - best to display it this way
    #  Returns normalized 100-point score representing the
    #  likelihood of a domain to rank well in search engine results


def return_competitor_crawler_timestamp(data):
    return data['ulc']
    #  Returns time and date on which Mozscape last
    #  crawled the URL, returned in Unix epoch format


def return_competitor_total_root_domain_links(data):
    return data['puid']  # int
    #  The total number of links, including internal and nofollow links,
    #  to the root domain of the URL


def return_competitor_normalized_root_domain_score(data):
    return data['ptrp']  # number
    # The MozTrust of the root domain of the URL,
    # in both the normalized 10-point score (ptrp)


def return_competitor_normalized_root_domain_moz_trust(data):
    return data['utrp']



POTENTIAL PROBLEMS

These keys ['ddd'] can be switched the variables instead -- possibly
passed by an external widget where we can switch it --
var = function() which returns a code through a Selector!
data[var]
During the switch on a selector - a different key is passed, or
a differnt set of keys to be passed then assigned locally

this will be necessary to use less code to reach into several
different columns within one metric.

This may be a second parameter to be passed in a function's
last name(var, var,..)



POTENTIAL PROBLEMS

Perhaps the selector will assign already stored variables for the cols Calls
this way a pair ors set of pairs, of a cols bit flag and keys are passed to
reduce necessary code


May be able to do assignments and returns within only 2 functions max
"""
