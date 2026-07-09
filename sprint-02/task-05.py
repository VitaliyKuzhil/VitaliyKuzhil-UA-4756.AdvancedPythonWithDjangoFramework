import re

pattern = r'([a-z]{2}_[a-z]*),(\d{5})'


def max_population(data):


    city_populations = {name: int(population) for line in data for name, population in re.findall(pattern, line)}

    max_city_population = max(city_populations, key=city_populations.get)

    return max_city_population, city_populations[max_city_population]

data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))