import React from 'react';
import { useState, useEffect } from 'react';
import classes from './ForYouArticleList.module.css';
import ForYouArticleItem from './ForYouArticleItem';
import axios from 'axios';

const sampleData = [
    { 
      id: 1, 
      title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7 ", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Politics", 
      content: "Content of article 1",
    },
    { 
      id: 2, 
      title: "Iphone sắp thoát lối mòn Mobile", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Politics", 
      content: "Content of article 2",
    },
    { 
      id: 3, 
      title: "Iphone sắp thoát lối mòn Mobile", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Sports", 
      content: "Content of article 3",
    },
    { 
        id: 1, 
        title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7 ", 
        imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
        time: "Hôm nay", 
        category: "Politics", 
        content: "Content of article 1",
      },
      { 
        id: 2, 
        title: "Iphone sắp thoát lối mòn Mobile", 
        imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
        time: "Hôm nay", 
        category: "Politics", 
        content: "Content of article 2",
      },
      { 
        id: 3, 
        title: "Iphone sắp thoát lối mòn Mobile", 
        imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
        time: "Hôm nay", 
        category: "Sports", 
        content: "Content of article 3",
      }
  ];


const ForYouArticleList = () => {
	const [isLoading, setIsLoading] = useState(true);
	const [articleList, setArticleList] = useState([]);
	
	useEffect(() => {
		setIsLoading(true);
		const fetchRecommendations = async (email) => {
            try {
                const response = await axios.post('http://localhost:5000/get_recommendation', {
                    email: email
                
                });
                setArticleList(response.data.articles.slice(3, 9));
                console.log("Recommendation");
                console.log(response.data.articles);
            } catch (err) {
                console.log(err);
            } finally {
                setIsLoading(false);
            }
        }

		const email = localStorage.getItem('email');
		if (email) fetchRecommendations(email);
	}, []);

    return (
        <div className={classes.main_for_you}>
            {articleList.map(article => (
                <ForYouArticleItem key={article._id} article={article} />
            ))}
            <div className={classes.separate_mid}></div>
        </div>
    );
}

export default ForYouArticleList;