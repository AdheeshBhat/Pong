import Setup
#top five
#goes through top five list and writes list of top five scores
def top_five():
  Setup.app.fill(73,163,242)
  Setup.app.rect(150,20,250,100,10)
  Setup.app.fill(0,0,0)
  Setup.app.textSize(15)
  Setup.app.text("maxscore 1: " + Setup.list_item1, 240, 40)
  Setup.app.text("maxscore 2: " + Setup.list_item2, 240, 60)
  Setup.app.text("maxscore 3: " + Setup.list_item3, 240, 80)
  Setup.app.text("maxscore 4: " + Setup.list_item4, 240, 100)
  Setup.app.text("maxscore 5: " + Setup.list_item5, 240, 120)