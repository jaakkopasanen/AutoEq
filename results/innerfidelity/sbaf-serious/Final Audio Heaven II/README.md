# Final Audio Heaven II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.3; 25 -1.4; 28 -1.6; 31 -1.8; 34 -1.9; 37 -2.1; 41 -2.2; 45 -2.4; 49 -2.7; 54 -3.0; 60 -3.2; 66 -3.6; 72 -4.0; 79 -4.4; 87 -4.9; 96 -5.3; 106 -5.6; 116 -5.8; 128 -6.2; 141 -6.5; 155 -6.8; 170 -7.0; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.3; 274 -7.2; 302 -7.2; 332 -7.1; 365 -7.0; 402 -6.9; 442 -6.6; 486 -6.5; 535 -6.3; 588 -5.9; 647 -5.7; 712 -5.8; 783 -5.6; 861 -5.8; 947 -6.1; 1042 -6.4; 1146 -6.8; 1261 -7.3; 1387 -7.9; 1526 -8.5; 1678 -9.0; 1846 -9.1; 2031 -9.2; 2234 -9.6; 2457 -9.6; 2703 -9.2; 2973 -6.8; 3270 -3.5; 3597 -1.1; 3957 -0.5; 4353 -1.6; 4788 -1.8; 5267 -1.1; 5793 -1.7; 6373 -4.2; 7010 -5.5; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.93 | 5.0 dB  |
| Peaking | 54 Hz   | 1.55 | 2.4 dB  |
| Peaking | 2520 Hz | 1.25 | -5.4 dB |
| Peaking | 3705 Hz | 2.21 | 8.0 dB  |
| Peaking | 5425 Hz | 3.36 | 4.5 dB  |
| Peaking | 93 Hz   | 1.37 | 0.7 dB  |
| Peaking | 242 Hz  | 0.54 | -1.2 dB |
| Peaking | 745 Hz  | 1.09 | 1.4 dB  |
| Peaking | 1546 Hz | 3.56 | -1.0 dB |
| Peaking | 8388 Hz | 3.06 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20II/Final%20Audio%20Heaven%20II.png)