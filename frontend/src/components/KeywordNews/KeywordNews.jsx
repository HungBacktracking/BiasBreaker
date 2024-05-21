import React from 'react';
import { useState, useEffect } from 'react';
import classes from './KeywordNews.module.css';
import KeywordItem from './KeywordItem';

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

const KeywordNews = ({ keyword }) => {
    const [topArticles, setTopArticles] = useState([]);
    const [allArticles, setAllArticles] = useState([]);
    const [keywordText, setKeywordText] = useState('');

    useEffect(() => {
        if (keyword.length > 0) {
        setKeywordText(keyword.charAt(0).toUpperCase() + keyword.slice(1));
        }
    }, [keyword]);

    useEffect(() => {
        const top = sampleData.slice(0, 4);
        const allArticles = sampleData.slice(4, sampleData.length);
        setTopArticles(top);
        setAllArticles(allArticles);
    }, [keyword]);

    return (
        <div className={classes.full_height}>
            <main className={classes.main_container}>
                <div className={classes.context}>
                    <div className={classes.context_container}>
                        <img className={classes.context_icon} alt="Icon" src="https://lh3.googleusercontent.com/JDFOyo903E9WGstK0YhI2ZFOKR3h4qDxBngX5M8XJVBZFKzOBoxLmk3OVlgNw9SOE-HfkNgb=w40-rw" data-iml="48042090"/>
                        <div className={classes.context_text}>Thông tin toàn cảnh</div>
                    </div>
                </div>
                <h1 className={classes.keyword_description}>Tin tức về {keyword}</h1>
                <div className={classes.keyword_container}>
                    <h2 className={classes.keyword_title}>Tin tức hàng đầu</h2>
                    <div className={classes.keyword_list}>
                        { topArticles.map((data, index) => (
                            <KeywordItem article={data} key={index} />
                        ))}
                    </div>
                    <h2 className={classes.keyword_title}>Tất cả bài viết</h2>
                    <div className={classes.keyword_list}>
                        { allArticles.map((data, index) => (
                            <KeywordItem article={data} key={index} />
                        ))}
                    </div>
                </div>
            </main>
        </div>
    );
}

export default KeywordNews;