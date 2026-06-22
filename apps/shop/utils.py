def convert_english_to_persian_digits(value):
    english_digits = "0123456789"
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"

    translation_table = str.maketrans(english_digits, persian_digits)
    return str(value).translate(translation_table)

def format_price_toman(value):
    formated_value = f'{value:,.0f}'
    persian_value = convert_english_to_persian_digits(formated_value)
    return f' {persian_value} تومان'
result = format_price_toman(12333)
print(result)