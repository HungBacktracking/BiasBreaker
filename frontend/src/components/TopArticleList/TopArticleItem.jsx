import React from 'react';
import classes from './TopArticleList.module.css';
import MainArticle from './MainArticle';

const TopArticleItem = ({ article }) => {
    return (
        <div className={classes.top_article_item}>
            <div className={classes.main_article}>
                <MainArticle article={article} />
            </div>
            <div className={classes.related_article_list}></div>
        </div>
    );
}

export default TopArticleItem;