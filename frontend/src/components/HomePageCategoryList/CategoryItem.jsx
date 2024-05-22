import React from 'react';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import classes from './HomePageCategoryList.module.css';

const CategoryItem = ({ article }) => {
    return (
        <>
            <hr className={classes.separate}/>
            <div className={classes.content}>
                <Link className={classes.article_link} to={`/article/${article._id}`}></Link>
                <div className={classes.article_text}>
                    <div className={classes.article_logo_wrapper}>
                        <div className={classes.article_logo}>
                            <img className={classes.article_logo_img} src={article.publisher_logo} alt="Logo trang báo" />
                            {/* (article.publisher == "Tuổi trẻ" ? <div className={classes.article_logo_name}>{article.publisher}</div> : <></>) */}
                        </div>
                    </div>
                    <div className={classes.article_title}>{article.title}</div>
                </div>
                <img className={classes.article_img} src={article.image.url_link} alt="Ảnh bài báo" loading="lazy"/>
            </div>
            <div className={classes.time}>
                <div className={classes.article_time}>{article.datetime}</div>
            </div>
        </>
    );
}

export default CategoryItem;