import React from 'react';
import TrendingNews from '../components/TrendingNews/TrendingNews';

const TrendingPage = () => {
    return (
        <div className="flex flex-col">
        <div style={{ height: '125px' }}></div>
            <TrendingNews />
        </div>
    );
}

export default TrendingPage;