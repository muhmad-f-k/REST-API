from db.moduls import Magsin, session

test = session.query(Magsin).all()

for tests in test:
    print(tests)
