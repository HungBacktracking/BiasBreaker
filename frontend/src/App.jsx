import Header from './components/Header/Header';
import MainNews from './components/MainNews/MainNews';

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
