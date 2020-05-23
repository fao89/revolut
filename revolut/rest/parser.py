import json
from flask import Blueprint, request, jsonify
from flask_simplelogin import login_required

from revolut.use_cases.json_parser import ParseJson

blueprint = Blueprint("json_parser", __name__)


@blueprint.route("/parse", methods=["POST"])
@login_required(basic=True)
def json_parser():
    query_string = request.query_string.decode("utf-8")
    sep = " "
    if "&" in query_string:
        sep = "&"
    elif "," in query_string:
        sep = ","
    elif ";" in query_string:
        sep = ";"

    nest_levels = query_string.replace("nest=", "").split(sep)

    convert = ParseJson(request.json, nest_levels)
    convert.parse()

    return jsonify(convert.output)
