import React, {useState} from 'react';
import {
  Box,
  Grid,
  IconButton,
  Link,
  ListItemIcon,
  ListItemText,
  Menu,
  MenuItem,
  SvgIcon,
  Typography
} from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import PrivacyTipIcon from '@mui/icons-material/PrivacyTip';
import GavelIcon from '@mui/icons-material/Gavel';
import HelpIcon from '@mui/icons-material/Help';
import CSVAutocomplete from "./CSVAutocomplete";

const GitHubIcon = (props) => {
  return (
    <SvgIcon {...props}>
      <path
        d='M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12'/>
    </SvgIcon>
  );
};

const IconAndText = (props) => {
  return (
    <Grid container direction='row' alignItems='center' sx={{color: theme => theme.palette.text.primary}}>
      <Grid item><ListItemIcon sx={{color: theme => theme.palette.text.primary, height: '24px'}}>{props.icon}</ListItemIcon></Grid>
      <Grid item><ListItemText>{props.label}</ListItemText></Grid>
    </Grid>
  );
};

const TopBar = (props) => {
  const [menuAnchor, setMenuAnchor] = useState(null);
  const isMenuOpen = Boolean(menuAnchor);

  const onShowInfoClick = () => {
    setMenuAnchor(null);
    props.onShowInfoClicked();
  };

  return (
    <Grid item container direction='row' justifyContent='space-between' alignItems='center'>
      <Grid item sx={{ width: {xs: '60px', sm: '100px'}}} >
        <img
          src='autoeq_logo.svg'
          alt='AutoEq logo'
          style={{width: '100%', display: props.showLogo ? 'block' : 'none' }}
        />
      </Grid>
      <Grid item sx={{width: {xs: '200px', sm: '400px', md: '500px'}}}>
        <CSVAutocomplete
          value={props.selectedMeasurement}
          options={props.measurements || []}
          onChange={props.onMeasurementSelected}
          autocompleteProps={{
            size: 'large',
            blurOnSelect: true,
          }}
          label='Select headphones'
          onOptionCreated={props.onMeasurementCreated}
          onError={props.onError}
          virtualize
          renderOption={(liProps, option, style) => (
            <Box component='li' { ...liProps } style={{ ...style, top: (style.top) + 8, borderBottom: '1px solid #eee' }}>
              <Typography>{option.label}</Typography>
              <Typography variant='caption' sx={{whiteSpace: 'nowrap', ml: 'auto', textAlign: 'right'}}>
                by {option.source}
                {option.rig !== 'unknown' && <br />}
                {option.rig !== 'unknown' && (`on ${option.rig}`)}
              </Typography>
            </Box>
          )}
        />
      </Grid>
      <Grid item>
        <IconButton onClick={(e) => setMenuAnchor(!!menuAnchor ? null : e.currentTarget)}>
          <MoreVertIcon sx={{color: theme => theme.palette.grey.A200}} />
        </IconButton>
      </Grid>
      <Menu
        open={isMenuOpen} anchorEl={menuAnchor} onClose={() => setMenuAnchor(null)}
        anchorOrigin={{ vertical: 'top', horizontal: 'left' }}
        PaperProps={{sx: {width: '200px'}}}
      >
        <MenuItem onClick={onShowInfoClick}>
          <IconAndText icon={<HelpIcon />} label='Show Info' />
        </MenuItem>
        <MenuItem>
          <Link href='https://github.com/jaakkopasanen/AutoEq' target='_blank' rel='noopener' sx={{textDecoration: 'none'}}>
            <IconAndText icon={<GitHubIcon sx={{color: '#000'}} />} label='Github' />
          </Link>
        </MenuItem>
        <MenuItem>
          <Link href='/legal/privacy-policy.html' target='_blank' rel='noopener' sx={{textDecoration: 'none'}}>
            <IconAndText icon={<PrivacyTipIcon />} label='Privacy Policy' />
          </Link>
        </MenuItem>
        <MenuItem>
          <Link href='/legal/terms-of-service.html' target='_blank' rel='noopener' sx={{textDecoration: 'none'}}>
            <IconAndText icon={<GavelIcon />} label='Terms of Service' />
          </Link>
        </MenuItem>
      </Menu>
    </Grid>
  )
}

export default TopBar;
