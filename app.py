from flask import Flask, request
from services.contracts_service import Contracts, Contract

app = Flask(__name__)


@app.route("/contracts", methods=['POST'])
def contract():
    contracts = request.json['contracts']
    open_contracts = [
        Contract(contract['id'], contract['debt']) for contract in contracts
    ]
    contracts = Contracts()
    return contracts.get_top_N_open_contracts(
        open_contracts,
        request.json['renegotiated'],
        request.json['top_n']
    )
