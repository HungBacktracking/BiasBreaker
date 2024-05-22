import React from 'react';
import { Link } from 'react-router-dom';
import classes from './CategoryNews.module.css';


const CategoryNewsItem = ({ article }) => {
    const { related, ...mainArticle } = article;

    return (
        <div className={classes.top_article_item}>
            <div className={classes.main_article}>
                <Link className={classes.article_link} to={`/article/${mainArticle._id}`}></Link>
                <img className={classes.main_article_img} src={mainArticle.image.url_link} alt="Ảnh nổi bật của bài báo" loading='lazy'/>
                <div className={classes.article_publisher}>
                    <img class={classes.article_publisher_img} alt="Ảnh trang báo" src={mainArticle.publisher_logo} loading="lazy"></img>
                </div>
                <p className={classes.main_article_title}>{mainArticle.title}</p>
                <p className={classes.article_time}>{mainArticle.datetime}</p>
            </div>

            <div className={classes.related_article_list}>
                {related.map(relatedArticle => (
                    <div className={classes.related_article}>
                        <Link className={classes.article_link} to={`/article/${relatedArticle._id}`}></Link>
                        <div className={classes.article_publisher}>
                            <img class={classes.article_publisher_img} alt="Ảnh trang báo" src={relatedArticle.publisher_logo} loading="lazy"></img>
                        </div>
                        <p className={classes.related_article_title}>{relatedArticle.title}</p>
                        <p className={classes.related_article_time}>{relatedArticle.datetime}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default CategoryNewsItem;