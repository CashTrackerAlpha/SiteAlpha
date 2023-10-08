import React from 'react';
import List from '../Components/List';

const App = () => {
  const numbers = [1, 2, 3, 4, 5];

  return (
    <div>
      <h1>Numbers List</h1>
      <List numbers={numbers} />
    </div>
  );
};

export default App;
