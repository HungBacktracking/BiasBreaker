import React from 'react';
import { Link } from 'react-router-dom';
import classes from './TopArticleList.module.css'

const MainArticle = ({ article }) => {
    return (
        <>
            <Link className={classes.main_article_link} to={`/article/${article.id}`}></Link>
            <img className={classes.main_article_img} src={article.imagePath} alt="Ảnh nổi bật của bài báo" loading='lazy'/>
            <div className={classes.article_publisher}>
                <img class={classes.article_publisher_img} alt="Ảnh trang báo" src="https://lh3.googleusercontent.com/1lUP5eLpU5Mo0hLUEhgegmjBU4IO1p-xmAB-IqtrjsGZx1Hyd6GfItHHwIBwCbdz0Ir-DEatWg=s0-h24-rw" loading="lazy"></img>
            </div>
            
        </>
    );
}

export default MainArticle;