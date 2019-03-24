import json
from flask import Blueprint, request, jsonify

from revolut.use_cases.json_parser import ParseJson

blueprint = Blueprint('json_parser', __name__)

@blueprint.route('/parse', methods=['POST'])
def json_parser():
    for arg in request.args.keys():
        if arg.startswith('nest_'):
            nest_levels = arg.replace('nest_', '').split("__")

    convert = ParseJson(request.json, nest_levels)
    convert.parse()

    return jsonify(convert.output)