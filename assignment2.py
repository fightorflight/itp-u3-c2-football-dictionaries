import csv

def read_squad_file(file_name='squads.csv'):
    squad = []
    with open(file_name) as fp:
        reader = csv.reader(fp)
        for line in reader:
            squad.append(line)

    return squad

def players_as_dictionaries(SQUADS_DATA):
    complete_list = []
    for element in SQUADS_DATA:
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
    return (complete_list)
        
players_as_dictionaries(read_squad_file())