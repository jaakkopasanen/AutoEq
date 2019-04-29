# 64 Audio N8 custom sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.4; 28 -4.0; 31 -4.4; 34 -4.8; 37 -5.1; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.3; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.1; 96 -8.3; 106 -8.5; 116 -8.9; 128 -9.1; 141 -9.3; 155 -9.4; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.6; 249 -9.5; 274 -9.4; 302 -9.3; 332 -9.2; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.5; 535 -8.2; 588 -7.9; 647 -7.5; 712 -7.1; 783 -6.7; 861 -6.3; 947 -6.1; 1042 -6.2; 1146 -6.9; 1261 -7.8; 1387 -8.5; 1526 -8.8; 1678 -8.7; 1846 -8.3; 2031 -7.8; 2234 -7.1; 2457 -6.0; 2703 -4.8; 2973 -3.7; 3270 -2.9; 3597 -2.7; 3957 -3.0; 4353 -3.2; 4788 -4.0; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -10.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.66 | 5.1 dB  |
| Peaking | 198 Hz   | 0.5  | -3.4 dB |
| Peaking | 1715 Hz  | 2.28 | -2.8 dB |
| Peaking | 3454 Hz  | 1.96 | 3.8 dB  |
| Peaking | 5877 Hz  | 3.45 | 6.1 dB  |
| Peaking | 502 Hz   | 1.95 | -0.5 dB |
| Peaking | 949 Hz   | 2.08 | 1.3 dB  |
| Peaking | 1348 Hz  | 4.72 | -1.0 dB |
| Peaking | 8141 Hz  | 5.28 | -1.0 dB |
| Peaking | 18493 Hz | 1.96 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20custom%20sample%203/64%20Audio%20N8%20custom%20sample%203.png)