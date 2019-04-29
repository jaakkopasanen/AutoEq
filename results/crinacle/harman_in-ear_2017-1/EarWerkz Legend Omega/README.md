# EarWerkz Legend Omega
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.7; 28 -7.2; 31 -7.6; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.7; 49 -8.9; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.5; 87 -10.9; 96 -11.3; 106 -11.7; 116 -12.0; 128 -12.3; 141 -12.5; 155 -12.6; 170 -12.7; 187 -12.8; 206 -12.8; 227 -12.7; 249 -12.5; 274 -12.4; 302 -12.1; 332 -11.7; 365 -11.3; 402 -10.9; 442 -10.6; 486 -10.2; 535 -9.7; 588 -9.2; 647 -8.8; 712 -8.2; 783 -7.7; 861 -7.3; 947 -7.3; 1042 -7.6; 1146 -8.4; 1261 -9.2; 1387 -9.8; 1526 -10.1; 1678 -9.6; 1846 -8.7; 2031 -8.1; 2234 -5.6; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.4; 15026 -19.4; 16529 -14.8; 18182 -9.0; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`EarWerkz Legend Omega GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `EarWerkz Legend Omega ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.55 | -2.8 dB  |
| Peaking | 259 Hz   | 0.51 | -4.9 dB  |
| Peaking | 1718 Hz  | 1.28 | -9.7 dB  |
| Peaking | 2934 Hz  | 0.55 | 9.4 dB   |
| Peaking | 15391 Hz | 2.13 | -14.3 dB |
| Peaking | 17 Hz    | 2.15 | 1.3 dB   |
| Peaking | 1293 Hz  | 6.34 | -0.6 dB  |
| Peaking | 6319 Hz  | 2.95 | 4.4 dB   |
| Peaking | 7378 Hz  | 1.91 | -3.8 dB  |
| Peaking | 12673 Hz | 5.62 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/EarWerkz%20Legend%20Omega/EarWerkz%20Legend%20Omega.png)