from fastapi import APIRouter, HTTPException

from database import db
from models import Tree, Pair, Person

router = APIRouter(prefix='/read')


@router.get('/trees')
def trees_list():
    trees = []
    tree: Tree
    for tree in db.query(Tree).all():
        trees.append({
            'id': tree.id,
            'name': tree.name,
            'persons_count': tree.get_entries(db, Person).count()
        })
    return trees


@router.get('/trees/{tree_id}/pairs')
def pairs_list(tree_id: int):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    pairs = []
    pair: Pair
    for pair in tree.get_entries(db, Pair).all():
        pairs.append({
            'id': pair.id,
            'husband_id': pair.husband_id,
            'wife_id': pair.wife_id
        })
    return pairs


@router.get('/trees/{tree_id}/pairs/{pair_id}')
def pair_info(tree_id: int, pair_id: int):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    pair: Pair = db.query(Pair).filter_by(id=pair_id).first()
    if not pair:
        raise HTTPException(404, 'Pair not found')

    if tree.id != pair.tree_id:
        raise HTTPException(400, 'Pair does not belong to tree')

    return {
        'husband_id': pair.husband_id,
        'wife_id': pair.wife_id,
        'wedding_date': pair.wedding_date
    }


@router.get('/trees/{tree_id}/persons')
def persons_list(tree_id: int):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    persons = []
    person: Person
    for person in tree.get_entries(db, Person).all():
        persons.append({
            'id': person.id,
            'pair_id': person.pair_id
        })
    return persons


@router.get('/trees/{tree_id}/persons/{person_id}')
def persons_list(tree_id: int, person_id: int):
    tree: Tree = db.query(Tree).filter_by(id=tree_id).first()
    if not tree:
        raise HTTPException(404, 'Tree not found')

    person: Person = db.query(Person).filter_by(id=person_id).first()
    if not person:
        raise HTTPException(404, 'Person not found')

    if tree.id != person.tree_id:
        raise HTTPException(400, 'Person does not belong to tree')

    return {
        'name': person.name,
        'bio': person.bio,
        'gender': person.gender,
        'alive': person.alive,
        'birth_date': person.birth_date,
        'death_date': person.death_date
    }
