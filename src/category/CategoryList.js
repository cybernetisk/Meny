import React from 'react';

import Category from './Category.js'

class CategoryList extends React.Component {
      constructor(props){
            super();
            this.categories =props.categories;
      }
      render() {
      return (<ul>{
            this.categories.map(
                  item => ( <li key={item.name}>
                        <Category
                              name={item.name}
                              pro={item.products}
                        /></li>
                  )
            )
            }</ul>);
      }
}
export default CategoryList
