from fastapi import APIRouter, Form, HTTPException

from database import db
from models import Tree, Pair, Person

router = APIRouter(tags=['update'])


@router.put('/trees/{tree_id}')
def update_trees(tree_id: int, name: str = Form()):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    tree.name = name
    db.commit()
    db.refresh(tree)
    return tree
