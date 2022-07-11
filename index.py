
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
    num_cards = request.args.get('num_cards')
    cards = get_cards(num_cards)
    html = render_template('cards.html', cards=cards, num_cards=num_cards)
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


def get_cards(num_cards):
    if (num_cards is None or num_cards is ""): return "Oh no!"
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
            current_card = Card(k, ET, P, topo, wtd)
            
        else:
            # high WTD
            k = get_value(k_high)
            ET = get_value(ET_high)
            P = get_value(P_high)
            topo = get_value(topo_high)
            wtd = "High"
            current_card = Card(k, ET, P, topo, wtd)

        cards.append(current_card)


    return cards


def main():
    pass