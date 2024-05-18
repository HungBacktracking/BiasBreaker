import classes from './Title.module.css';

function Title({name, date}) {
  return (
    <>
			<div className={classes.title}>
					<h1 className={classes.title_name}>{name}</h1>
					<p className={classes.title_date}>{date}</p>
			</div>
    </>
  );
}

export default Title;
