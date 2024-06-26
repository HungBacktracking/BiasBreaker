import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import Header from './components/Header/Header';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import CategoryPage from './pages/CategoryPage';
import ForYouPage from './pages/ForYou';
import TrendingPage from './pages/TrendingPage';
import KeyWordPage from './pages/KeywordPage';
import NewsDetail from './pages/NewsDetail';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/for-you" element={<ForYouPage />} />
        <Route path="/trending" element={<TrendingPage />} />
        <Route path="/keyword/:keyword" element={<KeyWordPage />} />
        <Route path='/category/:category' element={<CategoryPage />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/article/:id" element={<NewsDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
