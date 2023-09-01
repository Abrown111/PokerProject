from Deck import Deck
from Hand import Hand
from PIL import Image, ImageDraw, ImageFont
from Card import Card

if __name__ == '__main__':
    # alex = Hand()
    # sean = Hand()
    # alexc = Hand()
    # taylor = Hand()
    # images = []
    #
    # amount = []
    # deck = Deck()
    # deck.shuffle()
    # for i in range(5):
    #     alex.add_card(deck.deal_card())
    #     sean.add_card(deck.deal_card())
    #     alexc.add_card(deck.deal_card())
    #     taylor.add_card(deck.deal_card())
    #
    # hands = [alex, alexc, sean, taylor]
    #
    # for i in range(5):
    #     filename = f'/Users/alexbrown/Downloads/drive-download-20230406T182701Z-001/{alex.cards[i].image_file_name()}'
    #     images.append(Image.open(filename))
    # for i in range(5):
    #     filename = f'/Users/alexbrown/Downloads/drive-download-20230406T182701Z-001/{alexc.cards[i].image_file_name()}'
    #     images.append(Image.open(filename))
    # for i in range(5):
    #     filename = f'/Users/alexbrown/Downloads/drive-download-20230406T182701Z-001/{sean.cards[i].image_file_name()}'
    #     images.append(Image.open(filename))
    # for i in range(5):
    #     filename = f'/Users/alexbrown/Downloads/drive-download-20230406T182701Z-001/{taylor.cards[i].image_file_name()}'
    #     images.append(Image.open(filename))
    #
    # new_img = Image.new('RGB', (6*images[0].width, 4*images[0].height))
    # print(images)
    # x_change = int(new_img.width/6)
    # y_change = int(new_img.height/4)
    # counter = 0
    # for y in range(0, new_img.height, y_change):
    #     for x in range(0, 5*x_change, x_change):
    #         try:
    #             new_img.paste(images[counter], (x, y))
    #         except IndexError:
    #             print("counter weird")
    #         finally:
    #             counter += 1
    #
    # # new_img.show()
    #
    # winners = []
    # winner = 0
    #
    # print(alex.cards, alex.get_hand_type())
    # print(sean.cards, sean.get_hand_type())
    # print(taylor.cards, taylor.get_hand_type())
    # print(alexc.cards, alexc.get_hand_type())
    # if sean.compare(taylor) == -1:
    #     winners.append(taylor)
    # elif sean.compare(taylor) == 1:
    #     winners.append(sean)
    # else:
    #     print('tie')
    #
    # if alex.compare(alexc) == -1:
    #     winners.append(alexc)
    # elif alex.compare(alexc) == 1:
    #     winners.append(alex)
    # else:
    #     print('tie')
    #
    # end = []
    #
    # try:
    #     if winners[0].compare(winners[1]) == -1:
    #         print(f'{winners[1].cards} wins!')
    #         end.append(winners[1])
    #     elif winners[0].compare(winners[1]) == 1:
    #         print(f'{winners[0].cards} wins!')
    #         end.append(winners[0])
    #     else:
    #         print('tie')
    # except IndexError:
    #     winners = []
    #
    # print(new_img.width, new_img.height)
    # draw_img = ImageDraw.Draw(new_img)
    #
    # news = [x for x in hands if x.cards == end[0].cards]
    #
    # for i in range(4):
    #     draw_img.text((510, 72.5+145*i), hands[i].get_hand_type(), (255, 255, 255))
    #     if i == hands.index(news[0]):
    #         draw_img.text((510, 90 + 145*i), 'WINNER!', (203, 14, 17))
    #
    # new_img.save("Poker_img.jpg")
    # saved_img = Image.open("/Users/alexbrown/PycharmProjects/PokerProject/Poker_img.jpg")
    # saved_img.show()

    j = Hand()
    j.add_card(Card('diamonds', 12))
    j.add_card(Card('hearts', 7))
    j.add_card(Card('spades', 9))
    j.add_card(Card('clubs', 4))
    j.add_card(Card('diamonds', 14))

    h = Hand()
    h.add_card(Card('hearts', 12))
    h.add_card(Card('clubs', 7))
    h.add_card(Card('diamonds', 9))
    h.add_card(Card('spades', 11))
    h.add_card(Card('hearts', 10))

    print(j.compare(h))



