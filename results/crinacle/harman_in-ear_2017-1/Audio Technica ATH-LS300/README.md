# Audio Technica ATH-LS300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.5; 25 -11.5; 28 -11.6; 31 -11.6; 34 -11.6; 37 -11.5; 41 -11.6; 45 -11.5; 49 -11.5; 54 -11.5; 60 -11.5; 66 -11.6; 72 -11.7; 79 -11.8; 87 -11.9; 96 -12.1; 106 -12.1; 116 -12.2; 128 -12.3; 141 -12.4; 155 -12.4; 170 -12.4; 187 -12.3; 206 -12.2; 227 -12.2; 249 -12.0; 274 -11.9; 302 -11.7; 332 -11.4; 365 -11.1; 402 -10.8; 442 -10.5; 486 -10.1; 535 -9.8; 588 -9.3; 647 -8.9; 712 -8.3; 783 -7.8; 861 -7.5; 947 -7.3; 1042 -7.6; 1146 -8.1; 1261 -8.6; 1387 -8.5; 1526 -8.1; 1678 -7.3; 1846 -6.4; 2031 -5.1; 2234 -3.7; 2457 -2.5; 2703 -1.8; 2973 -1.6; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.9; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -18.5; 16529 -18.8; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.14 | -4.7 dB  |
| Peaking | 251 Hz   | 0.47 | -4.5 dB  |
| Peaking | 1461 Hz  | 2.33 | -2.9 dB  |
| Peaking | 3986 Hz  | 0.81 | 6.8 dB   |
| Peaking | 15951 Hz | 2.84 | -16.8 dB |
| Peaking | 877 Hz   | 5.13 | 0.5 dB   |
| Peaking | 6393 Hz  | 3.56 | 4.6 dB   |
| Peaking | 7354 Hz  | 2.86 | -4.7 dB  |
| Peaking | 13517 Hz | 6.26 | 3.6 dB   |
| Peaking | 18660 Hz | 5.21 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-LS300/Audio%20Technica%20ATH-LS300.png)