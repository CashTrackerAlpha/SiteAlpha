import React, { useState } from 'react';
import { Login } from './Login';
import { Register } from './Register'

const Auth = () => {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  // Makes our swap from Login to Register button work!
  return (
    <>
      {currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Register onFormSwitch={toggleForm} />}
    </>
  );
};

export default Auth;