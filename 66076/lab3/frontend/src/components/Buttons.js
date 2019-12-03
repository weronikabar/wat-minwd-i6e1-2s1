import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';


class Buttons extends React.Component {

    useStyles = makeStyles(theme => ({
        root: {
            '& > *': {
                margin: theme.spacing(1),
                width: 200,
            },
        },
    }));

    onClick = () => {
        console.log("dupeczka")
        console.log(this.textInput)
    }

    textInput = "AAAAAAAAle dupeczka"
    render() {
        return (
            <>
                <form className={this.useStyles.root} noValidate autoComplete="off">
                    <TextField id="standard-basic" label="Github username" ref={(input) => this.textInput = input.getValue}/>
                </form>
                <br></br>
                <Button variant="contained" color="primary" onClick={this.onClick}>
                    Wyszukaj
                </Button>
            </>
        )
    }
}

export default Buttons