from app import db
from app.models import Assets
import os
import pandas as pd

file = os.path.dirname(os.path.abspath(__file__)) + "/assets.csv"
assets = pd.read_csv(file)

# asset = Assets()
# asset.medium = 'air'
# asset.asset_type = 1
# db.session.add(asset)
# db.session.commit()
# asset = Assets(assets.itertuples(index=False).__next__())
# db.session.add(asset)
# db.session.commit()

for row in assets.itertuples(index=False):
    asset = Assets(row)
    db.session.add(asset)
    db.session.commit()

print('done')
