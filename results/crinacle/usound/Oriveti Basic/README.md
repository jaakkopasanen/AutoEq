# Oriveti Basic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.3; 25 -12.4; 28 -12.5; 31 -12.5; 34 -12.5; 37 -12.6; 41 -12.6; 45 -12.6; 49 -12.6; 54 -12.7; 60 -12.7; 66 -12.8; 72 -12.9; 79 -13.1; 87 -13.2; 96 -13.4; 106 -13.4; 116 -13.5; 128 -13.5; 141 -13.4; 155 -13.3; 170 -13.1; 187 -12.8; 206 -12.6; 227 -12.2; 249 -11.8; 274 -11.6; 302 -11.2; 332 -10.8; 365 -10.4; 402 -9.9; 442 -9.6; 486 -9.3; 535 -8.9; 588 -8.5; 647 -8.1; 712 -7.6; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.6; 1146 -6.8; 1261 -6.8; 1387 -6.3; 1526 -5.5; 1678 -4.2; 1846 -2.8; 2031 -1.4; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -3.4; 4353 -4.2; 4788 -4.5; 5267 -4.3; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -6.9; 18182 -10.3; 20000 -13.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriveti Basic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriveti Basic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.55 | -4.2 dB |
| Peaking | 137 Hz   | 0.34 | -6.5 dB |
| Peaking | 2667 Hz  | 1.29 | 6.9 dB  |
| Peaking | 6219 Hz  | 5.55 | 5.3 dB  |
| Peaking | 1428 Hz  | 1.98 | -2.6 dB |
| Peaking | 2086 Hz  | 0.75 | 2.2 dB  |
| Peaking | 2610 Hz  | 3.77 | -2.5 dB |
| Peaking | 4581 Hz  | 2.87 | -1.0 dB |
| Peaking | 19739 Hz | 1.09 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriveti%20Basic/Oriveti%20Basic.png)