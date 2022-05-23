from flask import Blueprint, jsonify, request
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


@apiroutes.route("/magasin/<id>")
def get_magasin(id):
    magasin = session.query(Magasin).filter(Magasin.id == id).first()
    print(magasin)
    return jsonify({"id": magasin.id, "dato_Id": magasin.dato_id, "iso_uke": magasin.iso_uke, "fyllingsgrad": magasin.fyllingsgrad, "kapasitet_TWh": magasin.kapasitet_twh,
                    "fylling_TWh": magasin.fylling_twh, "fyllingsgrad_forrige_uke": magasin.fyllingsgrad_forrige_uke, "endring_fyllingsgrad": magasin.endring_fyllingsgrad, "latitude": magasin.latitude, "longitude": magasin.longitude, "name": magasin.name})


# @apiroutes.route('/magasin', methods=['POST'])
# def add_magasin():
#     magasin = Magasin(dato_Id=request.json["dato_Id"], iso_uke=request.json["iso_uke"], fyllingsgrad=request.json["fyllingsgrad"], kapasitet_TWh=request.json["kapasitet_TWh"], fylling_TWh=request.json["fylling_TWh"],
#                       fyllingsgrad_forrige_uke=request.json["fyllingsgrad_forrige_uke"], endring_fyllingsgrad=request.json["endring_fyllingsgrad"], latitude=request.json["latitude"], longitude=request.json["longitude"], name=request.json["name"])
#     session.add(magasin)
#     session.commit()
#     session.close()
#     return {"Name": magasin.name}


# @apiroutes.route("/magasin/<id>", methods="DELETE")
# def delete_magasin(id):
#     magasin = session.query(Magasin).filter(Magasin.id == id).first()
#     session.delete(magasin)
#     session.commit()
#     session.close()
