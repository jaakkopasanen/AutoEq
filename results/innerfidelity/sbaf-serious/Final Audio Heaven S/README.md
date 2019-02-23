# Final Audio Heaven S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.7; 25 -1.8; 28 -2.0; 31 -2.1; 34 -2.3; 37 -2.4; 41 -2.6; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.6; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.1; 96 -5.6; 106 -5.9; 116 -6.1; 128 -6.3; 141 -6.6; 155 -6.9; 170 -6.9; 187 -7.0; 206 -7.0; 227 -6.9; 249 -6.9; 274 -6.7; 302 -6.6; 332 -6.4; 365 -6.3; 402 -6.0; 442 -5.5; 486 -5.4; 535 -5.0; 588 -4.5; 647 -4.2; 712 -4.1; 783 -3.7; 861 -3.8; 947 -4.0; 1042 -4.2; 1146 -4.4; 1261 -4.7; 1387 -5.1; 1526 -5.6; 1678 -5.9; 1846 -5.8; 2031 -5.7; 2234 -6.0; 2457 -6.1; 2703 -6.5; 2973 -5.6; 3270 -3.4; 3597 -1.0; 3957 -0.5; 4353 -1.8; 4788 -2.4; 5267 -3.0; 5793 -5.5; 6373 -10.8; 7010 -9.8; 7711 -8.7; 8482 -8.8; 9330 -6.2; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.38 | 4.0 dB  |
| Peaking | 46 Hz   | 2.21 | 2.1 dB  |
| Peaking | 824 Hz  | 2.49 | 2.0 dB  |
| Peaking | 4299 Hz | 2.19 | 5.6 dB  |
| Peaking | 6875 Hz | 2.63 | -6.0 dB |
| Peaking | 209 Hz  | 0.64 | -2.7 dB |
| Peaking | 478 Hz  | 0.09 | 1.1 dB  |
| Peaking | 2414 Hz | 0.77 | -1.8 dB |
| Peaking | 2815 Hz | 5.38 | -1.3 dB |
| Peaking | 3581 Hz | 6.45 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20S/Final%20Audio%20Heaven%20S.png)