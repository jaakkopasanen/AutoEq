import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Legend, Tooltip, ResponsiveContainer} from 'recharts';

class FrequencyResponseGraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }

    onLegendItemClick(item) {
        console.log(item);
    }

    render() {
        const data = [{frequency: 20, raw: 0.0}, {frequency: 613, raw: 0.8}, {frequency: 20e3, raw: 1}]
        const dataMin = Math.min(...data.map(o => o.raw));
        const dataMax = Math.max(...data.map(o => o.raw));
        return (
            <ResponsiveContainer aspect={2.5}>
                <LineChart data={data}>
                    <Line dataKey='raw' type='linear' dot={true} stroke='#8884d8' isAnimationActive={false} />
                    <CartesianGrid stroke='#cfcfcf' />
                    <XAxis
                        dataKey='frequency' scale='log' domain={[20, 20e3]} type='number'
                        fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
                    />
                    <YAxis
                        scale='linear'
                        domain={[
                            dataMin - (dataMax - dataMin) * 0.1,
                            dataMax + (dataMax - dataMin) * 0.1
                        ]}
                        fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
                    />
                    <Legend
                        layout='vertical' align='right' verticalAlign='middle' onClick={this.onLegendItemClick}
                        wrapperStyle={{fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif'}}
                    />
                    <Tooltip />
                </LineChart>
            </ResponsiveContainer>
        );
    }

}

export default FrequencyResponseGraph;
