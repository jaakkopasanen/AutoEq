# JH Audio Billie Jean
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.8; 28 -7.9; 31 -8.0; 34 -8.0; 37 -8.0; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.3; 79 -9.5; 87 -9.8; 96 -10.2; 106 -10.5; 116 -10.8; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.3; 187 -11.3; 206 -11.2; 227 -11.0; 249 -10.8; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.5; 402 -9.1; 442 -8.7; 486 -8.3; 535 -7.9; 588 -7.4; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.6; 947 -5.5; 1042 -5.9; 1146 -6.8; 1261 -7.9; 1387 -8.8; 1526 -9.0; 1678 -8.2; 1846 -6.1; 2031 -3.2; 2234 -2.1; 2457 -2.9; 2703 -2.2; 2973 -0.6; 3270 -0.5; 3597 -0.6; 3957 -2.5; 4353 -0.7; 4788 -0.5; 5267 -2.7; 5793 -4.6; 6373 -4.1; 7010 -7.5; 7711 -8.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Billie Jean GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Billie Jean ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 86 Hz   | 0.4  | -2.0 dB |
| Peaking | 204 Hz  | 0.7  | -3.7 dB |
| Peaking | 1531 Hz | 3.64 | -4.4 dB |
| Peaking | 2961 Hz | 1.16 | 5.8 dB  |
| Peaking | 4750 Hz | 4.7  | 4.1 dB  |
| Peaking | 892 Hz  | 2.83 | 1.5 dB  |
| Peaking | 1268 Hz | 5.52 | -1.0 dB |
| Peaking | 3499 Hz | 8.78 | 0.9 dB  |
| Peaking | 6481 Hz | 7.7  | 2.0 dB  |
| Peaking | 7314 Hz | 5.45 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Billie%20Jean/JH%20Audio%20Billie%20Jean.png)