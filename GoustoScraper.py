import requests
import pandas as pd


#specify the url
url = 'https://www.gousto.co.uk/cookbook/beef-recipes/annabels-mighty-meatball-pasta-bake'

import pandas as pd
import requests

df = pd.read_html(
    requests.get(url).text,
    flavor="bs4",
)
df[-1].to_csv("last_table.csv", index=False)