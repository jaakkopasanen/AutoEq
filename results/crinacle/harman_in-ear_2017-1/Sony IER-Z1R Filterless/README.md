# Sony IER-Z1R Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.0; 34 -7.2; 37 -7.4; 41 -7.5; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.0; 66 -8.1; 72 -8.3; 79 -8.5; 87 -8.6; 96 -8.7; 106 -8.8; 116 -8.8; 128 -8.8; 141 -8.7; 155 -8.5; 170 -8.1; 187 -7.8; 206 -7.5; 227 -7.1; 249 -6.7; 274 -6.3; 302 -6.0; 332 -5.6; 365 -5.4; 402 -5.3; 442 -5.2; 486 -5.1; 535 -5.0; 588 -5.0; 647 -4.9; 712 -4.9; 783 -4.9; 861 -5.0; 947 -5.3; 1042 -5.8; 1146 -6.6; 1261 -7.3; 1387 -7.7; 1526 -7.9; 1678 -7.9; 1846 -7.4; 2031 -6.2; 2234 -4.3; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -1.4; 3597 -6.1; 3957 -10.7; 4353 -10.9; 4788 -10.8; 5267 -8.7; 5793 -8.7; 6373 -11.5; 7010 -8.6; 7711 -9.3; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.7; 13660 -13.6; 15026 -21.8; 16529 -27.8; 18182 -24.8; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 100 Hz   | 1    | -2.6 dB  |
| Peaking | 2963 Hz  | 2.67 | 8.3 dB   |
| Peaking | 4198 Hz  | 3.14 | -6.4 dB  |
| Peaking | 6346 Hz  | 7.76 | -3.5 dB  |
| Peaking | 17190 Hz | 1.35 | -24.1 dB |
| Peaking | 660 Hz   | 0.81 | 1.9 dB   |
| Peaking | 1530 Hz  | 2.24 | -2.7 dB  |
| Peaking | 11503 Hz | 2.03 | 5.1 dB   |
| Peaking | 15462 Hz | 2.97 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -22.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20IER-Z1R%20Filterless/Sony%20IER-Z1R%20Filterless.png)