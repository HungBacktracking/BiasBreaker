import React from 'react';
import { useParams } from 'react-router-dom';
import KeywordNews from '../components/KeywordNews/KeywordNews';


function KeywordPage() {
    const { keyword } = useParams();
    
    return (
        <div className="flex flex-col">
        <div style={{ height: '125px' }}></div>
            <KeywordNews keyword={keyword} />
        </div>
    );
}

export default KeywordPage;
