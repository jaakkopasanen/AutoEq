# 64 Audio N8 M15 pre-RMA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.5; 28 -11.4; 31 -11.3; 34 -11.1; 37 -11.0; 41 -10.8; 45 -10.7; 49 -10.6; 54 -10.4; 60 -10.3; 66 -10.2; 72 -10.2; 79 -10.3; 87 -10.3; 96 -10.3; 106 -10.4; 116 -10.5; 128 -10.5; 141 -10.6; 155 -10.7; 170 -10.7; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.6; 274 -10.5; 302 -10.2; 332 -10.0; 365 -9.8; 402 -9.6; 442 -9.4; 486 -9.1; 535 -8.7; 588 -8.3; 647 -8.0; 712 -7.5; 783 -7.0; 861 -6.7; 947 -6.5; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -8.3; 1526 -8.2; 1678 -7.8; 1846 -7.1; 2031 -6.1; 2234 -4.8; 2457 -3.4; 2703 -2.1; 2973 -1.3; 3270 -0.9; 3597 -1.0; 3957 -1.5; 4353 -1.9; 4788 -2.6; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.1; 15026 -29.8; 16529 -34.2; 18182 -28.8; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 pre-RMA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 pre-RMA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.67 | -4.4 dB  |
| Peaking | 186 Hz   | 0.25 | -3.9 dB  |
| Peaking | 5563 Hz  | 0.57 | 13.6 dB  |
| Peaking | 12409 Hz | 1.53 | 17.8 dB  |
| Peaking | 16015 Hz | 0.54 | -36.1 dB |
| Peaking | 944 Hz   | 1.34 | 2.8 dB   |
| Peaking | 1497 Hz  | 0.98 | -3.7 dB  |
| Peaking | 2913 Hz  | 1.8  | 3.2 dB   |
| Peaking | 4873 Hz  | 6.62 | -2.5 dB  |
| Peaking | 9992 Hz  | 6.59 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -30.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20pre-RMA/64%20Audio%20N8%20M15%20pre-RMA.png)