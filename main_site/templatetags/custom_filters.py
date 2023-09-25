from django import template

register = template.Library()

@register.filter
def format_phone_number(phone_number):
    if phone_number:
        # Remove all non-digit characters from the phone number
        digits = [char for char in phone_number if char.isdigit()]

        # Check if it's a valid phone number (e.g., 10 or 11 digits for North America)
        if len(digits) == 10:
            formatted_phone = "({}{}{}) {}{}{}-{}{}{}{}".format(*digits)
            return formatted_phone
        elif len(digits) == 11 and digits[0] == "1":
            formatted_phone = "1 ({}{}{}) {}{}{}-{}{}{}{}".format(*digits[1:])
            return formatted_phone

    return phone_number
