# Turtle Beach Elite Atlas
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.3; 25 -6.4; 28 -6.5; 31 -6.6; 34 -6.5; 37 -6.4; 41 -6.2; 45 -6.1; 49 -6.2; 54 -6.3; 60 -6.4; 66 -6.5; 72 -6.6; 79 -6.6; 87 -6.7; 96 -6.8; 106 -6.8; 116 -7.3; 128 -8.1; 141 -9.3; 155 -10.3; 170 -10.8; 187 -10.7; 206 -10.3; 227 -9.0; 249 -7.6; 274 -5.9; 302 -4.9; 332 -3.6; 365 -1.9; 402 -1.3; 442 -1.3; 486 -2.6; 535 -5.1; 588 -6.5; 647 -6.2; 712 -4.1; 783 -2.2; 861 -2.5; 947 -3.3; 1042 -4.9; 1146 -6.1; 1261 -7.4; 1387 -7.1; 1526 -6.2; 1678 -5.5; 1846 -5.4; 2031 -5.6; 2234 -5.3; 2457 -4.5; 2703 -4.3; 2973 -5.3; 3270 -5.5; 3597 -6.0; 3957 -6.9; 4353 -6.5; 4788 -3.3; 5267 -0.5; 5793 -1.0; 6373 -3.3; 7010 -4.4; 7711 -8.2; 8482 -12.1; 9330 -10.6; 10263 -6.0; 11289 -5.8; 12418 -6.8; 13660 -7.0; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Atlas GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Atlas ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 179 Hz   | 1.59 | -5.5 dB |
| Peaking | 396 Hz   | 2.64 | 5.7 dB  |
| Peaking | 831 Hz   | 5.25 | 3.9 dB  |
| Peaking | 5598 Hz  | 3.79 | 6.1 dB  |
| Peaking | 8666 Hz  | 4.67 | -7.6 dB |
| Peaking | 604 Hz   | 5.72 | -2.7 dB |
| Peaking | 1320 Hz  | 3.38 | -2.8 dB |
| Peaking | 1816 Hz  | 0.28 | 1.0 dB  |
| Peaking | 4107 Hz  | 4.71 | -3.0 dB |
| Peaking | 13147 Hz | 6.54 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Atlas/Turtle%20Beach%20Elite%20Atlas.png)