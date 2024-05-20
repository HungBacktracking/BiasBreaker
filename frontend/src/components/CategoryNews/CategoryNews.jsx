import React from 'react';
import classes from './CategoryNews.module.css';
import Title from '../MainNews/Title/Title';


const CategoryNews = ({ category }) => {
    

    return (
        <div className={classes.full_height}>
			<main className={classes.main_container}>
				<div className={classes.news}>
						<Title	name="Báo chí hôm nay" date="Thứ Bảy, 19 tháng 5"/>
				</div>
			</main>
		</div>
    );
}

export default CategoryNews;