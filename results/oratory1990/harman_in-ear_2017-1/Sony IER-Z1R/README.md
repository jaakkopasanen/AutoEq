# Sony IER-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.0; 28 -8.4; 31 -8.6; 34 -8.8; 37 -9.0; 41 -9.2; 45 -9.3; 49 -9.4; 54 -9.5; 60 -9.7; 66 -9.8; 72 -10.0; 79 -10.1; 87 -10.3; 96 -10.4; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.4; 155 -10.2; 170 -9.9; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.5; 274 -8.2; 302 -7.8; 332 -7.4; 365 -7.1; 402 -6.9; 442 -6.8; 486 -6.7; 535 -6.6; 588 -6.5; 647 -6.4; 712 -6.3; 783 -6.1; 861 -6.1; 947 -6.5; 1042 -6.9; 1146 -7.5; 1261 -7.9; 1387 -8.0; 1526 -7.6; 1678 -6.9; 1846 -5.9; 2031 -4.4; 2234 -2.5; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -3.0; 3597 -5.3; 3957 -5.8; 4353 -5.5; 4788 -4.1; 5267 -3.7; 5793 -5.9; 6373 -6.7; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -7.5; 11289 -7.3; 12418 -7.6; 13660 -13.3; 15026 -23.1; 16529 -30.4; 18182 -29.3; 20000 -16.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.48 | -2.7 dB  |
| Peaking | 145 Hz   | 0.89 | -2.6 dB  |
| Peaking | 2717 Hz  | 2.59 | 7.1 dB   |
| Peaking | 11185 Hz | 0.47 | 15.6 dB  |
| Peaking | 16848 Hz | 0.51 | -34.0 dB |
| Peaking | 1389 Hz  | 3.58 | -2.1 dB  |
| Peaking | 5110 Hz  | 6.2  | 3.0 dB   |
| Peaking | 12736 Hz | 2.9  | 6.8 dB   |
| Peaking | 12810 Hz | 1.11 | -3.8 dB  |
| Peaking | 18449 Hz | 5.93 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 16000 Hz | 1.41 | -26.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-Z1R/Sony%20IER-Z1R.png)