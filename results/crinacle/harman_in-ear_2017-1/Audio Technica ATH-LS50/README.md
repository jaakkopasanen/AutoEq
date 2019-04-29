# Audio Technica ATH-LS50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.4; 25 -11.6; 28 -11.8; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.3; 49 -12.4; 54 -12.5; 60 -12.7; 66 -12.8; 72 -12.9; 79 -13.1; 87 -13.2; 96 -13.4; 106 -13.5; 116 -13.5; 128 -13.5; 141 -13.4; 155 -13.3; 170 -13.0; 187 -12.7; 206 -12.4; 227 -11.9; 249 -11.5; 274 -10.9; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.4; 442 -7.8; 486 -7.2; 535 -6.5; 588 -5.9; 647 -5.3; 712 -4.7; 783 -4.1; 861 -3.8; 947 -4.0; 1042 -4.7; 1146 -6.1; 1261 -8.4; 1387 -10.4; 1526 -10.9; 1678 -10.1; 1846 -9.0; 2031 -7.6; 2234 -5.7; 2457 -3.4; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -3.4; 5267 -3.3; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.5; 15026 -17.1; 16529 -16.3; 18182 -16.5; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.38 | -5.4 dB  |
| Peaking | 131 Hz   | 0.96 | -4.4 dB  |
| Peaking | 242 Hz   | 1.7  | -2.8 dB  |
| Peaking | 3464 Hz  | 2.22 | 7.0 dB   |
| Peaking | 6070 Hz  | 4.36 | 5.6 dB   |
| Peaking | 930 Hz   | 1.62 | 4.3 dB   |
| Peaking | 1531 Hz  | 1.87 | -6.1 dB  |
| Peaking | 2651 Hz  | 3.87 | 3.2 dB   |
| Peaking | 11199 Hz | 1.06 | 5.7 dB   |
| Peaking | 19442 Hz | 0.23 | -13.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -13.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-LS50/Audio%20Technica%20ATH-LS50.png)