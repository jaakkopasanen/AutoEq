# V-Moda XS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.0; 28 -7.5; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.7; 49 -8.8; 54 -8.9; 60 -8.9; 66 -9.0; 72 -9.1; 79 -9.1; 87 -9.2; 96 -9.3; 106 -9.1; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.0; 170 -8.5; 187 -8.3; 206 -7.7; 227 -7.4; 249 -7.9; 274 -6.8; 302 -5.6; 332 -4.5; 365 -3.3; 402 -3.1; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.5; 647 -1.5; 712 -1.9; 783 -2.0; 861 -2.8; 947 -3.6; 1042 -4.4; 1146 -4.9; 1261 -5.2; 1387 -5.2; 1526 -5.1; 1678 -4.9; 1846 -4.5; 2031 -4.8; 2234 -4.5; 2457 -4.7; 2703 -5.7; 2973 -6.4; 3270 -6.0; 3597 -4.0; 3957 -0.9; 4353 -0.6; 4788 -3.3; 5267 -0.5; 5793 -1.8; 6373 -1.3; 7010 -2.3; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda XS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 187 Hz  | 0.14 | -5.5 dB |
| Peaking | 546 Hz  | 0.74 | 7.9 dB  |
| Peaking | 3129 Hz | 3.8  | -2.4 dB |
| Peaking | 4086 Hz | 5    | 4.4 dB  |
| Peaking | 5861 Hz | 2.66 | 3.5 dB  |
| Peaking | 253 Hz  | 8.34 | -0.8 dB |
| Peaking | 361 Hz  | 4.19 | 1.2 dB  |
| Peaking | 802 Hz  | 1.83 | 2.0 dB  |
| Peaking | 926 Hz  | 0.64 | -1.6 dB |
| Peaking | 1966 Hz | 1.83 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)