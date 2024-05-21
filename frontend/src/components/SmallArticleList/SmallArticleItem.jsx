import classes from "./SmallArticleList.module.css";
import { Link } from "react-router-dom";

const SmallArticleItem = ({ article }) => {
    return (
        <div className={classes.small_article_item}>
            <div className={classes.article_content}>
                <Link className={classes.article_link} to={`/article/${article._id}`}></Link>
                <div className={classes.article_text}>
                    <div className={classes.article_logo_wrapper}>
                        <img className={classes.article_logo} src={article.publisher_logo} alt=" Logo của trang báo" loading="lazy"/>
                    </div>
                    <div className={classes.article_title}>{article.title}</div>
                </div>
                <img className={classes.article_img} src={article.image.url_link} alt="Ảnh bài báo" loading="lazy"/>
            </div>
            <div className={classes.article_time}>{article.datetime}</div>
            
        </div>
    );
}

export default SmallArticleItem;