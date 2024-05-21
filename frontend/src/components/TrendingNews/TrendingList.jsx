import React from 'react';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; 
import classes from './TrendingNews.module.css';

const TrendingList = ({ trendingList }) => {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        setArticles(trendingList.articles);
    }, [trendingList]);

    return (
        <>
            <div className={classes.trending_container}>
                <div className={classes.trending_time}>{trendingList.time}</div>
                <div className={classes.trending_list}>
                    {articles.map((article, index) => (
                        <Link to={`/keyword/${article.keyword}`} className={classes.trending_item} key={index}>
                            <div className={classes.trending_index}>{index + 1}</div>
                            <div className={classes.trending_content}>
                                <div className={classes.trending_keyword}>{article.keyword}</div>
                                <div className={classes.article_detail}>
                                    <div className={classes.article_title}>
                                        {article.title}
                                    </div>
                                    <div className={classes.source_time}>
                                        <div>{article.publisher}</div>
                                        <div>  •  </div>
                                        <div>{article.time}</div>
                                    </div>
                                </div>
                            </div>
                            <div className={classes.trending_frequency}>
                                <div className={classes.frequency_top}>{article.frequency}</div>
                                <div className={classes.frequency_bottom}>lượt quan tâm</div>
                            </div>
                            <img className={classes.trending_img} src={article.imagePath} alt="Ảnh bài báo" />
                        </Link>
                    ))}
                </div>
            </div>
        </>
    );
}

export default TrendingList;