# Turtle Beach Elite Atlas
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.8; 28 -5.9; 31 -5.9; 34 -5.9; 37 -5.7; 41 -5.6; 45 -5.5; 49 -5.5; 54 -5.6; 60 -5.8; 66 -5.9; 72 -5.9; 79 -6.0; 87 -6.0; 96 -6.0; 106 -6.1; 116 -6.6; 128 -7.5; 141 -8.6; 155 -9.6; 170 -10.1; 187 -10.1; 206 -9.7; 227 -8.6; 249 -7.1; 274 -5.4; 302 -4.4; 332 -2.9; 365 -1.1; 402 -0.8; 442 -0.8; 486 -2.2; 535 -4.7; 588 -6.1; 647 -5.8; 712 -3.6; 783 -1.9; 861 -2.1; 947 -3.0; 1042 -4.6; 1146 -5.8; 1261 -7.0; 1387 -6.8; 1526 -5.9; 1678 -5.3; 1846 -5.2; 2031 -5.7; 2234 -5.8; 2457 -5.0; 2703 -4.5; 2973 -4.9; 3270 -4.9; 3597 -5.4; 3957 -6.1; 4353 -5.7; 4788 -3.3; 5267 -0.5; 5793 -0.5; 6373 -1.8; 7010 -4.0; 7711 -8.5; 8482 -11.2; 9330 -8.4; 10263 -5.3; 11289 -5.4; 12418 -6.6; 13660 -5.8; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Atlas GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Atlas ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 185 Hz  | 1.4  | -6.6 dB |
| Peaking | 301 Hz  | 0.53 | 1.7 dB  |
| Peaking | 394 Hz  | 2.89 | 4.6 dB  |
| Peaking | 5793 Hz | 3.24 | 5.9 dB  |
| Peaking | 8435 Hz | 4.39 | -7.1 dB |
| Peaking | 622 Hz  | 4    | -4.2 dB |
| Peaking | 812 Hz  | 1.79 | 3.8 dB  |
| Peaking | 1261 Hz | 2.8  | -3.0 dB |
| Peaking | 4295 Hz | 5.74 | -2.5 dB |
| Peaking | 4475 Hz | 1.69 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Atlas/Turtle%20Beach%20Elite%20Atlas.png)