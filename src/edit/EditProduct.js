import React from 'react';

class EditProduct extends React.Component{
      render(){
            var p = this.props.product
            return ( <div> <table> <tbody>
                  <tr>
                        <td>name</td>
                        <td><input value={p.name} /></td>
                  </tr>
                  <tr>
                        <td>volume</td>
                        <td><input value={p.volume}/></td>
                  </tr>
                  <tr>
                        <td>price</td>
                        <td><input value={p.price}/></td>
                  </tr>
                  <tr>
                        <td>priceIntern</td>
                        <td><input value={p.priceIntern}/></td>
                  </tr>
                  <tr>
                        <td>glutenfree</td>
                        <td><input type="checkbox" /></td>
                  </tr>
                  <tr>
                        <td>active</td>
                        <td><input type="checkbox" value={p.active} /></td>
                  </tr>
            </tbody> </table> </div>
            )
      }                 
}
                  export default EditProduct;
