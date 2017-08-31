def get_innings_changes(data):
    delivery_numbers = []

    for i in range(2, 1 + len(data.inn.unique())):
        delivery_numbers.append(data[data.inn == i]['deliv'].idxmin())

    return delivery_numbers


def print_inning_lines(delivery_numbers, y0, y1, color='grey'):
    lines = []
    for number in delivery_numbers:
        lines.append(
            {
                'type': 'line',
                'x0': number,
                'y0': y0,
                'x1': number,
                'y1': y1,
                'line': {
                    'width': 1,
                    'color': color
                }
            }
        )

    return lines
