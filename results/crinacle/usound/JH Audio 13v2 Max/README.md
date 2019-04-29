# JH Audio 13v2 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.3; 28 -11.4; 31 -11.5; 34 -11.6; 37 -11.7; 41 -11.8; 45 -11.9; 49 -12.0; 54 -12.1; 60 -12.2; 66 -12.4; 72 -12.5; 79 -12.7; 87 -12.9; 96 -13.1; 106 -13.2; 116 -13.2; 128 -13.2; 141 -13.2; 155 -13.0; 170 -12.8; 187 -12.6; 206 -12.3; 227 -11.9; 249 -11.4; 274 -11.0; 302 -10.5; 332 -10.0; 365 -9.4; 402 -8.9; 442 -8.3; 486 -7.8; 535 -7.2; 588 -6.6; 647 -6.0; 712 -5.4; 783 -4.7; 861 -4.3; 947 -4.1; 1042 -4.4; 1146 -4.8; 1261 -5.2; 1387 -5.4; 1526 -5.2; 1678 -4.9; 1846 -4.8; 2031 -5.1; 2234 -5.6; 2457 -5.9; 2703 -4.9; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.6; 6373 -3.4; 7010 -8.6; 7711 -13.6; 8482 -10.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.8; 18182 -16.4; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.34 | -5.0 dB  |
| Peaking | 136 Hz  | 0.91 | -4.3 dB  |
| Peaking | 261 Hz  | 1.58 | -2.6 dB  |
| Peaking | 4542 Hz | 0.9  | 7.0 dB   |
| Peaking | 7763 Hz | 4.02 | -10.8 dB |
| Peaking | 418 Hz  | 2.43 | -0.8 dB  |
| Peaking | 894 Hz  | 1.72 | 2.4 dB   |
| Peaking | 2595 Hz | 3.54 | -3.5 dB  |
| Peaking | 3052 Hz | 4.1  | 3.0 dB   |
| Peaking | 4300 Hz | 6.05 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2013v2%20Max/JH%20Audio%2013v2%20Max.png)