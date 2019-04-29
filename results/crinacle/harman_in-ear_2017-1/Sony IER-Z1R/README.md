# Sony IER-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.4; 25 -8.7; 28 -9.0; 31 -9.2; 34 -9.4; 37 -9.5; 41 -9.7; 45 -9.8; 49 -9.9; 54 -10.0; 60 -10.1; 66 -10.3; 72 -10.4; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.9; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.2; 187 -9.9; 206 -9.5; 227 -9.1; 249 -8.8; 274 -8.4; 302 -8.1; 332 -7.6; 365 -7.4; 402 -7.2; 442 -7.1; 486 -7.0; 535 -6.9; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -7.0; 1146 -7.5; 1261 -8.0; 1387 -8.1; 1526 -7.8; 1678 -7.1; 1846 -6.1; 2031 -4.7; 2234 -3.0; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -2.9; 3597 -5.0; 3957 -5.1; 4353 -4.9; 4788 -3.5; 5267 -2.7; 5793 -4.6; 6373 -5.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -7.1; 11289 -7.6; 12418 -9.3; 13660 -15.2; 15026 -23.9; 16529 -30.4; 18182 -29.3; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.53 | -2.4 dB  |
| Peaking | 131 Hz   | 0.64 | -3.6 dB  |
| Peaking | 2733 Hz  | 3    | 6.5 dB   |
| Peaking | 10357 Hz | 0.47 | 13.0 dB  |
| Peaking | 16877 Hz | 0.54 | -31.8 dB |
| Peaking | 1398 Hz  | 3.1  | -2.3 dB  |
| Peaking | 5150 Hz  | 6.3  | 2.9 dB   |
| Peaking | 8963 Hz  | 2.47 | -1.7 dB  |
| Peaking | 12458 Hz | 2.85 | 2.8 dB   |
| Peaking | 15060 Hz | 3.9  | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -27.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20IER-Z1R/Sony%20IER-Z1R.png)