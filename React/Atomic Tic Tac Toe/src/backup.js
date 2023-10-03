import React, { useState } from 'react';
import './App.css';

function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [bigboard, setBigBoard] = useState(Array(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const [start, setStart] = useState(true);
  const winner = calculateWinner(bigboard);

  const handleClick = (i) => {
    const squares = [...board];
    if (winner || squares[i]) return;

    squares[i] = xIsNext ? 'X' : 'O';
    //board[0][i] = squares[i];
    setBoard(squares);
    setXIsNext(!xIsNext);
  };

  const handleBigClick = (i) => {
    // needs to dim the other squares and only let the player play on the right square
    
  };

  const renderBigSquare = (i) => (
    <div className="board">
      {Array(3)
        .fill(null)
        .map((_, row) => (
          <div key={row} className="board-row">
            {Array(3)
              .fill(null)
              .map((_, col) => renderSquare(row * 3 + col))}
          </div>
        ))}
      </div>
  );

  const renderSquare = (i) => (
    <button className="square" onClick={() => handleClick(i)}>
      {board[i]}
    </button>
  );

  const handleReset = () => {
    setBoard(Array(9).fill(null));
    setXIsNext(true);
  };

  const renderBigBoard = () => {
    <div className="game">
    <div className="game-bigboard">
      <div className="status">{status}</div>
      <div className="board">
        {Array(3)
          .fill(null)
          .map((_, row) => (
            <div key={row} className="board-row">
              {Array(3)
                .fill(null)
                .map((_, col) => renderBigSquare(row * 3 + col))}
            </div>
          ))}
      </div>
    </div>
  </div>
  };

  const startGame = () =>{
    if(start){
      <div>
        
      </div>
      setStart(false);
    }
  }

  const status = winner
    ? `Winner: ${winner}`
    : `Next player: ${xIsNext ? 'X' : 'O'}`;

  return (
    <div className="game">
      {startGame}
    <div className="game-bigboard">
      <div className="status">{status}</div>
      <div> 
        {/* instead just manually do board[0][0] ... board[8][8] */}
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