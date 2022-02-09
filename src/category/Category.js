import React from 'react';
import Collapsible from 'react-collapsible';
import CategoryHeader from './CategoryHeader.js';
import Product from '../product/Product.js'

class Category extends React.Component {

      categoryOnClose(id){ 
            var el = document
                  .getElementsByClassName("arrow_open")
                  .namedItem(id);
            el.classList.remove("arrow_open");

      }
      categoryOnOpen(id){
            var elems = document.getElementsByClassName("arrow")
            var el = elems.namedItem(id);
            el.classList.add("arrow_open");
      }
      render() {
      return (
            <Collapsible 
                  trigger=<CategoryHeader 
                        name={this.props.name}
                        />
                  onOpening={() => this.categoryOnOpen(this.props.name+"cat")}
                  onClosing={() => this.categoryOnClose(this.props.name+ "cat")}
                  >
            {this.props.pro.map( item =>
                  item.active ?
                        <Product key={item.name} product={item} />:
                        <div key={item.name}/>)}
            </Collapsible>
      );
      }
}
export default Category;
