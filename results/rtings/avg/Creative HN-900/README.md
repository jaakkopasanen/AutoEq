# Creative HN-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.8; 49 -3.3; 54 -5.1; 60 -5.7; 66 -5.3; 72 -6.7; 79 -9.7; 87 -11.7; 96 -12.9; 106 -13.6; 116 -13.9; 128 -14.1; 141 -13.9; 155 -13.9; 170 -13.7; 187 -13.1; 206 -12.6; 227 -12.1; 249 -11.6; 274 -11.1; 302 -10.6; 332 -10.1; 365 -9.8; 402 -9.7; 442 -9.8; 486 -10.2; 535 -10.9; 588 -11.9; 647 -12.8; 712 -12.5; 783 -11.1; 861 -8.5; 947 -6.2; 1042 -5.9; 1146 -7.4; 1261 -5.5; 1387 -3.2; 1526 -2.7; 1678 -1.6; 1846 -0.5; 2031 -0.8; 2234 -2.6; 2457 -4.3; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -6.7; 5793 -5.1; 6373 -5.2; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.7; 13660 -12.0; 15026 -12.2; 16529 -10.3; 18182 -9.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.38 | 10.6 dB  |
| Peaking | 112 Hz   | 0.54 | -13.5 dB |
| Peaking | 665 Hz   | 2.58 | -5.8 dB  |
| Peaking | 1785 Hz  | 2.02 | 5.6 dB   |
| Peaking | 3696 Hz  | 1.86 | 6.5 dB   |
| Peaking | 2497 Hz  | 6.64 | -3.8 dB  |
| Peaking | 2695 Hz  | 2.99 | 2.6 dB   |
| Peaking | 8526 Hz  | 0.83 | 3.9 dB   |
| Peaking | 11355 Hz | 3.14 | 3.9 dB   |
| Peaking | 13616 Hz | 0.41 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20HN-900/Creative%20HN-900.png)