from typing import List
import re

from recipie import Recipe

a = Recipe.parse("""Then add @salt and @ground black pepper{} to taste.
Poke holes in @potato{2}. #Pot #oven sheet{}
Place @bacon strips{1%kg} ...""")
i = a.ingredients
c = a.cookware
print(a.fileOut())