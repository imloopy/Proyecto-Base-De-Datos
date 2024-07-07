import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ChakraProvider } from '@chakra-ui/react';
import Login from './components/Login';
import MainMenu from './components/MainMenu';

function App() {
  const [userData, setUserData] = useState(null);

  const handleLogin = (userData) => {
    setUserData(userData);
  };

  return (
    <ChakraProvider>
      <Router>
        <Routes>
          <Route path="/main-menu" element={<MainMenu userName={userData?.name} sedeComuna={userData?.comuna} />} />
          <Route path="/" element={<Login onLogin={handleLogin} />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
