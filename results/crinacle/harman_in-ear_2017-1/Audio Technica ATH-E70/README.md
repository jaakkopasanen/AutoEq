# Audio Technica ATH-E70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.7; 31 -7.7; 34 -7.8; 37 -7.8; 41 -8.0; 45 -8.1; 49 -8.3; 54 -8.4; 60 -8.6; 66 -8.8; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.1; 106 -10.4; 116 -10.8; 128 -11.0; 141 -11.3; 155 -11.5; 170 -11.5; 187 -11.6; 206 -11.6; 227 -11.6; 249 -11.5; 274 -11.4; 302 -11.2; 332 -10.8; 365 -10.5; 402 -10.2; 442 -9.9; 486 -9.5; 535 -9.1; 588 -8.6; 647 -8.1; 712 -7.6; 783 -7.0; 861 -6.6; 947 -6.5; 1042 -6.6; 1146 -7.2; 1261 -7.6; 1387 -7.6; 1526 -7.2; 1678 -6.5; 1846 -5.6; 2031 -4.1; 2234 -2.1; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -3.7; 7010 -9.0; 7711 -11.4; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -21.2; 16529 -16.6; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-E70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-E70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.19 | -0.6 dB  |
| Peaking | 211 Hz   | 0.44 | -4.9 dB  |
| Peaking | 3586 Hz  | 1.07 | 7.2 dB   |
| Peaking | 15459 Hz | 2.61 | -16.7 dB |
| Peaking | 22050 Hz | 1.31 | -10.5 dB |
| Peaking | 1514 Hz  | 2.93 | -1.9 dB  |
| Peaking | 2411 Hz  | 6.13 | 2.5 dB   |
| Peaking | 5685 Hz  | 4.09 | 3.5 dB   |
| Peaking | 7474 Hz  | 5.64 | -7.5 dB  |
| Peaking | 12519 Hz | 4.72 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -11.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-E70/Audio%20Technica%20ATH-E70.png)