import React from 'react';
import { useState, useEffect } from 'react';
import classes from './ForYouNews.module.css';
import Title from '../MainNews/Title/Title';
import CategoryNewsItem from '../CategoryNews/CategoryNewsItem';


const sampleData = [
    { 
      id: 1, 
      title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7 ", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Politics", 
      content: "Content of article 1",
      relatedArticles: [
        { id: 4, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 1 for article 1" },
        { id: 5, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 2 for article 1" },
        { id: 6, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 3 for article 1" }
      ]
    },
    { 
      id: 2, 
      title: "Iphone sắp thoát lối mòn Mobile", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Politics", 
      content: "Content of article 2",
      relatedArticles: [
        { id: 7, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 1 for article 2" },
        { id: 8, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 2 for article 2" },
        { id: 9, title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 3 for article 2" }
      ]
    },
    { 
      id: 3, 
      title: "Iphone sắp thoát lối mòn Mobile", 
      imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp", 
      time: "Hôm nay", 
      category: "Sports", 
      content: "Content of article 3",
      relatedArticles: [
        { id: 10, title: "Sự rối ren tại công ty đứng sau ChatGPT", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 1 for article 3" },
        { id: 11, title: "Sự rối ren tại công ty đứng sau ChatGPT", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 2 for article 3" },
        { id: 12, title: "Sự rối ren tại công ty đứng sau ChatGPT", imagePath: "https://via.placeholder.com/150", time: "Hôm qua", content: "Content of related article 3 for article 3" }
      ]
    }
  ];


const ForYouNews = () => {
    const [articleList, setArticleList] = useState([]);

    useEffect(() => {
        const filteredArticles = sampleData;
        setArticleList(filteredArticles);
    }, [articleList]);

    
    return (
        <div className={classes.full_height}>
			<main className={classes.main_container}>
				<div className={classes.news}>
						<Title	name="Dành cho bạn" description="Đề xuất dựa trên sở thích của riêng bạn"/>
                        <div className={classes.news_list}>
                            {articleList.map(article => (
                                <CategoryNewsItem key={article.id} article={article} />
                            ))}
                        </div>
				</div>
			</main>
		</div>
    );
}

export default ForYouNews;