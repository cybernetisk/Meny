
import React from 'react';
class CategoryHeader extends React.Component {
      constructor(props){
            super();
            this.name  = props.name;
      }
      render(){
      return (
            <div className="categoryHeader">
                  <div className="arrow" id={this.name + "cat"}/>
                  <h2>{this.name}</h2>      
            </div>
      ) }
}

export default CategoryHeader;
