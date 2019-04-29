# 64 Audio N8 M15 custom sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.3; 25 -10.5; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.6; 41 -10.6; 45 -10.6; 49 -10.6; 54 -10.6; 60 -10.5; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.8; 96 -10.8; 106 -10.8; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.6; 170 -10.5; 187 -10.4; 206 -10.2; 227 -10.0; 249 -9.8; 274 -9.6; 302 -9.3; 332 -9.1; 365 -8.9; 402 -8.6; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.4; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.5; 947 -5.3; 1042 -5.5; 1146 -6.2; 1261 -7.2; 1387 -7.9; 1526 -8.2; 1678 -8.0; 1846 -7.7; 2031 -7.2; 2234 -6.6; 2457 -5.5; 2703 -4.3; 2973 -3.3; 3270 -2.6; 3597 -2.4; 3957 -2.7; 4353 -3.0; 4788 -3.6; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.17 | -4.4 dB |
| Peaking | 920 Hz  | 1.31 | 4.0 dB  |
| Peaking | 2414 Hz | 0.38 | -4.9 dB |
| Peaking | 3338 Hz | 1.14 | 8.1 dB  |
| Peaking | 5970 Hz | 2.99 | 6.7 dB  |
| Peaking | 61 Hz   | 3.03 | 0.4 dB  |
| Peaking | 1098 Hz | 5.85 | 0.3 dB  |
| Peaking | 1436 Hz | 4.63 | -0.4 dB |
| Peaking | 7834 Hz | 5.78 | -1.0 dB |
| Peaking | 9022 Hz | 0.69 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20custom%20sample%203/64%20Audio%20N8%20M15%20custom%20sample%203.png)