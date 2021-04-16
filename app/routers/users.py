from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def root():
    return [
        {'id': 0, 'name': 'Jees0'},
        {'id': 1, 'name': 'Jees1'},
    ]
