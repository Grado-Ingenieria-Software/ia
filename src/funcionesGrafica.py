def generaGrafica(elementos):
    s = ""
    for n in elementos:
        s = s + "," + str(n)
    url = "https://image-charts.com/chart?cht=lc&chd=t:" + s[1:] + "&chco=FF0000&chs=600x300"
    return url
