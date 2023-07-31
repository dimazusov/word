import json
from flask import request
import helper
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def handler():
    data = json.loads(request.data)

    errors = validate(data)
    if len(errors) > 0:
        return json.dumps({"errors": errors})

    parseVariants = morph.parse(data["word"])
    selectedVariant = getSelectedVariants(parseVariants, data["normalForm"])
    if selectedVariant == None:
        return json.dumps({"errors": ["selected variant not found"]})

    declensionVariant = selectedVariant.inflect({data["inflect"]})

    return helper.getFormattedParseVariant(declensionVariant)

def validate(data):
    errors = []
    requiredFields = ["word", "normalForm", "inflect"]
    for fieldName in requiredFields:
        if data.get(fieldName) == None:
            errors.append("field " + fieldName + " is required")

    return errors

def getSelectedVariants(variants, normalForm):
    for variant in variants:
        if variant.normal_form == normalForm:
           return variant

    return None