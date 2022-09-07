from requests_html import HTMLSession


class Movie():
    def searchproviders(self, movieid):
        url = f"https://www.themoviedb.org/movie/{movieid}/watch?language=es-ES"
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        providersDiv = r.html.find("div.ott_provider")
        providersList = []
        for providerDivBueno in providersDiv:
            titulo = providerDivBueno.find("h3", first=True)
            if titulo.text == "Stream":
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
        print(providersList)
        return providersList

peli = Movie()

peli.searchproviders(767)