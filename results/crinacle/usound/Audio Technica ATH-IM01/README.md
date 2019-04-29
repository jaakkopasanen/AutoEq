# Audio Technica ATH-IM01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.7; 25 -6.0; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.4; 45 -7.6; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.2; 106 -10.6; 116 -11.0; 128 -11.4; 141 -11.6; 155 -11.7; 170 -11.8; 187 -11.9; 206 -12.0; 227 -11.9; 249 -11.8; 274 -11.5; 302 -11.3; 332 -11.1; 365 -10.7; 402 -10.4; 442 -10.0; 486 -9.5; 535 -9.0; 588 -8.4; 647 -7.8; 712 -7.0; 783 -6.2; 861 -5.5; 947 -4.9; 1042 -4.7; 1146 -5.0; 1261 -5.2; 1387 -5.0; 1526 -4.4; 1678 -3.5; 1846 -2.4; 2031 -1.8; 2234 -1.5; 2457 -1.8; 2703 -2.7; 2973 -3.9; 3270 -4.2; 3597 -2.9; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.6; 6373 -5.5; 7010 -8.3; 7711 -8.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 158 Hz  | 0.61 | -5.1 dB |
| Peaking | 358 Hz  | 1.23 | -2.4 dB |
| Peaking | 2045 Hz | 1.15 | 4.2 dB  |
| Peaking | 5068 Hz | 1.67 | 6.7 dB  |
| Peaking | 7205 Hz | 3.25 | -5.2 dB |
| Peaking | 19 Hz   | 2    | 1.3 dB  |
| Peaking | 961 Hz  | 3.41 | 1.6 dB  |
| Peaking | 1449 Hz | 2.72 | -1.1 dB |
| Peaking | 3030 Hz | 1.66 | 1.9 dB  |
| Peaking | 3192 Hz | 3.99 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-IM01/Audio%20Technica%20ATH-IM01.png)