import React from 'react';
import classes from './Heading.module.css';

const Heading = ( { title, color} ) => {
    return (
        <div className={classes.heading}>
            <h3 className={`${classes.heading_title} ${classes[color]}`}>{title}</h3>
            <i className={`${classes.heading_icon} ${classes[color]} fa-solid fa-chevron-right`}></i>
        </div>
    )
}

export default Heading;