import argparse
from datetime import datetime
from mpr.env import get_db_connstr
from mpr.db import DB, Property
from mpr.extractor import MyDwellworksPropertiesExtractor


def populate():
    db = DB.singleton()

    extractor = MyDwellworksPropertiesExtractor()
    raw_props = extractor.extract_properties()

    with db.session() as sess:
        for raw_prop in raw_props:
            raw_pp = raw_prop['property']
            prop = Property(
                name=raw_pp['display_name'],
                description=raw_pp['description'],
                address=raw_pp['address'],
                location='POINT(%f %f)' % (raw_pp['longitude'], raw_pp['latitude']),
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


def query():
    db = DB.singleton()

    with db.session() as sess:
        q = sess.query(Property).order_by(Property.location)
        for prop in q:
            print(prop.location)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True, dest='command')
    subparsers.add_parser('populate')
    subparsers.add_parser('query')
    args = parser.parse_args()
    command = args.command
    if command == 'populate':
        populate()
    elif command == 'query':
        query()
    else:
        exit(1)
