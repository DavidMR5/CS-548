#!/usr/bin/env python

import jsonpatch
import copy
import base64
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def inject_label(obj, label):
    if "metadata" not in obj:
        obj["metadata"] = {}
    if "labels" not in obj["metadata"]:
        obj["metadata"]["labels"] = {}
    obj["metadata"]["labels"][label] = "true"


@app.route('/mutate', methods=['POST'])
def mutate():
    data = request.get_json()

    uid = data["request"]["uid"]
    obj = copy.deepcopy(data["request"]["object"])

    inject_label(obj, os.getenv("CUSTOM_LABEL", "custom-label"))

    patch = jsonpatch.JsonPatch.from_diff(
        data["request"]["object"],
        obj
    )

    encoded_patch = base64.b64encode(
        patch.to_string().encode("utf-8")
    ).decode("utf-8")

    return jsonify({
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": uid,
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": encoded_patch
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)