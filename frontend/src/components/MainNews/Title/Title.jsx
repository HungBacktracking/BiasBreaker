import classes from './Title.module.css';

function Title({name, description}) {
  return (
    <>
			<div className={classes.title}>
					<h1 className={classes.title_name}>{name}</h1>
					<p className={classes.title_date}>{description}</p>
			</div>
    </>
  );
}

export default Title;
