from requests_html import HTMLSession


class Tv():
    def searchproviders(self, tvid):
        url = f"https://www.themoviedb.org/tv/{tvid}/watch?locale=ES&language=es-ES"
        s = HTMLSession()
        r = s.get(url)
        if r.status_code != 200:
            return [
                {
                    "Error": "El título que buscas no existe o no es una serie "
                }
            ]

        providersDiv = r.html.find("div.ott_provider")
        providersList = []
        for providerDivBueno in providersDiv:
            titulo = providerDivBueno.find("h3", first=True)
            if titulo.text == "Stream" or titulo.text == "Gratis":
                info = providerDivBueno.find("li.ott_filter_best_price")
                for provider in info:
                    link = provider.find("a", first=True)
                    providerLink = link.attrs["href"]
                    providerName = link.attrs["title"].split("en")[1]
                    providerPick = "https://www.themoviedb.org/" + link.find("img", first=True).attrs["src"]

                    proveedor = {
                        "Proveedor": f"{providerName}",
                        "Link": f"{providerLink}",
                        "Imagen": f"{providerPick}"
                    }

                    providersList.append(proveedor)

        return providersList