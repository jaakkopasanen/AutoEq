# qdc Anole V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.5; 25 -9.6; 28 -9.6; 31 -9.7; 34 -9.7; 37 -9.8; 41 -9.8; 45 -9.8; 49 -9.9; 54 -9.9; 60 -9.9; 66 -10.0; 72 -10.1; 79 -10.1; 87 -10.3; 96 -10.4; 106 -10.5; 116 -10.4; 128 -10.3; 141 -10.3; 155 -10.2; 170 -10.0; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.9; 274 -8.6; 302 -8.2; 332 -7.9; 365 -7.6; 402 -7.4; 442 -7.2; 486 -7.0; 535 -6.9; 588 -6.8; 647 -6.8; 712 -6.7; 783 -6.6; 861 -6.6; 947 -6.9; 1042 -7.4; 1146 -8.2; 1261 -8.9; 1387 -9.1; 1526 -8.9; 1678 -8.4; 1846 -7.9; 2031 -7.2; 2234 -6.1; 2457 -4.9; 2703 -3.6; 2973 -2.7; 3270 -2.6; 3597 -2.9; 3957 -3.7; 4353 -3.7; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.6; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -18.7; 15026 -29.2; 16529 -32.1; 18182 -30.7; 20000 -33.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 1.29 | -2.8 dB  |
| Peaking | 28 Hz    | 0.57 | -2.3 dB  |
| Peaking | 125 Hz   | 0.5  | -3.6 dB  |
| Peaking | 3189 Hz  | 3.38 | 4.0 dB   |
| Peaking | 5495 Hz  | 3.11 | 6.9 dB   |
| Peaking | 1451 Hz  | 1.66 | -3.6 dB  |
| Peaking | 3201 Hz  | 0.26 | 9.6 dB   |
| Peaking | 7394 Hz  | 0.49 | 11.4 dB  |
| Peaking | 12065 Hz | 1.52 | 20.3 dB  |
| Peaking | 15449 Hz | 0.16 | -35.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.3 dB   |
| Peaking | 16000 Hz | 1.41 | -33.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V6/qdc%20Anole%20V6.png)