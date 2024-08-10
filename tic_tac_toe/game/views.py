from django.shortcuts import render, redirect
from .game_logic import check_winner, check_draw

def index(request):
    if 'board' not in request.session:
        request.session['board'] = [['' for _ in range(3)] for _ in range(3)]
        request.session['turn'] = 'X'

    board = request.session['board']
    turn = request.session['turn']
    winner = check_winner(board)
    draw = check_draw(board)

    if request.method == 'POST':
        if 'reset' in request.POST:
            request.session['board'] = [['' for _ in range(3)] for _ in range(3)]
            request.session['turn'] = 'X'
        else:
            try:
                row = int(request.POST.get('row', -1))
                col = int(request.POST.get('col', -1))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '' and winner is None and not draw:
                    board[row][col] = turn
                    request.session['turn'] = 'O' if turn == 'X' else 'X'
                    winner = check_winner(board)
                    draw = check_draw(board)
            except (ValueError, TypeError):
                pass  # Ignore invalid data

            request.session['board'] = board
            request.session.modified = True

    context = {
        'board': board,
        'turn': turn,
        'winner': winner,
        'draw': draw,
    }
    return render(request, 'game/index.html', context)
