# JH Audio 16v2 2 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.4; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.7; 60 -7.1; 66 -7.5; 72 -7.9; 79 -8.3; 87 -8.8; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.4; 141 -10.6; 155 -10.9; 170 -11.0; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.1; 402 -9.9; 442 -9.6; 486 -9.3; 535 -8.9; 588 -8.5; 647 -8.0; 712 -7.5; 783 -6.9; 861 -6.4; 947 -6.1; 1042 -6.0; 1146 -6.1; 1261 -6.2; 1387 -6.0; 1526 -5.4; 1678 -4.5; 1846 -3.6; 2031 -3.2; 2234 -3.1; 2457 -3.2; 2703 -2.8; 2973 -2.6; 3270 -2.5; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -1.6; 7010 -4.0; 7711 -7.1; 8482 -11.0; 9330 -11.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.3; 20000 -16.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.59 | 2.8 dB  |
| Peaking | 120 Hz   | 0.92 | -1.9 dB |
| Peaking | 261 Hz   | 0.59 | -4.0 dB |
| Peaking | 4838 Hz  | 0.59 | 6.6 dB  |
| Peaking | 8823 Hz  | 2.78 | -9.4 dB |
| Peaking | 936 Hz   | 1.88 | 2.3 dB  |
| Peaking | 1013 Hz  | 1    | -1.7 dB |
| Peaking | 1919 Hz  | 3.43 | 1.4 dB  |
| Peaking | 3215 Hz  | 6.99 | -1.0 dB |
| Peaking | 19866 Hz | 1.61 | -9.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2016v2%202%20Min/JH%20Audio%2016v2%202%20Min.png)