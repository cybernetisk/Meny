import React from 'react';
import VinboksProduct from './VinboksProduct.js'
import VinflaskeProduct from './VinflaskeProduct.js'
import RegularProduct from './RegularProduct.js'
import SnacksProduct from './SnacksProduct.js'

class Product extends React.Component{
      constructor(props){
            super();
            this.type = props.product.type;
            this.product = props.product;
      }
      render(){
            var type = this.type
            return ( 
            (parameter)=>{
            switch(parameter){
                  case "flaske":
                        return <VinflaskeProduct
                                    product={this.product}/>
                  case "boks": 
                        return <VinboksProduct
                                    product={this.product}/>
                  case "snacks":
                        return <SnacksProduct 
                                    product={this.product}/>

                  default:
                        return <RegularProduct
                                    product={this.product} />
            }
            })(type);
      }                 
}
export default Product;
