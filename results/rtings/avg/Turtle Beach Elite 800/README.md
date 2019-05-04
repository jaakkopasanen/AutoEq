# Turtle Beach Elite 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -6.9; 25 -6.8; 28 -6.7; 31 -6.6; 34 -6.6; 37 -6.7; 41 -6.8; 45 -6.9; 49 -7.1; 54 -7.4; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.6; 87 -8.8; 96 -8.8; 106 -8.8; 116 -8.7; 128 -8.6; 141 -8.5; 155 -8.3; 170 -8.1; 187 -7.8; 206 -7.4; 227 -6.9; 249 -6.4; 274 -5.9; 302 -5.1; 332 -4.0; 365 -2.0; 402 -0.5; 442 -0.5; 486 -0.6; 535 -1.8; 588 -2.6; 647 -3.3; 712 -3.8; 783 -4.1; 861 -4.3; 947 -4.7; 1042 -5.4; 1146 -6.0; 1261 -6.7; 1387 -7.5; 1526 -8.6; 1678 -10.3; 1846 -12.2; 2031 -11.9; 2234 -10.6; 2457 -9.6; 2703 -9.3; 2973 -10.7; 3270 -13.2; 3597 -13.3; 3957 -9.2; 4353 -5.3; 4788 -3.4; 5267 -3.3; 5793 -4.5; 6373 -1.2; 7010 -4.0; 7711 -7.9; 8482 -9.7; 9330 -8.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 476 Hz   | 1.74 | 6.5 dB  |
| Peaking | 1923 Hz  | 3.04 | -6.0 dB |
| Peaking | 3458 Hz  | 3.11 | -8.5 dB |
| Peaking | 5053 Hz  | 1.98 | 5.0 dB  |
| Peaking | 21028 Hz | 1.85 | -1.3 dB |
| Peaking | 93 Hz    | 1.13 | -2.3 dB |
| Peaking | 167 Hz   | 1.77 | -1.3 dB |
| Peaking | 888 Hz   | 2.76 | 1.4 dB  |
| Peaking | 6557 Hz  | 7.62 | 4.5 dB  |
| Peaking | 8487 Hz  | 3.55 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)