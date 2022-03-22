def get_list_by_faq_list_id(self, faq_list_id: int) -> list:
        pass

    @abstractclassmethod
    def get_list(self) -> list:
        pass

    @abstractclassmethod
    def find_by_id(self, id: int) -> BotModel:
        pass