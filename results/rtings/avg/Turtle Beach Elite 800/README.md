# Turtle Beach Elite 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.1; 25 -7.0; 28 -6.9; 31 -6.8; 34 -6.8; 37 -6.9; 41 -6.9; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.3; 72 -8.6; 79 -8.8; 87 -9.0; 96 -9.1; 106 -9.0; 116 -9.0; 128 -8.8; 141 -8.7; 155 -8.6; 170 -8.3; 187 -8.0; 206 -7.5; 227 -7.0; 249 -6.5; 274 -6.0; 302 -5.2; 332 -4.0; 365 -2.1; 402 -0.5; 442 -0.5; 486 -0.6; 535 -1.7; 588 -2.5; 647 -3.2; 712 -3.7; 783 -4.0; 861 -4.2; 947 -4.6; 1042 -5.2; 1146 -5.8; 1261 -6.5; 1387 -7.4; 1526 -8.4; 1678 -10.1; 1846 -11.9; 2031 -11.4; 2234 -9.8; 2457 -8.7; 2703 -8.8; 2973 -10.6; 3270 -13.4; 3597 -13.7; 3957 -9.5; 4353 -5.7; 4788 -3.2; 5267 -2.5; 5793 -4.9; 6373 -1.4; 7010 -4.0; 7711 -6.9; 8482 -10.0; 9330 -10.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 456 Hz   | 2.24 | 6.2 dB   |
| Peaking | 1916 Hz  | 1.63 | -10.5 dB |
| Peaking | 3451 Hz  | 2.25 | -15.8 dB |
| Peaking | 3490 Hz  | 0.44 | 10.0 dB  |
| Peaking | 8926 Hz  | 2.52 | -8.1 dB  |
| Peaking | 15 Hz    | 1.58 | -1.0 dB  |
| Peaking | 86 Hz    | 1.26 | -1.7 dB  |
| Peaking | 173 Hz   | 0.74 | -2.5 dB  |
| Peaking | 316 Hz   | 0.69 | 1.4 dB   |
| Peaking | 14078 Hz | 1.89 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)