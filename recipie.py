from typing import List
from ingredient import Ingredient

from cookware import Cookware
from step import Step


class Recipe():
    def __init__(self) -> None:
        #self.ingredients : List[Ingredient] = []
        #self.cookware : List[Cookware] = []
        self.steps : List[Step] = []

    @property
    def ingredients(self) -> List[Ingredient]:
        ingredients = {}
        for step in self.steps:
            for ingredient in step.ingredients:
                if ingredient.name not in ingredients:
                    ingredients[ingredient.name] = ingredient
                else:
                    ingredients[ingredient.name].amount += ingredient.amount #TODO: convert units
        return list(ingredients.values())

    @property
    def cookware(self) -> List[Cookware]:
        cw = {}
        for step in self.steps:
            for cookware in step.cookware:
                if cookware.name not in cw:
                    cw[cookware.name] = cookware
        return list(cw.values())

    def parse(input:str) -> None:
        r = Recipe()
        r.steps = list(map((lambda x: Step.parse(x)), input.split("\n")))
        return r

    def fileOut(self) -> str:
        return "\n".join(map((lambda x: x.fileOut()), self.steps))