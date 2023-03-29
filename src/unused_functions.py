#
# def make_valid_link(link, parent):
#     # Обработка зависимых ссылок
#     if "http" or "https" not in link:
#         link = link.strip()
#         verifier = link[0]
#         if verifier == "/":
#             link = link[:1].replace('/', '') + link[1:]
#             link = parent + link
#             return link
#         else:
#             link = parent + link
#             return link
#     #  Обработка самостоятельных ссылок
#     else:
#         # if '/description_tags/description_http_equiv' in link:
#         #     link = parent + link
#         return link
#
#
# def parse_link(link):
#     response = requests.get(link)
#     links = re.findall('<a href="(.*?)"', response.text)
#
#     return links
