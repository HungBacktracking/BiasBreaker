import React from 'react';
import { useState, useEffect } from 'react';
import classes from './CategoryNews.module.css';
import Title from '../MainNews/Title/Title';
import CategoryNewsItem from './CategoryNewsItem';
import axios from 'axios';


const CategoryNews = ({ category, description }) => {
    const [articleList, setArticleList] = useState([]);
    const [categoryText, setCategoryText] = useState('');

    useEffect(() => {
        if (category.length > 0) {
        setCategoryText(category.charAt(0).toUpperCase() + category.slice(1));
        }
    }, [category]);

    useEffect(() => {
		const fetchArticles = async () => {
			try {
				const response = await axios.get(`http://localhost:5000/articles/latest/related/category/${category}`,);
				setArticleList(response.data.articles);
				console.log(response.data.articles);
			} catch (err) {
				console.log(err);
			} finally {
				
			}
		}

		fetchArticles();
    }, [category]);

    return (
      <div className={classes.full_height}>
        <main className={classes.main_container}>
          <div className={classes.news}>
            <Title	name={categoryText} description={description}/>
              <div className={classes.news_list}>
                  {articleList.map(article => (
                      <CategoryNewsItem key={article._id} article={article} />
                  ))}
              </div>
          </div>
        </main>
      </div>
    );
}

export default CategoryNews;