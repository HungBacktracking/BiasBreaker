import React from 'react';
import classes from './TopArticleList.module.css';
import { Link } from 'react-router-dom';

const TopArticleItem = ({ article }) => {
    const { relatedArticles, ...mainArticle } = article;

    return (
        <div className={classes.top_article_item}>
            <div className={classes.main_article}>
                <Link className={classes.article_link} to={`/article/${mainArticle.id}`}></Link>
                <img className={classes.main_article_img} src={mainArticle.imagePath} alt="Ảnh nổi bật của bài báo" loading='lazy'/>
                <div className={classes.article_publisher}>
                    <img class={classes.article_publisher_img} alt="Ảnh trang báo" src="https://lh3.googleusercontent.com/1lUP5eLpU5Mo0hLUEhgegmjBU4IO1p-xmAB-IqtrjsGZx1Hyd6GfItHHwIBwCbdz0Ir-DEatWg=s0-h24-rw" loading="lazy"></img>
                </div>
                <p className={classes.main_article_title}>{mainArticle.title}</p>
                <p className={classes.article_time}>{mainArticle.time}</p>
            </div>

            <div className={classes.related_article_list}>
                {relatedArticles.map(relatedArticle => (
                    <div className={classes.related_article}>
                        <Link className={classes.article_link} to={`/article/${relatedArticle.id}`}></Link>
                        <div className={classes.article_publisher}>
                            <img class={classes.article_publisher_img} alt="Ảnh trang báo" src="https://lh3.googleusercontent.com/1lUP5eLpU5Mo0hLUEhgegmjBU4IO1p-xmAB-IqtrjsGZx1Hyd6GfItHHwIBwCbdz0Ir-DEatWg=s0-h24-rw" loading="lazy"></img>
                        </div>
                        <p className={classes.related_article_title}>{relatedArticle.title}</p>
                        <p className={classes.related_article_time}>{relatedArticle.time}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default TopArticleItem;