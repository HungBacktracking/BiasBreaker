import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import Header from './components/Header/Header';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import About from './pages/About';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
