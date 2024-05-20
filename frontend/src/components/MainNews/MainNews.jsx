import React from 'react';
import classes from './MainNews.module.css';
import { motion } from 'framer-motion';
import { fadeIn } from './variant';

import Title from './Title/Title';
import Heading from './Heading/Heading';
import TopArticleList from '../TopArticleList/TopArticleList';
import SmallArticleList from '../SmallArticleList/SmallArticleList';
import ForYouArticleList from '../ForYouArticleList/ForYouArticleList';
import HomePageCategoryList from '../HomePageCategoryList/HomePageCategoryList';

function MainNews() {
  	return (
		<div className={classes.full_height}>
			<main className={classes.main_container}>
				<div className={classes.news}>
						<Title	name="Báo chí hôm nay" date="Thứ Bảy, 19 tháng 5"/>
						<div className={classes.news_list}>
							<div className={classes.top_news}>
								<Heading title='Tin tức hàng đầu'/>
								<TopArticleList />
							</div>
							<div className={classes.small_news}>
								<div className={classes.for_you}>
									<SmallArticleList isForYou={false}/>
								</div>
								<div className={classes.for_you}>
									<SmallArticleList isForYou={true}/>
								</div>
							</div>	
						</div>
				</div>
				<motion.div
					variants={fadeIn("up", 0.3)}
					initial="hidden"
					whileInView={"show"}
					viewport={{ once: false, amount: 0.1 }}
					className={classes.news}>
					
					<Title name="Dành cho bạn" date="Đề xuất dựa trên sở thích của riêng bạn"/>
					<ForYouArticleList />
				</motion.div>
				<motion.div
					variants={fadeIn("up", 0.3)}
					initial="hidden"
					whileInView={"show"}
					viewport={{ once: false, amount: 0.01 }}
					className={classes.news}>
					
					<Title name="Các chủ đề nóng" date="Báo mới ra lò, vừa thổi vừa xem"/>
					<HomePageCategoryList />
				</motion.div>
			</main>
		</div>
	);
}

export default MainNews;
