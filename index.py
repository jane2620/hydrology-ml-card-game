
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

    train_cards, test_cards, key_cards = get_cards(num_train_cards, 
    num_test_cards)

    card_html = 'fakecards.html'

    html = render_template(card_html, train_cards=train_cards, 
                            test_cards=test_cards, 
                            key_cards = key_cards)
    response = make_response(html)
    return response

@app.route('/answers', methods=['GET', 'POST'])
def answer_page():
    var_type = request.args.get('variable_type')

    if (var_type == "wtd_vars"): card_html = 'cards.html'
    else: card_html = 'fakecards.html'

    html = render_template(card_html, answers=key_cards)
    response = make_response(html)
    return response


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
def get_cards(num_train_cards, num_test_cards):
    train_cards = []
    test_cards = []
    key_cards = []

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
        key_cards.append(key_card)

    return train_cards, test_cards, key_cards


def main():
    cards = get_cards(5, True)


# main()