
def create(db,object: object):
    db.add(object)
    db.commit()
    db.refresh(object)
    return object

def read(db,object):
    data = db.query(object).all()
    return data

def read_by_id(db,object: object,id: int):
    data = db.query(object).filter(object.id == id).first()
    return data

def read_by_email(db, object: object, email: str):
    data = db.query(object).filter(object.email == email).first()
    return data

def delete(db,object: object):
    db.delete(object)
    db.commit()
    db.refresh()
    return object