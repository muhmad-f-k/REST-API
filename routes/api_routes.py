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


@apiroutes.route('/magasin', methods=['POST'])
def add_magasin():
    magasin = Magasin(iso_uke=request.json["iso_uke"], fyllingsgrad=request.json["fyllingsgrad"], kapasitet_twh=request.json["kapasitet_twh"], fylling_twh=request.json["fylling_twh"],
                      fyllingsgrad_forrige_uke=request.json["fyllingsgrad_forrige_uke"], endring_fyllingsgrad=request.json["endring_fyllingsgrad"], latitude=request.json["latitude"], longitude=request.json["longitude"], name=request.json["name"])
    session.add(magasin)
    session.commit()
    return {"Name": magasin.name, "massage": "Er lagt til"}


@apiroutes.route('/magasin/<id>', methods=['PUT'])
def update_magasin(id):
    magasin_id = session.query(Magasin).filter(Magasin.id == id).first()

    if magasin_id is None:
        return {"erro": "Magasin finnes ikke"}

    iso_uke = request.json["iso_uke"]
    fyllingsgrad = request.json["fyllingsgrad"]
    kapasitet_twh = request.json["kapasitet_twh"]
    fylling_twh = request.json["fylling_twh"]
    fyllingsgrad_forrige_uke = request.json["fyllingsgrad_forrige_uke"]
    endring_fyllingsgrad = request.json["endring_fyllingsgrad"]
    latitude = request.json["latitude"]
    longitude = request.json["longitude"]
    name = request.json["name"]
    magasin_id.iso_uke = iso_uke
    magasin_id.fyllingsgrad = fyllingsgrad
    magasin_id.kapasitet_twh = kapasitet_twh
    magasin_id.fylling_twh = fylling_twh
    magasin_id.fyllingsgrad_forrige_uke = fyllingsgrad_forrige_uke
    magasin_id.endring_fyllingsgrad = endring_fyllingsgrad
    magasin_id.latitude = latitude
    magasin_id.longitude = longitude
    magasin_id.name = name
    session.commit()
    return {"Name": magasin_id.name, "massage": "Er oppdatert"}


@apiroutes.route("/magasin/<id>", methods=["DELETE"])
def delete_magasin(id):
    magasin = session.query(Magasin).filter(Magasin.id == id).first()
    if magasin is None:
        return {"erro": "Magasin finnes ikke"}
    session.delete(magasin)
    session.commit()
    return {"Name": magasin.name, "massage": "Er slettet"}
