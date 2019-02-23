# Final Audio Heaven A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.3; 31 -1.7; 34 -2.0; 37 -2.3; 41 -2.7; 45 -3.0; 49 -3.4; 54 -3.7; 60 -4.2; 66 -4.6; 72 -5.0; 79 -5.5; 87 -5.9; 96 -6.5; 106 -6.7; 116 -7.0; 128 -7.4; 141 -7.7; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.1; 227 -8.1; 249 -8.0; 274 -7.9; 302 -7.7; 332 -7.5; 365 -7.3; 402 -7.0; 442 -6.5; 486 -6.3; 535 -6.0; 588 -5.4; 647 -5.2; 712 -5.1; 783 -4.7; 861 -4.8; 947 -5.0; 1042 -5.3; 1146 -5.5; 1261 -5.7; 1387 -6.2; 1526 -6.7; 1678 -7.1; 1846 -7.4; 2031 -7.5; 2234 -7.7; 2457 -7.9; 2703 -7.9; 2973 -6.7; 3270 -4.3; 3597 -1.8; 3957 -1.3; 4353 -2.5; 4788 -3.2; 5267 -3.7; 5793 -6.4; 6373 -11.0; 7010 -9.0; 7711 -7.3; 8482 -8.7; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.41 | 6.0 dB  |
| Peaking | 45 Hz   | 2.01 | 2.6 dB  |
| Peaking | 823 Hz  | 2.73 | 2.0 dB  |
| Peaking | 4124 Hz | 2.89 | 5.6 dB  |
| Peaking | 6537 Hz | 5.43 | -5.3 dB |
| Peaking | 204 Hz  | 1.21 | -2.0 dB |
| Peaking | 2661 Hz | 1.74 | -2.4 dB |
| Peaking | 3480 Hz | 6    | 2.8 dB  |
| Peaking | 5266 Hz | 7.42 | 2.3 dB  |
| Peaking | 8660 Hz | 7.75 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20A/Final%20Audio%20Heaven%20A.png)