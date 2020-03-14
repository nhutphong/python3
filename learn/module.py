import os
import sys
import keyword

import math
import random

# mo rong chuc nang cho tupple list dict
import collections
import heapq
from itertools import chain
from functools import reduce


import pprint # pprint()

import re
import string
# contains nhieu function +,-,*,/ ...
import operator

# advanced
import asyncio
import threading
# subprocess.call(['ls', 'l']) => run command terminal
# os.system('ls -la')
import subprocess
import queue

#encrypt
import base64
import pickle

import zipfile
import PyPDF2
import docx
import json
import logging #debuging

from PIL import Image

import datetime
import time # .sleep()
import calendar
import timeit

import smtplib #mail

import json
import webbrowser
import socket
import requests
from bs4 import BeautifulSoup

# AI
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf


def json_module():
    # string json
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    # convert json to dict python
    y = json.loads(x) #y la {} dict of python

    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x) # y la string json'{ "name":"John", "age":30, "city":"New York"}'


def collections_module():

    #tao list giới hạn item = maxlen
    list_deque = collections.deque(maxlen=5)

    # {'Phong': ['IT', 25, 'HCM']}
    de_dict = collections.defaultdict(list)
    de_dict['Phong'].extend(['IT', 25, 'HCM'])

    # tao nhanh class ('ClassName', [attr1, attr2, ...])
    ClassName = collections.namedtuple('ClassName', ['first_name', 'last'])


def random_while():
    ran = """
        cac function() trong module random nen dung trong loop
        while -> vi moi lan lap se auto value
    """
    pass
