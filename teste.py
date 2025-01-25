from db import SessionLocal, Saint, GenderEnum

db = SessionLocal()

new_saint = Saint(
    saint_day='01/02/2024',
    name="São Francisco de Assis",
    gender=GenderEnum.Male,
    patron_city="Assis",
    born=1181,
    died=1226,
    birthplace="Assis",
    deathplace="Assis",
    protector_of="animais, meio ambiente",
)

db.add(new_saint)
db.commit()
db.close()