# JH Audio 16v2 2 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.6; 28 -11.8; 31 -11.9; 34 -12.1; 37 -12.2; 41 -12.3; 45 -12.5; 49 -12.7; 54 -12.9; 60 -13.1; 66 -13.4; 72 -13.7; 79 -14.0; 87 -14.3; 96 -14.7; 106 -15.0; 116 -15.2; 128 -15.4; 141 -15.6; 155 -15.6; 170 -15.6; 187 -15.5; 206 -15.3; 227 -15.0; 249 -14.8; 274 -14.4; 302 -14.0; 332 -13.6; 365 -13.1; 402 -12.6; 442 -12.1; 486 -11.5; 535 -10.9; 588 -10.2; 647 -9.4; 712 -8.5; 783 -7.5; 861 -6.5; 947 -5.8; 1042 -5.5; 1146 -5.7; 1261 -5.6; 1387 -4.9; 1526 -3.6; 1678 -2.1; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.25 | -5.0 dB |
| Peaking | 136 Hz  | 0.74 | -3.6 dB |
| Peaking | 316 Hz  | 0.6  | -5.3 dB |
| Peaking | 2447 Hz | 0.8  | 6.5 dB  |
| Peaking | 5320 Hz | 2.11 | 4.6 dB  |
| Peaking | 935 Hz  | 4.54 | 1.1 dB  |
| Peaking | 1294 Hz | 5.84 | -1.2 dB |
| Peaking | 4015 Hz | 3.27 | 1.4 dB  |
| Peaking | 6427 Hz | 3.95 | 4.5 dB  |
| Peaking | 6881 Hz | 1.36 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2016v2%202%20Max/JH%20Audio%2016v2%202%20Max.png)