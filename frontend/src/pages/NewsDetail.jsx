import React from 'react';
import { useParams } from 'react-router-dom';
import ArticleDetail from '../components/ArticleDetail/ArticleDetail';


function NewsDetail() {
    const { id } = useParams();
    
    return (
        <div className="flex flex-col">
        <div style={{ height: '125px' }}></div>
            <ArticleDetail article_id={id} />
        </div>
    );
}

export default NewsDetail;