class CardGame:


  def check_for_ace(self, card):
    if card.value == 1: #should be ==, = is to assign a variable but this is checking if values are equals
      return True
    else: #missing colon
      return False
   

  def highest_card(self, card1, card2): #dif instead of def when defining the function, comma missing after card1
    if card1.value > card2.value: #not indented
        return card1 #should be return card1
    else:
        return card2
  


def cards_total(self, cards):
  total = 0 # should be total = 0 to start a running total. Currently cards will be added to nothing
  for card in cards:
    total += card.value
    return "You have a total of" + total