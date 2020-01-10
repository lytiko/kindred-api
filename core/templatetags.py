from django import template
import datetime
import math

register = template.Library()

def pluralize(s, i):
    return s if i == 1 else f"{s}s"

@register.filter(name="time_offset")
def time_offset(date):
    """."""

    if not date: return "-"
    today = datetime.datetime.now().date()
    offset = (today - date).days
    abs_offset = abs(offset)
    suffix = " ago" if offset > 0 else " from now"
    if offset == 0:
        return "Today"
    if abs_offset < 7:
        return f"{abs_offset} {pluralize('day', abs_offset)}{suffix}"
    if abs_offset < 90:
        weeks = round(abs_offset / 7)
        return f"{weeks} {pluralize('week', weeks)} {suffix}"
    start, end = min(date, today), max(date, today)
    end_months = end.month
    start_months = (12 - start.month) if start.year != end.year else 0
    full_months = (end.year - start.year - 1) * 12
    months = start_months + end_months + full_months
    if months < 12:
        return f"{months} {pluralize('month', months)} {suffix}"
    if months < 48:
        years = months // 12
        months = months - (12 * years)
        if months:
            return f"{years} {pluralize('year', years)}, {months} {pluralize('month', months)} {suffix}"
        else:
            return f"{years} {pluralize('year', years)} {suffix}"
    years = round(months / 12)
    return f"{years} {pluralize('year', years)} {suffix}"