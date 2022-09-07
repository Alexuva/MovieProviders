from requests_html import HTMLSession


class Movie():

    def searchproviders(self, movieid):
        s = HTMLSession()
        r = s.get(f"https://www.themoviedb.org/movie/{movieid}/watch?language=es-ES")
        print(r.status_code)
        providersList = []
        providersDiv = r.html.find("div.ott_provider")
        for providerDivBueno in providersDiv:
            titulo = providerDivBueno.find("h3", first=True)
            if titulo.text == "Stream":
                info = providerDivBueno.find("li.ott_filter_best_price")
                for provider in info:
                    link = provider.find("a", first=True)
                    providerLink = link.attrs["href"]
                    providerName = link.attrs["title"].split("en")[1]
                    providerPick = "https://www.themoviedb.org/" + link.find("img", first=True).attrs["src"]

                    provider = {
                        "Proveedor": f"{providerName}",
                        "Link": f"{providerLink}",
                        "Imagen": f"{providerPick}"
                    }

                    providersList.append(provider)

        return providersList
