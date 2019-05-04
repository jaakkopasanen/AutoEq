# Sony IER-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.8; 31 -7.0; 34 -7.2; 37 -7.4; 41 -7.6; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.1; 66 -8.2; 72 -8.4; 79 -8.5; 87 -8.7; 96 -8.8; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.8; 155 -8.6; 170 -8.3; 187 -8.0; 206 -7.7; 227 -7.3; 249 -6.9; 274 -6.6; 302 -6.3; 332 -6.0; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.5; 535 -5.4; 588 -5.4; 647 -5.3; 712 -5.2; 783 -5.0; 861 -4.9; 947 -5.2; 1042 -5.6; 1146 -6.3; 1261 -7.0; 1387 -7.4; 1526 -7.2; 1678 -6.6; 1846 -5.6; 2031 -4.5; 2234 -3.2; 2457 -1.6; 2703 -0.5; 2973 -1.7; 3270 -4.8; 3597 -6.8; 3957 -6.9; 4353 -6.2; 4788 -4.6; 5267 -4.1; 5793 -6.5; 6373 -7.8; 7010 -6.3; 7711 -7.0; 8482 -7.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.6; 16529 -11.1; 18182 -12.4; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 69 Hz    | 0.79 | -2.1 dB |
| Peaking | 141 Hz   | 1.47 | -2.1 dB |
| Peaking | 2659 Hz  | 3.99 | 6.1 dB  |
| Peaking | 17852 Hz | 1.68 | -7.6 dB |
| Peaking | 20047 Hz | 2.44 | 0.9 dB  |
| Peaking | 1319 Hz  | 0.65 | 2.8 dB  |
| Peaking | 1413 Hz  | 1.67 | -4.4 dB |
| Peaking | 3816 Hz  | 3.73 | -2.4 dB |
| Peaking | 5258 Hz  | 3.82 | 3.8 dB  |
| Peaking | 5982 Hz  | 3.09 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20IER-Z1R/Sony%20IER-Z1R.png)