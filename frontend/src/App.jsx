import React from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';
import Layout from './Layout/Layout';
import Main from './Pages/Main';
import Test from './Pages/Test';
import Auth from './Login/Auth'
import { UserProvider } from './UserContext';

function App() {
  const location = useLocation();

  const isLoginPage = location.pathname === '/';

  const RoutesWithOptionalLayout = () => (
    <Routes>
      <Route path='/Main' element={<Main />} />
      <Route path='/Test' element={<Test />} />
      <Route path='/' element={<Auth />} />
    </Routes>
  );

  return (
    <UserProvider>
    <>
      {isLoginPage ? (
        <RoutesWithOptionalLayout />
      ) : (
        <Layout>
          <RoutesWithOptionalLayout />
        </Layout>
      )}
    </>
    </UserProvider>
  );
}

export default App;
