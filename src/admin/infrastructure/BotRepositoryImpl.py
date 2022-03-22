            BotModel.faq_list_id == faq_list_id).order_by(
            BotModel.id).all()

    def get_list(self) -> list:
        return db.session.query(BotModel).order_by(
            BotModel.id).all()

    def find_by_id(self, id: int) -> BotModel:
        return db.session.query(BotModel).get(id)