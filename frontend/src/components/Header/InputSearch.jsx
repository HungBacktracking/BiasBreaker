import classes from './Header.module.css';
import React, { useState } from 'react';

function InputSearch() {
	const [input, setInput] = useState('');

	const handleInputChange = (e) => {
		setInput(e.target.value);
	}

  return (
    <>
      <div className={classes.search_noti}>
				<form method="post" action="/search">
					<div className={`${classes.the_input_search} ${classes.ml_6}`}>
						<div className={classes.t_popper}>
							<div className={classes.t_popper__trigger}>
								<div className={`${classes.t_text_field__wrapper} ${classes.t_text_field___lg}`}>
									<span className={classes.t_text_field__prefix}><i className={`${classes.t_text_field__prefix_icon} ${classes.i_ui_search}`}></i></span> 
									<input onChange={handleInputChange} enterkeyhint="search" required name="search" inputmode="search" placeholder="Tìm kiếm chủ đề và các tin tức nóng hổi" autocomplete="off" type="text" value={input} className={classes.t_text_field}/> 
									<span className={classes.t_text_field__suffix}><i className={classes.t_text_field__clearable}></i></span>
								</div>
							</div> 
						</div>
					</div>
				</form>
				<i className={classes.noti_icon}></i>
			</div>
    </>
  );
  
}

export default InputSearch;
