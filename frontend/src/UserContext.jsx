import React, { createContext, useState } from 'react';

const UserContext = createContext();

const UserProvider = ({ children }) => {
  const initialUserData = {
    username: null,
    password: null,
    fullname: null,
    email: null,
  };

  const [userData, setUserData] = useState(initialUserData);

  return (
    <UserContext.Provider value={{ userData, setUserData}}>
      {children}
    </UserContext.Provider>
  );
};

export { UserContext, UserProvider };
