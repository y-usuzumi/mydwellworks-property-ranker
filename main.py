from datetime import datetime
from mpr.db import DB, Property
from mpr.extractor import MyDwellworksPropertiesExtractor


if __name__ == '__main__':
    db = DB("sqlite:///mpr.db")

    extractor = MyDwellworksPropertiesExtractor()
    raw_props = extractor.extract_properties()

    with db.session() as sess:
        for raw_prop in raw_props:
            raw_pp = raw_prop['property']
            prop = Property(
                name=raw_pp['display_name'],
                description=raw_pp['description'],
                address=raw_pp['address'],
                location='POINT(%f,%f)' % (raw_pp['longitude'], raw_pp['latitude']),
                rent=raw_prop['rent'],
                parking_fee=raw_pp['parking_fee'],
                size=float(raw_pp['size'].split(';')[1].strip()),
                typ=raw_pp['type'],
                included_utilities=','.join(raw_pp['included_utilities'] or ''),
                excluded_utilities=','.join(raw_pp['excluded_utilities'] or ''),
                archived=raw_prop['archived'],
                date_available=datetime.strptime(raw_prop['date_available'], '%Y-%m-%d'),
            )
            sess.add(prop)
