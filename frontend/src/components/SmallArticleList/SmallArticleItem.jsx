import classes from "./SmallArticleList.module.css";
import { Link } from "react-router-dom";

const SmallArticleItem = ({ article }) => {
    return (
        <div className={classes.small_article_item}>
            <div className={classes.article_content}>
                <Link className={classes.article_link} to={`/article/${article.id}`}></Link>
                <div className={classes.article_text}>
                    <div className={classes.article_logo_wrapper}>
                        <img className={classes.article_logo} src="https://lh3.googleusercontent.com/coH48HKromjaVo7QiwPfRSDMLsAq3as7MW4dPt48iBT7jlEXP8sTtV_UW9RVLEUHdcgSKsZJ8Q=h24-rw" alt=" Logo của trang báo" loading="lazy"/>
                    </div>
                    <div className={classes.article_title}>{article.title}</div>
                </div>
                <img className={classes.article_img} src={article.imagePath} alt="Ảnh bài báo" loading="lazy"/>
            </div>
            <div className={classes.article_time}>{article.time}</div>
            
        </div>
    );
}

export default SmallArticleItem;