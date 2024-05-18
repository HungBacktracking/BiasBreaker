import classes from './MainNews.module.css';
import { motion } from "framer-motion";
import { fadeIn } from "./variant";

import Title from '../Title/Title';

function MainNews() {
  return (
    <>
      <div className={classes.full_height}>
				<main className={classes.main_container}>
					<div className={classes.news}>
							<Title	name="Tin tức hôm nay" date="Thứ Bảy, 18 tháng 5"/>
							<div className={classes.news_list}>
								<div className={classes.top_news}>
									
								</div>
								<div className={classes.for_you}>

								</div>
							</div>
					</div>
					<motion.div
						variants={fadeIn("up", 0.3)}
						initial="hidden"
						whileInView={"show"}
						viewport={{ once: false, amount: 0.2 }}
						className={classes.category_news}>
						

					</motion.div>
				</main>
      </div>
    </>
  );
}

export default MainNews;
