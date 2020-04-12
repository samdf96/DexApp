from kivy.graphics import Color
from kivy.utils import get_color_from_hex

ColorDictionary = {
    'bug': ['C6D16E', 'A8B820', '6D7815'],
    'dark': ['A29288', '705848', '49392F'],
    'dragon': ['A27DFA', '7038F8', '4924A1'],
    'electric': ['FAE078', 'F8D030', 'A1871F'],
    'fairy': ['F4BDC9', 'EE99AC', '9B6470'],
    'fighting': ['D67873', 'C03028', '7D1F1A'],
    'fire': ['F5AC78', 'F08030', '9C531F'],
    'flying': ['C6B7F5', 'A890F0', '6D5E9C'],
    'ghost': ['A292BC', '705898', '493963'],
    'grass': ['A7DB8D', '78C850', '4E8234'],
    'ground': ['EBD69D', 'E0C068', '927D44'],
    'ice': ['BCE6E6', '98D8D8', '638D8D'],
    'normal': ['C6C6A7', 'A8A878', '6D6D4E'],
    'poison': ['C183C1', 'A040A0', '682A68'],
    'psychic': ['FA92B2', 'F85888', 'A13959'],
    'rock': ['D1C17D', 'B8A038', '786824'],
    'steel': ['D1D1E0', 'B8B8D0', '787887'],
    'water': ['9DB7F5', '6890F0', '445E9C'],
    '???': ['9DC1B7', '68A090', '44685E']
}

def ColorPicker(color, tone, export_color=False):
    """
    Takes a pokemon type and tone, and returns a kivy.graphics.Color object.

    Parameters
    ----------
    color : str
        This takes the pokemon type. Must be lowercase.
    tone : str, ['light', 'regular', 'dark']

    Returns
    -------
    list

    """
    # Grab List from Dictionary
    c_list = ColorDictionary[color]
    # Grabbing specific Tone
    if tone == 'light':
        c_hex = c_list[0]
    if tone == 'regular':
        c_hex = c_list[1]
    if tone == 'dark':
        c_hex = c_list[2]
    # Convert to RGBA and return Color object
    c = get_color_from_hex(c_hex)
    if export_color:
        return Color(c[0], c[1], c[2], c[3])
    else:
        return [c[0], c[1], c[2], c[3]]
