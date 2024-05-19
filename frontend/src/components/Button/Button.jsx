import React from 'react';
import PropTypes from 'prop-types';
import classes from './Button.module.css';

Button.propTypes = {
  children: PropTypes.node,
  onClick: PropTypes.func,
  props: PropTypes.object,
  variant: PropTypes.oneOf(['fill', 'stroke']),
};

function Button({ children, onClick, ...props }) {
  const { variant } = props;

  let styledBtn = variant === 'stroke' ? classes.btn_stroke : classes.btn;

  return (
    console.log(props),
    (
      <button onClick={onClick} className={styledBtn}>
        {children}
      </button>
    )
  );
}

export default Button;
