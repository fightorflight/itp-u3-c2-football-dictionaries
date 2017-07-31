complete_list = []

list_o_data = [
  [
    "1",                                     # Number
    "GK",                                    # Position
    "Juan Botasso",                          # Name
    "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
    "",                                      # Caps
    "Quilmes",                               # Club
    "Argentina",                             # Country (Players Country)
    "Argentina",                             # Club Country
    "1930"                                   # Year
  ],
  [
    "9",
    "FW",
    "Roberto Cherro",
    "(1907-02-23)23 February 1907 (aged 23)",
    "",
    "Boca Juniors",
    "Argentina",
    "Argentina",
    "1930"
  ]
  # More Players...
]

def squads_data(list_o_data):
    for element in list_o_data:
        a_dict = {}
        a_dict['number'] = element[0]
        a_dict['position'] = element[1]
        a_dict['name'] = element[2]
        a_dict['date_of_birth'] = element[3]
        a_dict['caps'] = element[4]
        a_dict['club'] = element[5]
        a_dict['country'] = element[6]
        a_dict['club_country'] = element[7]
        a_dict['year'] = element[8]
        complete_list.append(a_dict)
    if a_dict['position'] = 'GK'
    
        print (complete_list)
    


squads_data(list_o_data)




