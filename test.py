import pandas as pd
import requests
import time


url = "http://192.168.100.1/cgi-bin/status_cgi"

def get_statspage(url):
  headers = { 
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
  'Accept-Language' : 'en-US,en;q=0.5', 
  'Accept-Encoding' : 'gzip', 
  'DNT' : '1', # Do Not Track Request Header 
  'Connection' : 'close' }

  r = requests.get(url,headers=headers)
  df_list = pd.read_html(r.text)
  return df_list[1]

def get_stats(df,removeword):
  i=1
  results={}
  if len(df) == 9:
    for counter in df:
      if removeword not in counter:
        results[i]=counter
        i+=1
  return results
  
 
df=get_statspage(url)
uncorrected_first=get_stats(df[8],"Uncorrectables")
corrected_first=get_stats(df[7],"Correcteds")

time.sleep(5)

df=get_statspage(url)
uncorrected_second=get_stats(df[8],"Uncorrectables")
corrected_second=get_stats(df[7],"Correcteds")

print(uncorrected_first)
print(uncorrected_second)

print(corrected_first)
print(corrected_second)

