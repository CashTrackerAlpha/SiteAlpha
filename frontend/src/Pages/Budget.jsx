import React, { useState, useEffect, useContext } from 'react';
import List from '../Components/List';
import { UserContext } from '../UserContext';
const App = () => {
  const { userData } = useContext(UserContext);
  const [budgets, setBudgets] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log(localStorage.getItem('authToken'))
        const response = await fetch(`http://127.0.0.1:8000/budget/findbyid/${userData.id}/`, {
          method: "GET",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('authToken')}`
          }
        });
        if (response.ok) {
          const data = await response.json();
          setBudgets(data);
        } else {
          console.error('Failed to fetch budgets');
        }
      } catch (error) {
        console.error('Error fetching budgets:', error);
      }
    };

    fetchData();
  }, [userData.username]);

  return (
    <div>
      {budgets ? (
        <div>
          <h1>Budget for {userData.username}</h1>
          <p>Budget Name: {budgets.budgetname}</p>
        </div>
      ) : (
        <p>Loading budget...</p>
      )}
    </div>
  );
};

export default App;
