from flask import Blueprint

from db.moduls import Magasin, session

apiroutes = Blueprint('apiroutes', __name__)


@apiroutes.route("/magasin")
def magasin():
    magasins = session.query(Magasin).all()
    output = []
    for magasin in magasins:
        magasin_data = {"id": magasin.id, "dato_Id": magasin.dato_id, "iso_uke": magasin.iso_uke, "fyllingsgrad": magasin.fyllingsgrad, "kapasitet_TWh": magasin.kapasitet_twh,
                        "fylling_TWh": magasin.fylling_twh, "fyllingsgrad_forrige_uke": magasin.fyllingsgrad_forrige_uke, "endring_fyllingsgrad": magasin.endring_fyllingsgrad, "latitude": magasin.latitude, "longitude": magasin.longitude, "name": magasin.name}
        output.append(magasin_data)
    return {"Magasin": output}
