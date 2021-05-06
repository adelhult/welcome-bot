from bs4 import BeautifulSoup
from requests import get

def convert_list(soup):
    """Convert a menu list into a string"""
    try:
        lines = []
        for i in soup.find_all("li"):
            lines.append(f"**{i.contents[0].string}**   -   {i.contents[1]}")
    except Exception:
        return "Hittade ingen meny, kanske stängt idag?"    
    
    return "\n".join(lines)
      

def get_menu(query: str) -> str:
    # clean the query
    q = query.lower().strip().replace("'", "").replace(".", "")

    URL = "https://mat.dtek.se/"
    try:
        html = get(URL, timeout=20).text
    except Exception:
        return "Misslyckades med att läsa in mat.dtek.se"

    try: 

        soup = BeautifulSoup(html, 'html.parser')
        menus = soup.find_all("ul", {"class": "food-menu"})
        result = []

        if "kår" in q:
            result.append(
                "**Kårresturangen**\n"+
                convert_list(menus[0]))
        
        if "express" in q:
            result.append(
                "**Express Johanneberg**\n"+
                convert_list(menus[1]))

        if "smak" in q:
            result.append(
                "**S.M.A.K**\n"+
                convert_list(menus[2]))
        
        if "einstein" in q:
            result.append(
                "**Einstein**\n"+
                convert_list(menus[3]))
        
        if "kitchen" in q:
            result.append(
                "**L's Kitchen**\n"+
                convert_list(menus[4]))

        if "wijkanders" in q:
            result.append(
                "**Wijkanders**\n"+
                convert_list(menus[5]))

        if not result:
            # get the menu for every place if their query didnt match
            return get_menu("kår express smak einstein kitchen wijkanders")

        return "\n\n".join(result)
    except Exception:
        return "Misslyckades med att tolka menyerna"
