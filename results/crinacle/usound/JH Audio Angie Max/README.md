# JH Audio Angie Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.8; 25 -10.8; 28 -10.9; 31 -10.9; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.5; 60 -11.6; 66 -11.8; 72 -12.0; 79 -12.1; 87 -12.3; 96 -12.6; 106 -12.7; 116 -12.7; 128 -12.8; 141 -12.8; 155 -12.7; 170 -12.5; 187 -12.3; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.8; 302 -10.4; 332 -10.1; 365 -9.7; 402 -9.3; 442 -8.9; 486 -8.5; 535 -8.1; 588 -7.7; 647 -7.4; 712 -7.0; 783 -6.7; 861 -6.5; 947 -7.0; 1042 -8.2; 1146 -9.6; 1261 -10.6; 1387 -11.0; 1526 -10.4; 1678 -8.8; 1846 -6.6; 2031 -4.6; 2234 -3.2; 2457 -2.6; 2703 -3.0; 2973 -3.2; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.5; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.7; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 1.28 | -3.9 dB |
| Peaking | 44 Hz    | 0.27 | -3.8 dB |
| Peaking | 173 Hz   | 0.57 | -4.2 dB |
| Peaking | 1391 Hz  | 2.92 | -5.7 dB |
| Peaking | 4069 Hz  | 1    | 6.8 dB  |
| Peaking | 820 Hz   | 5.3  | 1.0 dB  |
| Peaking | 2280 Hz  | 7.2  | 1.8 dB  |
| Peaking | 6269 Hz  | 4.09 | 3.2 dB  |
| Peaking | 8122 Hz  | 3.94 | -4.4 dB |
| Peaking | 19584 Hz | 1.43 | -9.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Angie%20Max/JH%20Audio%20Angie%20Max.png)