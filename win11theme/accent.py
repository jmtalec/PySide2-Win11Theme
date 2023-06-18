from winreg import *

def get_accent_color():
    registry_path = r"SOFTWARE\Microsoft\Windows\DWM"
    try:
        key = OpenKey(HKEY_CURRENT_USER, registry_path)
        accent_color_value, _ = QueryValueEx(key, "AccentColor")
        CloseKey(key)

        # Extract individual RGB color components
        red = accent_color_value & 0xFF
        green = (accent_color_value >> 8) & 0xFF
        blue = (accent_color_value >> 16) & 0xFF

        # Format the RGB values into a hexadecimal color code
        hex_color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

        return red, green, blue, hex_color
    except FileNotFoundError:
        return None
