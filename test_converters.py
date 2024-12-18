import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'170 cm is {converters.cm_to_m(170)}m')
print(f'140 cm is {converters.cm_to_inch(140)} inch')
print(f'3 feet and 5 inch is {converters.feet_and_inch_to_cm(3, 5)}cm')
