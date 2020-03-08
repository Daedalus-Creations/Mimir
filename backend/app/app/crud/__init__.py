from .crud_user import user
from .crud_quote import quote
from .crud_tag import tag

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.quote import Quote
# from app.schemas.quote import QuoteCreate, QuoteUpdate

# quote = CRUDBase[Quote, QuoteCreate, QuoteUpdate](Quote)
