def getFormattedParseVariant(variant):
    formattedVariant = {
        "word": variant.word,
        "normalForm": variant.normal_form,
        "score": variant.score,
        "positionInSentence": 0,
        "tag": {
            "pos": variant.tag.POS,
            "animacy": variant.tag.animacy,
            "aspect": variant.tag.aspect,
            "case": variant.tag.case,
            "gender": variant.tag.gender,
            "involvement": variant.tag.involvement,
            "mood": variant.tag.mood,
            "number": variant.tag.number,
            "person": variant.tag.person,
            "tense": variant.tag.tense,
            "transitivity": variant.tag.transitivity,
            "voice": variant.tag.voice,
        }
    }

    for tagName in formattedVariant["tag"]:
        if formattedVariant["tag"][tagName] == None:
            formattedVariant["tag"][tagName] = ""

    return formattedVariant