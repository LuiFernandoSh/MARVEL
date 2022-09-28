def get(json, atribute):
    try:
        return json[atribute]

    except Exception:
        return None


def get_or_error(json, attribute):
    try:
        return json[attribute]

    except Exception:
        raise Exception(f"{attribute} is missing.")
