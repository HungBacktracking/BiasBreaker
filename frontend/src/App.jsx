import Header from './components/Header/Header';
import MainNews from './components/MainNews/MainNews';
import Navbar from './components/Navbar/Navbar';

function App() {
  return (
    <div className='flex flex-col'>
      <Header />
      <div style={{ height: '125px' }}></div>
      <MainNews />
    </div>
  );
}

export default App;
