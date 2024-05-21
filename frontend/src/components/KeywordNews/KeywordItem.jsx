import React from 'react';
import { Link } from 'react-router-dom';
import classes from './KeywordNews.module.css';


const keywordItem = ({ article }) => {
    return (
        <div className={classes.article}>
            <div className={classes.content}>
                <Link className={classes.article_link} to={`/article/${article.id}`}></Link>
                <div className={classes.article_text}>
                    <div className={classes.article_logo_wrapper}>
                        <div className={classes.article_logo}>
                            <img className={classes.article_logo_img} src="https://encrypted-tbn2.gstatic.com/faviconV2?url=https://tuoitre.vn&client=NEWS_360&size=96&type=FAVICON&fallback_opts=TYPE,SIZE,URL" alt="Logo trang báo" />
                            <div className={classes.article_logo_name}>Báo tuổi trẻ</div>
                        </div>
                    </div>
                    <h4 className={classes.article_title}>{article.title}</h4>
                    <div className={classes.time}>
                        <div className={classes.article_time}>{article.time}</div>
                    </div>
                </div>
                <img className={classes.article_img} src={article.imagePath} alt="Ảnh bài báo" loading="lazy"/>
            </div>
        </div>
    );
}

export default keywordItem;