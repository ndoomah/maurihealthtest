from pytrends.request import TrendReq
import pymongo
import json
from mongodb_atlas import connect_db

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
#pytrend.build_payload(kw_list=['flu', 'gastro', 'conjunctivitis', 'respiratory infection'], geo='MU', timeframe='2018-01-01 2018-12-31')
time = '2018-12-01 2019-01-05'
disease_term = ['flu', 'gastro', 'conjunctivitis', 'pink eye', 'respiratory infection']

for term in disease_term:
    pytrend.build_payload(kw_list=[term], geo='MU', timeframe=time)

    # Interest by Region
    trend = pytrend.interest_by_region(resolution='SUBREGION')
    print(trend)
    json_data = trend.to_json()
    js = json.loads(json_data)

    connect_db.save_trends(js)




