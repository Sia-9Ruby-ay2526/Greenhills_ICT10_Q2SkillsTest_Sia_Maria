
# Working with Dictionaries
from pyscript import display, document

def element_details(e):
    document.getElementById('result').innerHTML = ' '
    nonmental_elements = document.getElementById('dictionary').value.lower().strip()

    # Dictionaries setup with Element Name as the Key
    atomic_mass = {
        'hydrogen': 1.008, 'carbon': 12.01, 'nitrogen': 14.007, 'oxygen': 15.999,
        'fluorine': 19.00, 'neon': 20.18, 'phosphorus': 30.97, 'sulfur': 32.07,
        'chlorine': 35.45, 'argon': 39.95, 'selenium': 78.971, 'bromine': 79.90,
        'krypton': 83.80, 'iodine': 126.9, 'xenon': 131.3, 'radon': 222,
        'helium': 4.003, 'oganesson': 294
    }

    atomic_number = {
        'hydrogen': 1, 'carbon': 6, 'nitrogen': 7, 'oxygen': 8,
        'fluorine': 9, 'neon': 10, 'phosphorus': 15, 'sulfur': 16,
        'chlorine': 17, 'argon': 18, 'selenium': 34, 'bromine': 35,
        'krypton': 36, 'iodine': 53, 'xenon': 54, 'radon': 86,
        'helium': 2, 'oganesson': 118
    }

    element_symbol = {
        'hydrogen': 'H', 'carbon': 'C', 'nitrogen': 'N', 'oxygen': 'O',
        'fluorine': 'F', 'neon': 'Ne', 'phosphorus': 'P', 'sulfur': 'S',
        'chlorine': 'Cl', 'argon': 'Ar', 'selenium': 'Se', 'bromine': 'Br',
        'krypton': 'Kr', 'iodine': 'I', 'xenon': 'Xe', 'radon': 'Rn',
        'helium': 'He', 'oganesson': 'Og'
    }

    dict1 = atomic_mass
    dict2 = atomic_number
    dict3 = element_symbol

    # Combining dictionaries
    display(dict1 | dict2 | dict3, target='result')

    merged_dictionary = {**dict1, **dict2, **dict3}

    #display dictionary 
    display(merged_dictionary, target='result')


