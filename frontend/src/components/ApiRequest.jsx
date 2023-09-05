import React, { useState, useEffect } from 'react';

function ApiComponent() {
  // State to store the data from the API response
  const [data, setData] = useState([]);
  // State to track loading and error states
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Define the URL of the API you want to fetch
    const apiUrl = 'http://127.0.0.1:8000/findall/'; // Replace with your API URL

    // Fetch data from the API
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        // Update the state with the data
        setData(data);
        setIsLoading(false); // Set loading to false
      })
      .catch((error) => {
        setError(error); // Set the error state
        setIsLoading(false); // Set loading to false
      });
  }, []); // Empty dependency array ensures this effect runs once, similar to componentDidMount

  // JSX to render based on the API response
  return (
    <div>
      {isLoading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error.message}</p>
      ) : (
        <div>
          <h2>API Data</h2>
          <ul>
            {data.map((item) => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ApiComponent;
