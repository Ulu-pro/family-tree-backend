from fastapi import APIRouter, HTTPException

from database import db
from models import Tree, Pair, Person

router = APIRouter(tags=['delete'])


@router.delete('/trees/{tree_id}')
def delete_trees(tree_id: int):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    db.delete(tree)
    db.commit()
    return tree
