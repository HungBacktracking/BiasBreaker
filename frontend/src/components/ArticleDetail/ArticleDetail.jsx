import React from 'react';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import classes from './ArticleDetail.module.css';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import Loading from '../Loading/Loading';

const ArticleDetail = ({ article_id }) => {
    const [article, setArticle] = useState('');
	const [content, setContent] = useState([]);
	const [predictionText, setPredictionText] = useState("");
	const [summary, setSummary] = useState([]);
	const [loading, setLoading] = useState(`${classes.none} ${classes.spinner_border}`);
	const [isLoading, setIsLoading] = useState(false);

	const [easy, setEasy] = useState(`${classes.option}`);
	const [medium, setMedium] = useState(`${classes.option}`);
	const [hard, setHard] = useState(`${classes.option}`);


	const fetchSummary = async () => {
		setIsLoading(true);
		try {
			const response = await axios.get(`https://biasbreaker.onrender.com/get_summary/${article_id}`,);
			return response.data.summary;
		} catch (err) {
			console.log(err);
		} finally {
			setIsLoading(false);
		}
	}

	const handleEasy = async () => {
		setEasy(`${classes.option} ${classes.option_choosed}`);
		setMedium(`${classes.option}`);
		setHard(`${classes.option}`);

		setSummary([]);
		const ans = await fetchSummary();
		setSummary(ans.easy.trim().split('\n'));
	}

	const handleMedium = async () => {
		setEasy(`${classes.option}`);
		setMedium(`${classes.option} ${classes.option_choosed}`);
		setHard(`${classes.option}`);

		setSummary([]);
		const ans = await fetchSummary();
		setSummary(ans.normal.trim().split('\n'));
	}

	const handleHard = async () => {
		setEasy(`${classes.option}`);
		setMedium(`${classes.option}`);
		setHard(`${classes.option} ${classes.option_choosed}`);

		setSummary([]);
		const ans = await fetchSummary();
		setSummary(ans.detailed.trim().split('\n'));
	}

	const handleFull = () => {
		setEasy(`${classes.option}`);
		setMedium(`${classes.option}`);
		setHard(`${classes.option}`);

		setSummary(article.content.trim().split('\n'));
	}

    useEffect(() => {
		// setIsLoading(true);
		const fetchArticles = async () => {
			try {
				const response = await axios.get(`https://biasbreaker.onrender.com/articles/${article_id}`,);
				setArticle(response.data.articles);
				setSummary(response.data.articles.content.trim().split('\n'));
				setContent(response.data.articles.content.trim().split('\n'));
                console.log(response.data);
			} catch (err) {
				console.log(err);
			} finally {
				// setIsLoading(false);
			}
		}

		fetchArticles();
    }, [article_id]);

	const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }

    const fetchPrediction = async () => {
        try {
            const response = await axios.get(`https://biasbreaker.onrender.com/get_prediction/${article_id}`,);
            setPredictionText(response.data.prediction);
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

    return (
        <div className={classes.full_height}>
			<Loading isLoading={isLoading} />
            <div className={classes.main_container}>
                <div className={classes.insight}>
					<div className={classes.insight_title}>Tác động</div>
					{
						predictionText === "" ? (
							<div className={classes.button_wrapper}>
								<div onClick={handlePrediction} className={classes.buttonLoading}>
									<div className={loading}></div>
									Khám phá
								</div>
							</div>
						) : (<ReactMarkdown className={classes.prediction}>{predictionText}</ReactMarkdown>)
					}
				</div>
				<div className={classes.article}>
					<div className={classes.firstline}>
						<div className={classes.category}>{article.category}</div>
						<div className={classes.time}>{article.datetime}</div>
					</div>
					<div className={classes.title_wrapper}>
						<h1 className={classes.title}>{article.title}</h1>
						<img className={classes.publisher} src={article.publisher_logo} alt="Publisher Logo" />
					</div>
					{article.image && article.image.url_link && (
                        <div className={classes.image}>
                            <img className={classes.image_main} src={article.image.url_link} alt="Image of article" />
                            <div className={classes.image_content}>{article.image.description}</div>
                        </div>
                    )}

					<div className={classes.summary}>
						<div className={classes.choose}>
							<div onClick={handleEasy} className={`${easy}`}>Ngắn gọn</div>
							<div className={classes.separate_option}> </div>
							<div onClick={handleMedium} className={`${medium}`}>Trung bình</div>
							<div className={classes.separate_option}> </div>
							<div onClick={handleHard} className={`${hard}`}>Chi tiết</div>
						</div>
						<div onClick={handleFull} className={classes.original}>Đọc nội dung gốc</div>
					</div>
					{summary.map((paragraph, index) => (
						<ReactMarkdown key={index} className={classes.content}>{paragraph}</ReactMarkdown>
					))}
					
				</div>
            </div>
        </div>
    );
}

export default ArticleDetail;


