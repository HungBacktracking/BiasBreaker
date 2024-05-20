import React from 'react';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import classes from './HomePageCategoryList.module.css';

const CategoryItem = ({ article }) => {
    return (
        <>
            <hr className={classes.separate}/>
            <div className={classes.content}>
                <Link className={classes.article_link} to={`/article/${article.id}`}></Link>
                <div className={classes.article_text}>
                    <div className={classes.article_logo_wrapper}>
                        <div className={classes.article_logo}>
                            <img className={classes.article_logo_img} src="https://encrypted-tbn2.gstatic.com/faviconV2?url=https://tuoitre.vn&client=NEWS_360&size=96&type=FAVICON&fallback_opts=TYPE,SIZE,URL" alt="Logo trang báo" />
                            <div className={classes.article_logo_name}>Báo tuổi trẻ</div>
                        </div>
                    </div>
                    <div className={classes.article_title}>{article.title}</div>
                </div>
                <img className={classes.article_img} src={article.imagePath} alt="Ảnh bài báo" loading="lazy"/>
            </div>
            <div className={classes.time}>
                <div className={classes.article_time}>{article.time}</div>
            </div>
        </>
    );
}

export default CategoryItem;