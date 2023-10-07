import React from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';
import Layout from './Layout/Layout';
import Main from './Pages/Main';
import Auth from './Login/Auth';
import Homepage from './Pages/Homepage';
import { UserProvider } from './UserContext';
function App() {
  const location = useLocation();
  const layoutRoutes = ['/Main', '/About','/Edit','/View']; // Routes that should have the Layout
  const shouldHaveLayout = layoutRoutes.includes(location.pathname);

  return (
    <UserProvider>
      {shouldHaveLayout ? (
        <Layout>
          <Routes>
            <Route path='/Main' element={<Main />} />
          </Routes>
        </Layout>
      ) : (
        <Routes>
          <Route path='/' element={<Homepage />} />
          <Route path='/Login' element={<Auth />} />
        </Routes>
      )}
    </UserProvider>
  );
}


export default App;
