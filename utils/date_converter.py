from datetime import date


def date_converter(date_str: str) -> date or None:
    try:
        list_date = date_str.split('-')

        year: str = list_date[0]
        month: str = list_date[1]
        day: str = list_date[2]

        date_converted: date = date(int(year), int(month), int(day))
        return date_converted

    except IndexError:
        return None

    except AttributeError:
        return None
