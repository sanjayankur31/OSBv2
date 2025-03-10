import React, { useState } from "react";
import Pagination from '@material-ui/lab/Pagination';
import { makeStyles } from "@material-ui/core/styles";
import theme from "../../theme";

type sizes = 'small' | 'medium' | 'large'
type colors = 'primary' | 'secondary' | 'standard'
type variants = 'outlined' | 'text'

interface OSBPaginationProps {
    totalPages: number,
    handlePageChange: (event: React.ChangeEvent<unknown>, pageNumber: number) => void,
    size?: sizes,
    color?: colors,
    variant?: variants,
    showFirstButton?: boolean,
    showLastButton?: boolean,
}

const useStyles = makeStyles(() => ({
    pagination: {
        padding: theme.spacing(2),
        display: 'flex',
        justifyContent: 'center',
        "& .MuiPagination-root": {
            "& .MuiPagination-ul": {
                "& li": {
                    "& .MuiPaginationItem-root": {
                        color: 'white',
                    },
                },
            },
        },
    },
}));

export default (props: OSBPaginationProps) => {

    const classes = useStyles();

    return(
        <Pagination
            className={classes.pagination} count={props.totalPages}
            color={typeof props.color === 'undefined' ? "standard" : props.color}
            size={typeof props.size === 'undefined' ? "medium" : props.size}
            variant={typeof props.variant === 'undefined' ? "text" : props.variant}
            showFirstButton={typeof props.showFirstButton === 'undefined' ? null : props.showFirstButton}
            showLastButton={typeof props.showLastButton === 'undefined' ? null : props.showLastButton}
            onChange={props.handlePageChange}
        />
    )

}