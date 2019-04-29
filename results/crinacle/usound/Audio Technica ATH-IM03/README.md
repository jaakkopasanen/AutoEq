# Audio Technica ATH-IM03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.3; 25 -5.8; 28 -6.3; 31 -6.7; 34 -7.1; 37 -7.4; 41 -7.7; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.7; 66 -9.0; 72 -9.3; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.4; 116 -10.7; 128 -10.9; 141 -11.0; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.0; 227 -11.0; 249 -10.8; 274 -10.6; 302 -10.4; 332 -10.1; 365 -9.8; 402 -9.4; 442 -9.1; 486 -8.7; 535 -8.2; 588 -7.8; 647 -7.2; 712 -6.6; 783 -6.0; 861 -5.5; 947 -5.2; 1042 -5.3; 1146 -5.8; 1261 -6.3; 1387 -6.5; 1526 -6.1; 1678 -5.4; 1846 -4.7; 2031 -4.3; 2234 -4.3; 2457 -4.4; 2703 -3.7; 2973 -2.9; 3270 -2.3; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -4.2; 7010 -9.8; 7711 -11.7; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 2.23 | 2.3 dB  |
| Peaking | 134 Hz   | 0.56 | -4.2 dB |
| Peaking | 306 Hz   | 1.21 | -2.2 dB |
| Peaking | 4892 Hz  | 0.88 | 7.3 dB  |
| Peaking | 7440 Hz  | 3.63 | -9.9 dB |
| Peaking | 18 Hz    | 1.57 | 0.6 dB  |
| Peaking | 921 Hz   | 3.83 | 1.6 dB  |
| Peaking | 5815 Hz  | 8.53 | 1.1 dB  |
| Peaking | 10818 Hz | 3.23 | -0.6 dB |
| Peaking | 13421 Hz | 1.27 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-IM03/Audio%20Technica%20ATH-IM03.png)