from urllib import request
from project import Project
import tomli




class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        toml_dict = tomli.loads(content)
        print(toml_dict)

        print()
        nimi = toml_dict['tool']['poetry']['name']
        kuvaus = toml_dict['tool']['poetry']['description']
        lisenssi = toml_dict['tool']['poetry']['license']

        tekijät = toml_dict['tool']['poetry']['authors']
        
        riippuvuudet = toml_dict['tool']['poetry']['dependencies']
        
        dev_riippuvuudet = toml_dict['tool']['poetry']['group']['dev']['dependencies']

        



        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, lisenssi, tekijät, riippuvuudet, dev_riippuvuudet)
