
#TO PLOT FOUND RESULTS ON MAP (takes data stored in the cloud)
#import map_plot
from multiprocessing.pool import Pool

from facebook import fb_realtime

def run(file):
    exec(open(file).read())


files = ['./facebook/fb_realtime.py','./news_scraper/NewsScraper.py']

def main():
    with Pool() as p:
        p.map(run, files)

if __name__ == '__main__':
    main()
