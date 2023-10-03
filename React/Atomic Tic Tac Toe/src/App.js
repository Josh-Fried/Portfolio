import React, { useState } from 'react';
import './App.css';

function App() {
  const [board, setBoard] = useState(Array(9).fill(null).map(() => Array(9).fill(null)));
  const [bigboard, setBigBoard] = useState(Array(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const [newBoard, setNewBoard] = useState(true);
  const winner = calculateWinner(bigboard);
  const [currentBoard, setcurrentBoard] = useState(10);
  const [boardchose, setBoardChose] = useState(false);
  const [isOverlayVisible, setOverlayVisible] = useState(false);
  let status = "";

  const handleClick = (index, i) => {
    if(isOverlayVisible && index != currentBoard) return; //click in wrong square
    if (winner || board[index][i] != null) {
      getStatus()
      return; //if there is a winner or square is already chosen
    }
    if(newBoard){  
      chooseBoard(index);
      return;
    }
    setcurrentBoard(i);
    board[index][i] = xIsNext ? 'X' : 'O';
    setXIsNext(!xIsNext);

    bigboard[index] = calculateWinner(board[index]);
    if(bigboard[index] != null){ //changing the middle small board to the winner to display winner in big board
      console.log(board[index][4]);
      board[index][4] = bigboard[index];
      console.log(board[index][4]);
    }
    if(bigboard[i] != null){
      setOverlayVisible(false);
      setNewBoard(true);
    }
  };

  const renderBigSquare = (i) => (
    <div className='board'>
      {Array(3)
        .fill(null)
        .map((_, row) => (
          <div key={row} className="board-row">
            {Array(3)
              .fill(null)
              .map((_, col) => renderSquare(i, row * 3 + col))}
          </div>
        ))}
      </div>
  );

  const renderSquare = (index, i) => (
    <button className={`square ${isOverlayVisible ? 'overlay' : ''} ${currentBoard === index ? 'active' : ''} 
    ${board[index][i] == 'X' ? 'X' : ''} ${board[index][i] == 'O' ? 'O' : ''}
    ${bigboard[index] == 'X' ? 'WinX' : ''} ${bigboard[index] == 'O' ? 'WinO' : ''}
    ${bigboard[index] != null && i == 4 ? 'middle' : ''} ${winner ? 'gameOver' : ''}`} 
    onClick={() => handleClick(index, i)}>
      {board[index][i]}
    </button>
  );

  const handleReset = () => {
    setBoard(Array(9).fill(null).map(() => Array(9).fill(null)));
    setBigBoard(Array(9).fill(null));
    setXIsNext(true);
    setNewBoard(true);
    setOverlayVisible(false);
    setcurrentBoard(10);
  };

  const renderBigBoard = () => (
    <div className="game">
      <div className="game-bigboard">
        <div className="status">{getStatus()}</div>
        <div> 
          {Array(3) 
            .fill(null)
            .map((_, row) => (
              <div key={row} className="board-row">
                {Array(3)
                  .fill(null)
                  .map((_, col) => renderBigSquare(row * 3 + col))}
              </div>
            ))}
            <button className="replay-button" onClick={handleReset}>
              Reset Board
            </button>
        </div>
      </div>
    </div>
  );

  const chooseBoard = (index) => {
    setcurrentBoard(index);
    setOverlayVisible(true);
    setBoardChose(true);
    setNewBoard(false);
  };

  const getStatus = () => {
    if(winner){
      status = `Winner: ${winner}`;
      return status;
    } else {
      status = `Next player: ${xIsNext ? 'X' : 'O'}`;
    }
    if(newBoard){
      status = `Choose a board: ${xIsNext ? 'X' : 'O'}`;
    }
    return status;
  };

  return (
    <div>
      {renderBigBoard()}
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }

  return null;
}

export default App;


// Order
// 1. Render Board with "Choose a Square for X"
// 2. X chooses a position
// 3. Board changes based on X
// 4. O chooses position
// 5. Continue until someone wins a small board
// 6. Make small board unplayable and have big X or O
// 7. Continue
// 8. If someone's position leads them to a finished small board then the player can chose a new board and play
// 9. End when someone wins. 