from flask import Blueprint

from db.moduls import Magsin, session

apiroutes = Blueprint('apiroutes', __name__)


@apiroutes.route("/magsin")
def magasin():
    magasins = session.query(Magsin).all()
    output = []
    for magasin in magasins:
        magasin_data = {"id": magasin.id, "dato_Id": magasin.dato_Id, "iso_uke": magasin.iso_uke, "fyllingsgrad": magasin.fyllingsgrad, "kapasitet_TWh": magasin.kapasitet_TWh,
                        "fylling_TWh": magasin.fylling_TWh, "fyllingsgrad_forrige_uke": magasin.fyllingsgrad_forrige_uke, "endring_fyllingsgrad": magasin.endring_fyllingsgrad}
        output.append(magasin_data)
    return {"Magasin": output}
