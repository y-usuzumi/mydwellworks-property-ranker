from mpr.db import DB, Property


if __name__ == '__main__':
    db = DB("sqlite:///mpr.db")

    session = db.new_session()

    prop = Property(name="WTF", location="POLYGON(0 0,1 0,1 1,0 1,0 0)")
    session.add(prop)
    session.commit()
