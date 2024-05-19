import React, { useEffect, useState } from 'react';
import Heading from '../MainNews/Heading/Heading';
import Small from './SmallArticleItem';
import SmallArticleItem from './SmallArticleItem';

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

    useEffect(() => {
        const fetchArticles = async () => {
            try {
                // const response = await fetch(isForYou ? '/api/personalized-articles' : '/api/general-articles');
                // const data = await response.json();
                const data = sampleData;
                setArticles(data);
            } catch (error) {
                console.error('Error fetching articles:', error);
            }
        };

        fetchArticles();
    }, [isForYou]);


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