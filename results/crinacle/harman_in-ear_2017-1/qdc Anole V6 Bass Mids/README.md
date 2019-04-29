# qdc Anole V6 Bass Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.1; 25 -9.2; 28 -9.3; 31 -9.3; 34 -9.3; 37 -9.3; 41 -9.4; 45 -9.4; 49 -9.4; 54 -9.4; 60 -9.4; 66 -9.4; 72 -9.6; 79 -9.7; 87 -9.7; 96 -9.9; 106 -9.9; 116 -9.9; 128 -9.8; 141 -9.7; 155 -9.5; 170 -9.3; 187 -9.0; 206 -8.7; 227 -8.4; 249 -8.1; 274 -7.8; 302 -7.4; 332 -7.0; 365 -6.7; 402 -6.6; 442 -6.5; 486 -6.4; 535 -6.5; 588 -6.6; 647 -6.9; 712 -7.1; 783 -7.3; 861 -7.6; 947 -8.1; 1042 -8.7; 1146 -9.4; 1261 -9.9; 1387 -9.9; 1526 -9.4; 1678 -8.7; 1846 -8.0; 2031 -7.1; 2234 -6.2; 2457 -5.1; 2703 -4.0; 2973 -3.0; 3270 -2.7; 3597 -3.0; 3957 -4.3; 4353 -4.9; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -9.8; 10263 -6.7; 11289 -6.5; 12418 -7.1; 13660 -17.8; 15026 -28.5; 16529 -31.1; 18182 -29.2; 20000 -31.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Bass Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Bass Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 72 Hz    | 0.29 | -3.5 dB  |
| Peaking | 1361 Hz  | 1.27 | -5.3 dB  |
| Peaking | 5877 Hz  | 0.28 | 26.2 dB  |
| Peaking | 12256 Hz | 1.81 | 18.1 dB  |
| Peaking | 15346 Hz | 0.17 | -39.9 dB |
| Peaking | 3112 Hz  | 4.05 | 1.5 dB   |
| Peaking | 4281 Hz  | 4.86 | -3.9 dB  |
| Peaking | 5584 Hz  | 2.14 | 2.0 dB   |
| Peaking | 9360 Hz  | 2.42 | -3.3 dB  |
| Peaking | 10322 Hz | 4.71 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 16000 Hz | 1.41 | -31.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V6%20Bass%20Mids/qdc%20Anole%20V6%20Bass%20Mids.png)