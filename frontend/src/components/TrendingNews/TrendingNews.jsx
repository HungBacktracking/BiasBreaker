import React from 'react';
import classes from './TrendingNews.module.css';
import TrendingList from './TrendingList';
import Loading from '../Loading/Loading';
import { useState, useEffect } from 'react';
import axios from 'axios';

const sampleData = [
    {
        time: "Thứ Ba, 21 tháng 5, 2024",
        articles: [
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7 Chủ tịch Quốc hội tại Kỳ họp",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 2,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
        ],
    },

    {
        time: "Thứ Hai, 20 tháng 5, 2024",
        articles: [
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 2,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
        ],
    },
    {
        time: "Chủ Nhật, 19 tháng 5, 2024",
        articles: [
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 2,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
            {
                id: 1,
                keyword: "Tổng thống Iran",
                publisher: "Báo Thanh Niên",
                frequency: "Trên 20 N",
                title: "Quốc hội tiến hành bầu Chủ tịch nước, Chủ tịch Quốc hội tại Kỳ họp thứ 7",
                imagePath: "https://image.nhandan.vn/w800/Uploaded/2024/athlraguvhlra/2024_05_18/dai-tuong-to-lam-9610-81.jpg.webp",
                time: "Hôm nay",
                category: "Politics",
                content: "Content of article 1",
            },
        ],
    },
];

const TrendingNews = () => {
    const [isLoading, setIsLoading] = useState(true);
    const [articles, setArticles] = useState([]);

    const fetchArticles = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get('http://localhost:5000/articles/keywords-paper/number-of-day/3/limit/10',);
            setArticles(response.data.keywords);
        } catch (err) {
            
        } finally {
            setIsLoading(false);
        }
    };

    useEffect( () => {
		fetchArticles();
    }, []);

    return (
        <div className={classes.full_height}>
            <Loading isLoading={isLoading} />
            <main className={classes.main_container}>
                <div className={classes.trending_main}>
                    { articles.map((data, index) => (
                        <TrendingList key={index} trendingList={data} />
                    ))}
                </div>
            </main>
        </div>
    );
}

export default TrendingNews;