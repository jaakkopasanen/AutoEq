# Maximo iMetal iP-HS5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.5; 25 -14.4; 28 -14.2; 31 -14.0; 34 -13.9; 37 -13.7; 41 -13.5; 45 -13.3; 49 -13.2; 54 -13.0; 60 -12.9; 66 -12.7; 72 -12.6; 79 -12.4; 87 -12.2; 96 -12.0; 106 -11.7; 116 -11.5; 128 -11.2; 141 -11.0; 155 -10.7; 170 -10.4; 187 -10.0; 206 -9.6; 227 -9.1; 249 -8.7; 274 -8.2; 302 -7.7; 332 -7.2; 365 -7.0; 402 -6.7; 442 -6.3; 486 -6.0; 535 -5.7; 588 -5.5; 647 -5.3; 712 -5.1; 783 -5.2; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -9.1; 1526 -9.3; 1678 -9.9; 1846 -10.9; 2031 -11.8; 2234 -12.1; 2457 -11.3; 2703 -8.4; 2973 -4.7; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -3.0; 5267 -3.8; 5793 -6.3; 6373 -12.1; 7010 -11.1; 7711 -7.8; 8482 -6.5; 9330 -6.6; 10263 -8.3; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Maximo iMetal iP-HS5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Maximo iMetal iP-HS5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.27 | -7.8 dB  |
| Peaking | 133 Hz   | 1.02 | -2.4 dB  |
| Peaking | 2296 Hz  | 1.61 | -10.0 dB |
| Peaking | 3561 Hz  | 1.23 | 9.6 dB   |
| Peaking | 6561 Hz  | 4.46 | -8.6 dB  |
| Peaking | 230 Hz   | 2.46 | -0.7 dB  |
| Peaking | 741 Hz   | 1.05 | 2.0 dB   |
| Peaking | 1327 Hz  | 2.11 | -1.7 dB  |
| Peaking | 5574 Hz  | 7.82 | 1.1 dB   |
| Peaking | 10323 Hz | 7.17 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Maximo%20iMetal%20iP-HS5/Maximo%20iMetal%20iP-HS5.png)