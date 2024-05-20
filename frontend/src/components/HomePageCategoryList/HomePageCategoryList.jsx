import React from 'react';
import classes from './HomePageCategoryList.module.css';
import CategoryItemList from './CategoryItemList';

const categoryList = ["chính trị", "kinh doanh", "thể thao", "giải trí", "công nghệ", "du lịch"];

const HomePageCategoryList = () => {
  

    return (
        <div className={classes.home_category}>
            
            {categoryList.map((category, index) => (
                <CategoryItemList key={index} category={category} />
            ))}
        </div>
    );
};
  
  export default HomePageCategoryList;