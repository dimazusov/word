import json
import helper
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def handler(word):
    parseVariants = morph.parse(word)

    response = getFormattedParseVariants(parseVariants)

    return json.dumps(response)

def getFormattedParseVariants(variants):
    formattedParseVariants = []

    for variant in variants:
        formattedParseVariants.append(
            helper.getFormattedParseVariant(variant)
        )

    return formattedParseVariants
