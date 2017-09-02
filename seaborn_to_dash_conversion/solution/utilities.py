def changeovers(items):
    """
    Used to retrieve a list of integers each of which represents the
    delivery number at which the innings/days change.

    @param data: dataframe representing the match data
    @return: list of integers
    """
    indexes = []
    previous = items[0]
    for index, x in enumerate(items):
        if x != previous:
            indexes.append(index)
            previous = x
    return indexes


def print_inning_lines(delivery_numbers, y0, y1, color='grey'):
    """
    Generates vertical plotly lines that can be added to graphs. This is done
    by setting it equal to the *shapes* parameter of
    *dash_core_components.Graph*.

    @param delivery_numbers: (list), of integers, each of which represent the
                             point on the x axis where the vertical line
                             should be placed
    @param y0: (integer), the lines starting point on the y axis
    @param y1: (integer), the lines ending point on the y axis
    @param color: (string), the color of the line
    @return: (list of dicts), each dict represents the code needed to
             generate a single line on the graph
    """

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
