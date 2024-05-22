import React from 'react';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import classes from './ArticleDetail.module.css';
import axios from 'axios';

const ArticleDetail = ({ article_id }) => {
    const [article, setArticle] = useState(null);

    // useEffect(() => {
	// 	// setIsLoading(true);
	// 	const fetchArticles = async () => {
	// 		try {
	// 			const response = await axios.get(`http://localhost:5000/articles/${article_id}`,);
	// 			setArticle(response.data.articles);
    //             console.log(response.data);
	// 		} catch (err) {
	// 			console.log(err);
	// 		} finally {
	// 			// setIsLoading(false);
	// 		}
	// 	}

	// 	fetchArticles();
    // }, [article_id]);

    return (
        <div className={classes.full_height}>
            <div className={classes.main_container}>
                {/* {article[0].title} */}
            </div>
        </div>
    );
}

export default ArticleDetail;


