import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios';

class Buttons extends React.Component {

    state = {
        input: '',
        graphDepth: ''
    }

    useStyles = makeStyles(theme => ({
        root: {
            '& > *': {
                margin: theme.spacing(1),
                width: 200,
            },
        },
    }));

    handleChange = event => {
        this.setState({ input: event.target.value });
    }

    handleSubmit = event => {
        event.preventDefault();

        const input = {
            input: this.state.input,
            graphDepth: 3
        };
        console.log(input)
        axios.post(`http://localhost:8090/getUserData`, { input })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
    }

    render() {
        return (
            <>
                <form className={this.useStyles.root} noValidate autoComplete="off">
                    <TextField id="standard-basic" label="Github username" onChange={this.handleChange} />
                </form>
                <br></br>
                <Button variant="contained" color="primary" type="submit" onClick={this.handleSubmit} >
                    Wyszukaj
                </Button>
            </>
        )
    }
}

export default Buttons