from sqlalchemy.orm import sessionmaker
from database import Contestant, create_engine ,Category, Grade, Fee, Result, Voter
from sqlalchemy import engine


Session = sessionmaker(bind=engine)
session = Session()

def get_contestants():
    contestants = session.query(Contestant).all()
    contestants_list = []
    
    for contestant in contestants:
        contestant_dict = {
            'id': contestant.id,
            'First_Name': contestant.First_Name,
            'Last_Name': contestant.Last_Name,
            'Gender': contestant.Gender,
            'Category_id': contestant.Category_id,
            'Form': contestant.Form,
            'Stream': contestant.Stream,
            'Grade_id': contestant.Grade_id,
            'Fees_id': contestant.Fees_id
        }
        contestants_list.append(contestant_dict)
    
    return contestants_list

def get_categories():
    categories = session.query(Category).all()
    categories_list = []
    
    for category in categories:
        category_dict = {
            'id': category.id,
            'School_level': category.School_level,
            'Form_level': category.Form_level,
            'Class_level': category.Class_level
        }
        categories_list.append(category_dict)
    
    return categories_list

def get_winners():
    winners = session.query(Contestant).join(Result).filter(Result.Percentage_votes == 100).all()
    winners_list = []
    
    for winner in winners:
        winner_dict = {
            'id': winner.id,
            'First_Name': winner.First_Name,
            'Last_Name': winner.Last_Name,
            'Gender': winner.Gender,
            'Category_id': winner.Category_id,
            'Form': winner.Form,
            'Stream': winner.Stream,
            'Grade_id': winner.Grade_id,
            'Fees_id': winner.Fees_id
        }
        winners_list.append(winner_dict)
    
    return winners_list
