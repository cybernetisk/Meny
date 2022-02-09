import React from 'react';
import Name from './Name.js'
class VinflaskeProduct extends React.Component{
      render(){
      return (
                  <div className="product">
                        <Name product={this.props.product} />
                        <div className="productVolume">glass<br />flaske</div>
                        <div className="productPrice">{this.props.product.price1},- <br /> {this.props.product.price2},-</div>
                  </div>
            )
      }
}
export default VinflaskeProduct;
