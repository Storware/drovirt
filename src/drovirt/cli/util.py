import click
import datetime


class Context():
    pass


pass_context = click.make_pass_decorator(Context, ensure=True)


def display_output(value, details=False):
    if isinstance(value, list) and not details:
        click.echo(display_table(value))
    elif isinstance(value, list):
        click.echo(display_detail(value[0]))
    else:
        click.echo(display_detail(value))


def display_detail(object):
    output = ''
    for k, v in object.to_dict().items():
        output += f'{k.upper()}: {display_string(v)}\n'
    return output


def display_table(objects):
    output = ""
    separator = " | "
    items = []
    column_width = {}
    for o in objects:
        item = o.to_dict()
        for k, v in item.items():
            item[k] = display_string(v)
            if k not in column_width or column_width[k] < len(item[k]) or column_width[k] < len(k):
                column_width[k] = max(len(item[k]), len(k))
        items.append(item)

    # display rows titles
    line = []
    for k, v in column_width.items():
        line.append(k.upper().ljust(v))
    output += f"{separator.join(line)}\n"
    output += len(output) * '-' + '\n'

    # display data
    for item in items:
        line = []
        for k, v in item.items():
            line.append(v.ljust(column_width[k]))
        output += f"{separator.join(line)}\n"

    return output


def display_string(value):
    if isinstance(value, datetime.datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S UTC")
    return str(value)
