"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import FlaskWebProject1.controllers.maincontroller
import FlaskWebProject1.controllers.apicontroller
from FlaskWebProject1.models.BacktestingResult import BacktestingTrade