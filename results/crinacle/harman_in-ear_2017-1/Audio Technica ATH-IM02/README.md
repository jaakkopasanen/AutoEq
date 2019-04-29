# Audio Technica ATH-IM02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.5; 28 -4.8; 31 -5.1; 34 -5.4; 37 -5.6; 41 -5.8; 45 -6.0; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.3; 72 -7.7; 79 -8.1; 87 -8.5; 96 -9.1; 106 -9.5; 116 -9.8; 128 -10.2; 141 -10.6; 155 -10.9; 170 -11.1; 187 -11.2; 206 -11.3; 227 -11.3; 249 -11.3; 274 -11.2; 302 -11.1; 332 -10.8; 365 -10.5; 402 -10.2; 442 -10.0; 486 -9.6; 535 -9.2; 588 -8.8; 647 -8.3; 712 -7.8; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.7; 1146 -7.2; 1261 -7.6; 1387 -7.6; 1526 -7.4; 1678 -7.2; 1846 -7.1; 2031 -7.1; 2234 -6.9; 2457 -5.2; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.9; 5793 -6.7; 6373 -6.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -12.5; 13660 -21.4; 15026 -29.2; 16529 -32.1; 18182 -29.5; 20000 -22.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.2  | 2.5 dB   |
| Peaking | 303 Hz   | 0.26 | -6.0 dB  |
| Peaking | 1758 Hz  | 1.29 | -6.5 dB  |
| Peaking | 7162 Hz  | 0.17 | 19.8 dB  |
| Peaking | 16494 Hz | 0.35 | -39.9 dB |
| Peaking | 2315 Hz  | 4.38 | -3.9 dB  |
| Peaking | 2808 Hz  | 1.56 | 2.5 dB   |
| Peaking | 6051 Hz  | 6.35 | -5.8 dB  |
| Peaking | 11426 Hz | 3.31 | 6.2 dB   |
| Peaking | 14508 Hz | 3.38 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 16000 Hz | 1.41 | -33.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)