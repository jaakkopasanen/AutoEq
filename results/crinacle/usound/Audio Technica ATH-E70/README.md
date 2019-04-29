# Audio Technica ATH-E70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.4; 28 -6.5; 31 -6.6; 34 -6.6; 37 -6.7; 41 -6.8; 45 -7.0; 49 -7.1; 54 -7.3; 60 -7.4; 66 -7.7; 72 -8.0; 79 -8.3; 87 -8.6; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -10.1; 155 -10.3; 170 -10.4; 187 -10.5; 206 -10.5; 227 -10.5; 249 -10.4; 274 -10.3; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.4; 442 -9.1; 486 -8.7; 535 -8.3; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.4; 861 -5.9; 947 -5.7; 1042 -5.8; 1146 -6.4; 1261 -7.1; 1387 -7.4; 1526 -7.2; 1678 -6.6; 1846 -5.8; 2031 -4.7; 2234 -3.2; 2457 -2.1; 2703 -1.8; 2973 -1.4; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.9; 6373 -5.2; 7010 -11.4; 7711 -14.4; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-E70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-E70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 170 Hz   | 0.68 | -3.7 dB  |
| Peaking | 370 Hz   | 1.28 | -1.8 dB  |
| Peaking | 1540 Hz  | 2.8  | -2.7 dB  |
| Peaking | 4326 Hz  | 0.67 | 7.2 dB   |
| Peaking | 7558 Hz  | 3.91 | -12.8 dB |
| Peaking | 15 Hz    | 1.07 | 0.8 dB   |
| Peaking | 913 Hz   | 4.88 | 1.0 dB   |
| Peaking | 4181 Hz  | 4.1  | -0.7 dB  |
| Peaking | 5519 Hz  | 7.79 | 1.4 dB   |
| Peaking | 12410 Hz | 1.87 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-E70/Audio%20Technica%20ATH-E70.png)