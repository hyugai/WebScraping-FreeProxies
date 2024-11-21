# bs4 
import requests
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent

# asynchronous
import aiohttp
import asyncio

# playwright
from playwright.async_api import async_playwright, Playwright, Page

# data structure
import numpy as np
import pandas as pd

# others
import re, json, sqlite3
import time, random
from pathlib import Path
from datetime import datetime
from io import StringIO
from tabulate2 import tabulate

from proxies import FreeProxyListScraper, GeonodeScraper, scrape_freeProxyList, scrape_geonode, scrape_proxyScrape