import webbrowser


url=[

    "https://www.google.com/",
    "https://www.w3schools.com/",
    "https://www.youtube.com/?app=desktop&hl=ar&gl=EG",
   "https://www.facebook.com/?locale=ar_AR"

]


def firefox(link):

    webbrowser.get('firefox').open_new_tab(link)
    ##webbrowser.open(link,new=2)


