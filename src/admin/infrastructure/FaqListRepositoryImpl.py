from src.admin.domain.repositories.FaqListRepository import IFaqListRepository
from src.models.FaqList import FaqListModel
from src.database import db
class FaqListRepositoryImpl(IFaqListRepository):
    def find_by_id(self, id: int) -> FaqListModel:
        return FaqListModel.query.get(id)
    def find_by_name(self, name: str) -> FaqListModel:
        pass

    def save(self, faq_list: FaqListModel):
        db.session.add(faq_list)
        return db.session.commit()

    def get_list(self) -> list:
        return FaqListModel.query.order_by(FaqListModel.id).all()
        # return db.session.query(FaqListModel).all()