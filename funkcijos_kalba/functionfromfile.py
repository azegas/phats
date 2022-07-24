from functions import filter_countries  # import only one function
from functions import get_first_country
# from folder.functions import get_first_country  # example jeigu buna kitame folderyje
# import functions                          # import all functions(tuomet nereikia FUNCTIONS.) rasyti

# jeigu funkcija kitame folderyje nei present folder
# import sys
# sys.path.append('/opt/python/codefather/python_import/lib/')  # absolute path

countries = ['Italy', 'United Kingdom', 'Spain', 'France', 'Sweden']

print(filter_countries(countries, 'S'))
print(get_first_country(countries))
