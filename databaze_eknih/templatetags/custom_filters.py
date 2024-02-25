from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter(name="strip_image_tags")
def strip_image_tags(value):
    """
    Pokud p tag obsahuje string 'img src' tak je celý tag smazán z náhledu na indexu.
    """
    soup = BeautifulSoup(value, "html.parser")
    p = soup.find_all("p")
    for p_tag in p:
        if "img src" in p_tag.text:
            p_tag.extract()
    # print(p)
    return soup