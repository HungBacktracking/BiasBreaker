import React from 'react';
import { useParams } from 'react-router-dom';
import ForYouNews from '../components/ForYouNews/ForYouNews';


function ForYouPage() {
    return (
        <div className="flex flex-col">
        <div style={{ height: '125px' }}></div>
            <ForYouNews />
        </div>
    );
}

export default ForYouPage;
