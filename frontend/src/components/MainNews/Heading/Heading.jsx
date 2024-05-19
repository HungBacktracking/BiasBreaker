import React from 'react';
import classes from './Heading.module.css';

const Heading = ( { title } ) => {
    return (
        <div className={classes.heading}>
            <h3 className={classes.heading_title}>{title}</h3>
            <i className={`${classes.heading_icon} fa-solid fa-chevron-right`}></i>
        </div>
    )
}

export default Heading;