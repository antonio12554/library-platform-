
def create(db,object):
    db.add(object)
    db.commit()
    db.refresh()
    return object

def read(db,object):
    data = db.query(object).all()
    return data

def delete(db,object):
    db.delete(object)
    db.commit()
    db.refresh()
    return object