from ninetynine.hand import Hand

def test_can_add_card():
    hand = Hand('red')
    hand.add_card(55)
    assert hand.cards == [55]

def test_can_remove_card():
    hand = Hand('red')
    hand.add_card(26)

def test_cannot_add_card_when_full():
    hand = Hand('red')
    for n in range(6):
        try:
            hand.add_card(n)
        except ValueError:
            return True
    assert False

def test_cannot_remove_card_not_in_hand():
    hand = Hand('red')
    hand.add_card(5)
    hand.add_card(99)
    try:
        hand.remove_card(66)
    except ValueError:
        return True
    assert False