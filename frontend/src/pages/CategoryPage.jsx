import React from 'react';
import CategoryNews from '../components/CategoryNews/CategoryNews';

function CategoryPage() {
  return (
    <div className="flex flex-col">
      <div style={{ height: '125px' }}></div>
      <CategoryNews />
    </div>
  );
}

export default CategoryPage;
