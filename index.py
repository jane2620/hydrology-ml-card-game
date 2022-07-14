
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session
import numpy as np
from card import Card
from urllib.parse import urlparse

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response


@app.route('/cards', methods=['GET', 'POST'])
def card_page():
    num_train_cards = request.args.get('num_train_cards')
    num_test_cards = request.args.get('num_test_cards')
    var_type = request.args.get('variable_type')

    train_cards, test_cards = get_cards_2(num_train_cards, 
    num_test_cards)

    if (var_type == "wtd_vars"): card_html = 'cards.html'
    else: card_html = 'fakecards.html'
    
    html = render_template(card_html, train_cards=train_cards, 
                            test_cards=test_cards)
    response = make_response(html)
    return response


def get_value(dist):
    out = np.random.rand()
    if (out < dist[0]):
        return "Low"
    elif (out < dist[1]):
        return "Medium"
    else:
        return "High"


def get_cards(num_cards, isTrain):
    if (num_cards is None or num_cards == ""): print("Oh no!")
    cards = []
    n_cards = int(num_cards)


    k_high = [.2, .5, 1]
    k_low = [.5, .8, 1]
    ET_low = [.2, .5, 1]
    ET_high = [.5, .8, 1]
    P_high = [.2, .5, 1]
    P_low = [.5, .8, 1]
    topo_high = [.2, .5, 1]
    topo_low = [.5, .8, 1]

    for i in range(n_cards):
        if (np.random.rand() < 0.5):
            # low WTD
            k = get_value(k_low)
            ET = get_value(ET_low)
            P = get_value(P_low)
            topo = get_value(topo_low)
            wtd = "Low"
            if (not isTrain): wtd = ""
            current_card = Card(k, ET, P, topo, wtd)
            
        else:
            # high WTD
            k = get_value(k_high)
            ET = get_value(ET_high)
            P = get_value(P_high)
            topo = get_value(topo_high)
            wtd = "High"
            if (not isTrain): wtd = ""
            current_card = Card(k, ET, P, topo, wtd)

        cards.append(current_card)


    return cards


def get_low():
    val = np.random.uniform(0, 0.63)
    val = int(val * 100) // 29
    if (val == 0): return "Low"
    elif (val == 1): return "Medium"
    else: return "High"

def get_high():
    val = np.random.uniform(0.37, 1)
    val = int((val * 100)-15) // 29
    if (val == 0): return "Low"
    elif (val == 1): return "Medium"
    else: return "High"

def low():
    val = (np.random.uniform(0,1) * 100) // 40
    if (val == 0): return "Medium"
    else: return "Low"

def high():
    val =  (np.random.uniform(0,1) * 100) // 40
    if (val == 0): return "Medium"
    else: return "High"

# def __init__(self, k, temp, precip, slope, wtd)
def get_cards_2(num_train_cards, num_test_cards):
    train_cards = []
    test_cards = []

    for i in range(int(num_train_cards)) :
        if (np.random.rand() < 0.5):
            wtd = "Low"
            current_card = Card(low(), high(), low(), high(), wtd, i + 1)
        else:
            wtd = "High"
            current_card = Card(high(), low(), high(), low(), wtd, i + 1)

        train_cards.append(current_card)

    for i in range(int(num_test_cards)) :
        if (np.random.rand() < 0.5):
            wtd = "Low"
            test_card = Card(low(), high(), low(), high(), "", i + 1)
            key_card = Card(test_card.get_k(), test_card.get_temp(), 
            test_card.get_precip(), test_card.get_slope(), wtd, i + 1)


        else:
            wtd = "High"
            test_card = Card(high(), low(), high(), low(), "", i + 1)
            key_card = Card(test_card.get_k(), test_card.get_temp(), 
            test_card.get_precip(), test_card.get_slope(), wtd, i + 1)


        test_cards.append(test_card)
        test_cards.append(key_card)

    return train_cards, test_cards


def main():
    cards = get_cards_2(5, True)


# main()