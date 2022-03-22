import MeCab
from src.admin.domain.repositories.BotRepository import IBotRepository
from src.models.Bot import BotModel, FITTED_STATE_FITTING, FITTED_STATE_NO_FIT

from src.admin.domain.repositories.FaqListRepository import IFaqListRepository
from src.models.Faq import FaqModel

import pickle
import os

import sys

class BotService:
    def __init__(self, bot_repository: IBotRepository):
        self.bot_repository = bot_repository

    def get_new_obj(self) -> BotModel:
        return BotModel(name='', fitted_model_path='')

    def get_bots_by_faq_list_id(self, faq_list_id: int) -> list:
        return self.bot_repository.get_list_by_faq_list_id(faq_list_id)

    def get_bots(self) -> list:
        return self.bot_repository.get_list()

    def find_by_id(self, id: int) -> BotModel:
        return self.bot_repository.find_by_id(id)

    def save(self, bot: BotModel, old_bot=None):
        # 既存のFAQリストから変更があった場合、学習状態を未学習に変更
        if bot.id and old_bot:
            if bot.faq_list_id != old_bot.faq_list_id:
                bot.fitted_state = FITTED_STATE_NO_FIT

        return self.bot_repository.save(bot)

    def fit(self, bot_id: int):