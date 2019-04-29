# Campfire Audio Vega
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -12.0; 25 -12.1; 28 -12.2; 31 -12.3; 34 -12.3; 37 -12.3; 41 -12.4; 45 -12.4; 49 -12.4; 54 -12.5; 60 -12.6; 66 -12.7; 72 -12.8; 79 -12.9; 87 -13.0; 96 -13.2; 106 -13.3; 116 -13.3; 128 -13.2; 141 -13.2; 155 -13.0; 170 -12.8; 187 -12.5; 206 -12.1; 227 -11.7; 249 -11.3; 274 -10.9; 302 -10.4; 332 -9.9; 365 -9.4; 402 -8.9; 442 -8.4; 486 -8.0; 535 -7.5; 588 -7.1; 647 -6.7; 712 -6.3; 783 -5.8; 861 -5.6; 947 -5.7; 1042 -5.9; 1146 -6.4; 1261 -7.4; 1387 -7.1; 1526 -6.3; 1678 -5.8; 1846 -4.8; 2031 -3.3; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -3.8; 6373 -6.6; 7010 -8.2; 7711 -10.3; 8482 -11.1; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.3  | -5.0 dB |
| Peaking | 166 Hz  | 0.59 | -4.7 dB |
| Peaking | 3721 Hz | 0.84 | 7.1 dB  |
| Peaking | 7896 Hz | 2.58 | -6.8 dB |
| Peaking | 955 Hz  | 1.48 | 3.0 dB  |
| Peaking | 1270 Hz | 1.03 | -3.2 dB |
| Peaking | 2336 Hz | 2.86 | 3.0 dB  |
| Peaking | 4268 Hz | 1.31 | -1.2 dB |
| Peaking | 4910 Hz | 4.2  | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Vega/Campfire%20Audio%20Vega.png)