# AKG K167 Tiesto
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.3; 31 -1.7; 34 -2.0; 37 -2.1; 41 -2.2; 45 -2.2; 49 -2.1; 54 -1.9; 60 -1.4; 66 -0.7; 72 -0.5; 79 -1.1; 87 -1.7; 96 -1.8; 106 -1.9; 116 -2.0; 128 -2.3; 141 -2.3; 155 -2.1; 170 -1.6; 187 -2.6; 206 -2.7; 227 -2.4; 249 -2.5; 274 -2.4; 302 -3.0; 332 -3.5; 365 -3.9; 402 -4.2; 442 -4.3; 486 -4.7; 535 -4.9; 588 -4.9; 647 -5.1; 712 -5.5; 783 -5.6; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.3; 1261 -7.3; 1387 -7.9; 1526 -8.8; 1678 -9.7; 1846 -9.7; 2031 -8.1; 2234 -5.9; 2457 -4.9; 2703 -4.0; 2973 -2.9; 3270 -2.8; 3597 -3.2; 3957 -3.4; 4353 -3.5; 4788 -1.9; 5267 -0.5; 5793 -2.5; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -7.6; 9330 -9.3; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K167 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K167 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.12 | 4.4 dB  |
| Peaking | 73 Hz   | 0.71 | 4.5 dB  |
| Peaking | 242 Hz  | 0.82 | 3.3 dB  |
| Peaking | 4923 Hz | 1.76 | 5.3 dB  |
| Peaking | 13 Hz   | 0.75 | 0.9 dB  |
| Peaking | 1783 Hz | 1.61 | -6.9 dB |
| Peaking | 2630 Hz | 0.69 | 4.5 dB  |
| Peaking | 4314 Hz | 3.64 | -3.7 dB |
| Peaking | 9156 Hz | 3.77 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | 3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K167%20Tiesto/AKG%20K167%20Tiesto.png)