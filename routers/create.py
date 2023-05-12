from fastapi import APIRouter, Form, HTTPException

from database import db
from models import Tree, Pair, Person

router = APIRouter(tags=['create'])


@router.post('/trees')
def create_trees(name: str = Form()):
    new_tree = Tree(name=name)
    db.add(new_tree)
    db.commit()
    db.refresh(new_tree)
    return new_tree
