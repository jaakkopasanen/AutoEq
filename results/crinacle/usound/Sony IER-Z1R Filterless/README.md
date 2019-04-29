# Sony IER-Z1R Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.1; 28 -5.5; 31 -5.7; 34 -5.9; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.5; 54 -6.6; 60 -6.7; 66 -6.8; 72 -7.0; 79 -7.2; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.5; 128 -7.5; 141 -7.3; 155 -7.1; 170 -6.8; 187 -6.5; 206 -6.1; 227 -5.8; 249 -5.4; 274 -5.0; 302 -4.7; 332 -4.5; 365 -4.4; 402 -4.2; 442 -4.2; 486 -4.2; 535 -4.1; 588 -4.1; 647 -4.1; 712 -4.0; 783 -4.1; 861 -4.1; 947 -4.3; 1042 -4.8; 1146 -5.7; 1261 -6.6; 1387 -7.3; 1526 -7.8; 1678 -7.8; 1846 -7.4; 2031 -6.6; 2234 -5.2; 2457 -3.4; 2703 -0.8; 2973 -0.5; 3270 -3.4; 3597 -7.9; 3957 -12.1; 4353 -11.9; 4788 -11.5; 5267 -9.4; 5793 -9.6; 6373 -12.8; 7010 -10.8; 7711 -12.1; 8482 -9.4; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -8.7; 18182 -8.1; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 544 Hz   | 1.05 | 2.6 dB  |
| Peaking | 2942 Hz  | 3.65 | 8.4 dB  |
| Peaking | 4156 Hz  | 2.46 | -6.7 dB |
| Peaking | 7024 Hz  | 2.51 | -5.4 dB |
| Peaking | 17306 Hz | 2.98 | -3.4 dB |
| Peaking | 18 Hz    | 1.6  | 1.8 dB  |
| Peaking | 108 Hz   | 1.39 | -1.5 dB |
| Peaking | 930 Hz   | 3.12 | 1.3 dB  |
| Peaking | 1576 Hz  | 2.81 | -2.3 dB |
| Peaking | 9742 Hz  | 5.35 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-Z1R%20Filterless/Sony%20IER-Z1R%20Filterless.png)