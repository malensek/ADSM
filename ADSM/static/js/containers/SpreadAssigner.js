'use strict';
/**
 * Created by josiah on 1/4/2016.
 */
import React, { Component, PropTypes } from 'react';
import {dispatch} from '../GlobalStore'
import {select_value_changed} from '../actions/actions'
//import {SelectBox} from './SelectBox' //TODO use This instead, remove collapsible element and title bar element
import SelectBox from 'react-select-box'


export default class SpreadAssigner extends Component {

    onChangeSource(event) {
        var {spread_type, pk, input_state, index} = this.props
        var new_value = event.target.value;
        new_value = Object.assign({}, input_state, {source: new_value})  //wrap in the old values
        dispatch(select_value_changed(spread_type, pk, index, 'source', new_value, input_state))
    }

    onChangeDestinations(new_destinations) {
        var {spread_type, pk, input_state, index} = this.props
        //TODO: check if number is already in the list and remove it if it is
        var new_value = Object.assign({}, input_state, {destinations: new_destinations})  //wrap in the old values
        dispatch(select_value_changed(spread_type, pk, index, 'destinations', new_value, input_state))
    }

    render(){
        var { population, spread_type, pk, input_state } = this.props
        var options = population.map(function(option, index){
            return <option value={option.pk} key={'s'+index}>{option.name}</option>;
        })
        var destination_options = population.map(function(option, index){
            return <option value={option.pk} key={'d'+index}>{option.name}</option>;
        })
        return (
            <div>
                <label htmlFor="source" className="control-label requiredField">
				    Source Production Type<span className="asteriskField">*</span>
                </label>
                <select name="source"
                        required
                        value={input_state.source}
                        onChange={this.onChangeSource.bind(this)}
                        key="source">
                    <option value="">------</option>
                    {options}
                </select>

                <label htmlFor="destinations" className="control-label requiredField">
				    Destinations<span className="asteriskField">*</span>
                </label>
                <SelectBox name="destinations" required
                           spread_type={spread_type}
                           pk={pk}
                           multiple={true}
                           value={input_state.destinations}
                           population={population}
                           onChange={this.onChangeDestinations.bind(this)}
                           key="destinations">
                    {destination_options}
                </SelectBox>

            </div>
        )
    }
}