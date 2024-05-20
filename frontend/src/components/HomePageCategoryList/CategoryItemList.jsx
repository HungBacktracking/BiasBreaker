import React from 'react';
import { useState, useEffect } from 'react';
import classes from './HomePageCategoryList.module.css';
import CategoryItem from './CategoryItem';
import Heading from '../MainNews/Heading/Heading';

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
  ];


const CategoryItemList = ({ category }) => {
    const [articleList, setArticleList] = useState([]);
    const [categoryText, setCategoryText] = useState('');

    useEffect(() => {
        if (category.length > 0) {
        setCategoryText(category.charAt(0).toUpperCase() + category.slice(1));
        }
    }, [category]);

    useEffect(() => {
        const filteredArticles = sampleData;
        setArticleList(filteredArticles);
    }, [articleList]);

    return (
        <div className={classes.category}>
            <div className={classes.category_item}>
                <Heading title={categoryText} color="grab_green" />
                {articleList.map(article => (
                    <CategoryItem key={article.id} article={article} />
                ))}
            </div>
        </div>
    );
}

export default CategoryItemList;