import justpy as jp

from webpage.about import About
from webpage.dictionary import Dictionary
from webpage.home import Home

jp.Route(Home.path,Home.serve)
jp.Route(About.path,About.serve)
jp.Route(Dictionary.path,Dictionary.serve)
jp.justpy(port=8003)