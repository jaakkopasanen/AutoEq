# 64 Audio N8 M15 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.5; 28 -6.9; 31 -7.1; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.7; 54 -7.7; 60 -7.8; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.2; 96 -8.2; 106 -8.1; 116 -8.2; 128 -8.1; 141 -7.9; 155 -7.7; 170 -7.5; 187 -7.4; 206 -7.1; 227 -6.8; 249 -6.5; 274 -6.2; 302 -5.9; 332 -5.6; 365 -5.4; 402 -5.1; 442 -5.0; 486 -4.7; 535 -4.5; 588 -4.4; 647 -4.2; 712 -3.8; 783 -3.5; 861 -3.1; 947 -3.0; 1042 -3.2; 1146 -3.8; 1261 -4.6; 1387 -5.0; 1526 -4.8; 1678 -4.3; 1846 -3.7; 2031 -3.2; 2234 -2.8; 2457 -2.2; 2703 -1.6; 2973 -1.1; 3270 -1.0; 3597 -1.4; 3957 -2.2; 4353 -2.7; 4788 -3.8; 5267 -3.2; 5793 -0.5; 6373 -1.5; 7010 -3.1; 7711 -4.0; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -7.1; 18182 -16.1; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 83 Hz    | 0.34 | -3.9 dB  |
| Peaking | 851 Hz   | 2.95 | 1.5 dB   |
| Peaking | 3707 Hz  | 0.82 | 2.8 dB   |
| Peaking | 15666 Hz | 1.53 | 4.7 dB   |
| Peaking | 18171 Hz | 1.18 | -13.7 dB |
| Peaking | 1480 Hz  | 3.99 | -1.5 dB  |
| Peaking | 3005 Hz  | 3.09 | 1.0 dB   |
| Peaking | 5070 Hz  | 3.22 | -3.5 dB  |
| Peaking | 5789 Hz  | 3.53 | 4.1 dB   |
| Peaking | 7962 Hz  | 3.9  | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20sample%203/64%20Audio%20N8%20M15%20sample%203.png)