import React, { useEffect, useState } from 'react';
import Heading from '../MainNews/Heading/Heading';
import Small from './SmallArticleItem';
import SmallArticleItem from './SmallArticleItem';
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
    }
  ];



const SmallArticleList = ({ isForYou }) => {
    const [articles, setArticles] = useState([]);
    const title = isForYou ? "Tin dành riêng cho bạn" : "Tin thế giới";
    const color = isForYou ? "purple" : "emerald";
    const [userEmail, setUserEmail] = useState(null);


    useEffect( () => {
        const fetchArticles = async () => {
            try {
                const response = await axios.get('http://localhost:5000/articles/latest/category/thế giới',);
                setArticles(response.data.articles);
                console.log(response.data.articles);
            } catch (err) {
                
            } finally {
                
            }
        }

        const fetchRecommendations = async (email) => {
            try {
                const response = await axios.post('http://localhost:5000/get_recommendation', {
                    email: email
                
                });
                setArticles(response.data.articles);
                console.log(response.data.articles);
            } catch (err) {
                
            } finally {
                
            }
        }

        const email = localStorage.getItem('email');

        if (!email || !isForYou) fetchArticles();
        else fetchRecommendations(email);
    }, []);


    return (
        <>
            <Heading title={title} color={color} />
            {articles.map(article => (
                <SmallArticleItem key={article.id} article={article} />
            ))}
        </>
    );
}

export default SmallArticleList;