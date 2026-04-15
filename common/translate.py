def paramsMapping(pl):
    params = {
        "Wilgotność":"humidity",
        "Ciśnienie":"pressure",
        "Prędkość Wiatru":"wind_speed",
        "Temperatura":"temp"
    }

    value = params[pl]
    return value