# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:49:31 2021

@author: DomPC
"""

from craigslist import CraigslistForSale

cl_fs = CraigslistForSale(site='corvallis', category='bia',
                          filters={'max_price' : 200, 'has_image': True, 'search_distance': 25})

print(cl_fs.get_results_approx_count())

for result in cl_fs.get_results(sort_by='newest',limit=5):
    print(result)