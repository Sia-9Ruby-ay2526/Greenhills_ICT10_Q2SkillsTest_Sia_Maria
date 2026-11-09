# Working with Dictionaries
from pyscript import display, document

def _details(e):
    document.getElementById('result').innerHTML = ' '
    nonmental_elements = document.getElementById('dictionary').value.lower().strip()

    # Dictionaries setup with Element Name as the Key
    atomic_mass = {
        'Hydrogen': 1.008, 'Carbon': 12.01, 'Nitrogen': 14.007, 'Oxygen': 15.999,
        'Fluorine': 19.00, 'Neon': 20.18, 'Phosphorus': 30.97, 'Sulfur': 32.07,
        'Chlorine': 35.45, 'Argon': 39.95, 'Selenium': 78.971, 'Bromine': 79.90,
        'Krypton': 83.80, 'Iodine': 126.9, 'Xenon': 131.3, 'Radon': 222,
        'Helium': 4.003, 'Oganesson': 294
    }

    atomic_number = {
        'Hydrogen': 1, 'Carbon': 6, 'Nitrogen': 7, 'Oxygen': 8,
        'Fluorine': 9, 'Neon': 10, 'Phosphorus': 15, 'Sulfur': 16,
        'Chlorine': 17, 'Argon': 18, 'Selenium': 34, 'Bromine': 35,
        'Krypton': 36, 'Iodine': 53, 'Xenon': 54, 'Radon': 86,
        'Helium': 2, 'Oganesson': 118
    }

    element_symbol = {
        'Hydrogen': H, 'Carbon': C, 'Nitrogen': N, 'Oxygen': O,
        'Fluorine': F, 'Neon': Ne, 'Phosphorus': P, 'Sulfur': S,
        'Chlorine': Cl, 'Argon': Ar, 'Selenium': Se, 'Bromine': Br,
        'Krypton': Kr, 'Iodine': I, 'Xenon': Xe, 'Radon': Rn,
        'Helium': He, 'Oganesson': Og
        }

    dict1 = {'Hydrogen': 1.008, 'Carbon': 12.01, 'Nitrogen': 14.007, 'Oxygen': 15.999,
            'Fluorine': 19.00, 'Neon': 20.18, 'Phosphorus': 30.97, 'Sulfur': 32.07,
            'Chlorine': 35.45, 'Argon': 39.95, 'Selenium': 78.971, 'Bromine': 79.90,
            'Krypton': 83.80, 'Iodine': 126.9, 'Xenon': 131.3, 'Radon': 222,
            'Helium': 4.003, 'Oganesson': 294}
    dict2 = {'Hydrogen': 1, 'Carbon': 6, 'Nitrogen': 7, 'Oxygen': 8,
            'Fluorine': 9, 'Neon': 10, 'Phosphorus': 15, 'Sulfur': 16,
            'Chlorine': 17, 'Argon': 18, 'Selenium': 34, 'Bromine': 35,
            'Krypton': 36, 'Iodine': 53, 'Xenon': 54, 'Radon': 86,
            'Helium': 2, 'Oganesson': 118}
    dict3 = {
        'Hydrogen': H, 'Carbon': C, 'Nitrogen': N, 'Oxygen': O,
        'Fluorine': F, 'Neon': Ne, 'Phosphorus': P, 'Sulfur': S,
        'Chlorine': Cl, 'Argon': Ar, 'Selenium': Se, 'Bromine': Br,
        'Krypton': Kr, 'Iodine': I, 'Xenon': Xe, 'Radon': Rn,
        'Helium': He, 'Oganesson': Og
    }

    display(dict1 | dict2 | dict3 ,target='result') #combining dictionaries
    merged_dictionary = {**dict1, **dict2, **dict3}

    display(merged_dictionary, target='result') #display result of merged dictionaries


