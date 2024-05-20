import React from 'react';
import { useState, useEffect } from 'react';
import classes from './ForYouArticleList.module.css';
import ForYouArticleItem from './ForYouArticleItem';


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
    return (
        <div className={classes.main_for_you}>
            {sampleData.map(article => (
                <ForYouArticleItem key={article.id} article={article} />
            ))}
            <div className={classes.separate_mid}></div>
        </div>
    );
}

export default ForYouArticleList;