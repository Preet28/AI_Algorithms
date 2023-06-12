colors = ['Red', 'Blue', 'Green']
states = ['Telangana', 'Karnataka', 'TamilNadu', 'Kerala']
neighbours = {}
neighbours['Telangana'] = ['TamilNadu','Karnataka']
neighbours['Karnataka'] = ['Telangana','Kerala','TamilNadu']
neighbours['TamilNadu'] = ['Kerala','Karnataka','Telangana']
neighbours['Kerala'] = ['TamilNadu','Karnataka']

colors_of_states = {}


def promising(state, color):
    for neighbour in neighbours.get(state):
        color_of_neighbour = colors_of_states.get(neighbour)
        if color_of_neighbour == color:
            return False
    return True    

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for i in states:
        colors_of_states[i] = get_color_for_state(i)
    print(colors_of_states)

main()
