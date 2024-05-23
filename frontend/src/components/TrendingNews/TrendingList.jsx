import React from 'react';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; 
import classes from './TrendingNews.module.css';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';


const TrendingList = ({ trendingList }) => {
    const [articles, setArticles] = useState([]);
    const [predictionText, setPredictionText] = useState("");
    const [loading, setLoading] = useState(`${classes.none} ${classes.spinner_border}`);

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }

    const fetchPrediction = async () => {
        try {
            const response = await axios.get(`https://biasbreaker.onrender.com/articles/predict-top-keywords-title/date/${formatDate(trendingList.datetime)}`,);
            setPredictionText(response.data.Predictions);
            // console.log(response.data.Predictions);
        } catch (err) {
            console.log(err);
        } finally {

        }
    };

    const handlePrediction = async () => {
        setLoading(`${classes.spinner_border}`);
        await fetchPrediction();
        setLoading(`${classes.none} ${classes.spinner_border}`);
        console.log(predictionText);
    }

    useEffect(() => {
        setArticles(trendingList.keywords);
    }, [trendingList]);


    return (
        <>
            <div className={classes.trending_container}>
                <div className={classes.trending_time}>{trendingList.datetime}</div>
                <div className={classes.trending_list}>
                    <div className={classes.button_wrapper}>
                        {
                            predictionText === "" ? (
                                <div onClick={handlePrediction} className={classes.buttonLoading}>
                                    <div className={loading}></div>
                                    Khám phá
                                </div>
                            ) : (<ReactMarkdown className={classes.prediction}>{predictionText}</ReactMarkdown>)
                        }
                    </div>
                    {articles.map((article, index) => (
                        <Link to={`/keyword/${article.keyword}`} className={classes.trending_item} key={index}>
                            <div className={classes.trending_index}>{index + 1}</div>
                            <div className={classes.trending_content}>
                                <div className={classes.trending_keyword}>{article.keyword}</div>
                                <div className={classes.article_detail}>
                                    <div className={classes.article_title}>
                                        {article.article.title}
                                    </div>
                                    <div className={classes.source_time}>
                                        <div>{article.article.publisher}</div>
                                        {/* <div>  •  </div>
                                        <div>{formatDate(article.article.datetime)}</div> */}
                                    </div>
                                </div>
                            </div>
                            <div className={classes.trending_frequency}>
                                <div className={classes.frequency_top}>{article.frequency} N</div>
                                <div className={classes.frequency_bottom}>lượt quan tâm</div>
                            </div>
                            <img className={classes.trending_img} src={article.article.image.url_link} alt="Ảnh bài báo" />
                        </Link>
                    ))}
                </div>
            </div>
        </>
    );
}

export default TrendingList;