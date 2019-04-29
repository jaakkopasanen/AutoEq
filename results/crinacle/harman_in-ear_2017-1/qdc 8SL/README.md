# qdc 8SL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.0; 25 -8.3; 28 -8.6; 31 -8.8; 34 -8.9; 37 -8.9; 41 -9.0; 45 -9.2; 49 -9.4; 54 -9.5; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.4; 96 -10.6; 106 -10.7; 116 -10.8; 128 -10.8; 141 -10.8; 155 -10.6; 170 -10.4; 187 -10.2; 206 -10.0; 227 -9.7; 249 -9.2; 274 -8.8; 302 -8.4; 332 -7.9; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.5; 712 -6.6; 783 -6.7; 861 -7.0; 947 -7.4; 1042 -8.1; 1146 -8.8; 1261 -9.3; 1387 -9.2; 1526 -8.6; 1678 -7.9; 1846 -7.1; 2031 -6.3; 2234 -5.1; 2457 -4.2; 2703 -2.8; 2973 -1.5; 3270 -1.5; 3597 -2.2; 3957 -2.7; 4353 -4.1; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -8.7; 13660 -17.2; 15026 -21.3; 16529 -20.3; 18182 -21.3; 20000 -25.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.46 | -2.8 dB  |
| Peaking | 158 Hz   | 0.92 | -2.9 dB  |
| Peaking | 1358 Hz  | 2.15 | -3.2 dB  |
| Peaking | 3128 Hz  | 2.16 | 5.2 dB   |
| Peaking | 5612 Hz  | 3.19 | 6.4 dB   |
| Peaking | 268 Hz   | 2.81 | -0.6 dB  |
| Peaking | 532 Hz   | 1.39 | 0.7 dB   |
| Peaking | 9798 Hz  | 0.58 | 9.5 dB   |
| Peaking | 18278 Hz | 0.21 | -18.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -20.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%208SL/qdc%208SL.png)