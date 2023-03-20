from typing import Union

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Response, tuple[Response, int]]:
    data = request.json
    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    first_result = build_query(
        cmd=validated_data['cmd1'],
        value=validated_data['value1'],
        file_name=validated_data['file_name'],
        data=None,
    )
    second_result = build_query(
        cmd=validated_data['cmd2'],
        value=validated_data['value2'],
        file_name=validated_data['file_name'],
        data=first_result,
    )
    return jsonify(second_result)
