from constants import *

def check_request(request):
    request = request.lower()
    result = NOT_FOUND
    if "футболист" not in request and\
        "футболистов" not in request and\
        "футболисты" not in request:
        print("В запросе должна идти речь о футболистах!\n")
    elif "трансферная стоимость" not in request and\
            "трансферной стоимостью" not in request and\
            "стоимостью" not in request and\
            "стоимость" not in request:
        print("В запросе должна идти речь о трансферная стоимость")
    elif "не очень низкого" in request:
        result = NOT_VERY_LOW
    elif "не низкой" in request:
        result = NOT_LOW
    elif "не средней" in request:
        result = NOT_AVERAGE
    elif "очень высокой" in request or\
            "очень высокую" in request:
        result = VERY_HIGH
    elif "не высокой" in request:
        result = NOT_HIGH
    elif "не очень высокой" in request:
        result = NOT_VERY_HIGH
    elif "очень низкой" in request or "очень низкая" in request:
        result = VERY_LOW
    elif "низкой" in request:
        result = LOW
    elif "средней" in request:
        result = AVERAGE
    elif "высокой" in request:
        result = HIGH
    else:
        print("Речь должна идти о каком-то из термов!")
    return result

def get_interval(term):
    is_not = False
    interval = []
    if term > 5:
        is_not = True
    term = term % 5
    if term == VERY_LOW:
        interval = [0, 10]
    elif term == LOW:
        interval = [11, 50]
    elif term == AVERAGE:
        interval = [51, 110]
    elif term == HIGH:
        interval = [111, 157]
    else:
        interval = [158, 200]
    return interval, is_not

def search(data, interval, is_not):
    result = []
    start = interval[0] * 1e6
    end = interval[1] * 1e6
    for footballer in data:
        in_interval = False
        if start <= footballer.price <= end:
            in_interval = True
        if is_not != in_interval:
            result.append(footballer)
    return result