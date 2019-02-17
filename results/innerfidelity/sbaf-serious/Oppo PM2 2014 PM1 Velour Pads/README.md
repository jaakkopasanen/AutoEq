# Oppo PM2 2014 PM1 Velour Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.6; 25 -3.8; 28 -3.9; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.3; 45 -4.2; 49 -4.2; 54 -4.2; 60 -4.2; 66 -4.5; 72 -5.2; 79 -5.8; 87 -6.1; 96 -6.5; 106 -6.7; 116 -6.9; 128 -7.2; 141 -7.4; 155 -7.4; 170 -7.5; 187 -7.8; 206 -8.3; 227 -8.6; 249 -8.6; 274 -8.2; 302 -7.4; 332 -6.7; 365 -6.8; 402 -6.8; 442 -6.9; 486 -7.7; 535 -8.1; 588 -7.9; 647 -7.9; 712 -7.2; 783 -6.6; 861 -7.2; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -6.4; 1387 -6.7; 1526 -6.9; 1678 -7.0; 1846 -6.5; 2031 -5.9; 2234 -4.9; 2457 -3.8; 2703 -3.1; 2973 -2.5; 3270 -2.5; 3597 -2.8; 3957 -2.6; 4353 -3.2; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.8; 9330 -9.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Velour Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Velour Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.3  | 3.1 dB  |
| Peaking | 56 Hz   | 2.73 | 2.2 dB  |
| Peaking | 3071 Hz | 2.37 | 3.5 dB  |
| Peaking | 5706 Hz | 1.87 | 6.4 dB  |
| Peaking | 8893 Hz | 3.6  | -4.9 dB |
| Peaking | 12 Hz   | 0.32 | 0.2 dB  |
| Peaking | 219 Hz  | 1.62 | -2.1 dB |
| Peaking | 580 Hz  | 3.14 | -1.6 dB |
| Peaking | 1694 Hz | 2.56 | -1.0 dB |
| Peaking | 2428 Hz | 4.51 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Velour%20Pads/Oppo%20PM2%202014%20PM1%20Velour%20Pads.png)