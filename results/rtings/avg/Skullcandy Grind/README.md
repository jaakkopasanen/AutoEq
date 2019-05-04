# Skullcandy Grind
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.7; 25 -5.1; 28 -5.6; 31 -6.0; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.4; 87 -7.5; 96 -7.6; 106 -7.6; 116 -7.6; 128 -7.6; 141 -7.6; 155 -7.5; 170 -7.5; 187 -7.4; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.4; 302 -7.5; 332 -7.0; 365 -6.5; 402 -5.8; 442 -5.3; 486 -4.8; 535 -4.2; 588 -3.4; 647 -2.5; 712 -1.3; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -2.9; 1146 -5.0; 1261 -4.4; 1387 -6.0; 1526 -6.7; 1678 -6.9; 1846 -9.4; 2031 -11.5; 2234 -12.1; 2457 -11.4; 2703 -9.9; 2973 -8.4; 3270 -7.0; 3597 -6.2; 3957 -7.4; 4353 -5.7; 4788 -4.2; 5267 -2.4; 5793 -2.7; 6373 -5.9; 7010 -10.0; 7711 -12.6; 8482 -12.4; 9330 -9.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.87 | 2.5 dB  |
| Peaking | 826 Hz   | 1.76 | 6.7 dB  |
| Peaking | 2242 Hz  | 2.48 | -6.4 dB |
| Peaking | 5522 Hz  | 3.13 | 5.9 dB  |
| Peaking | 7897 Hz  | 3.01 | -7.6 dB |
| Peaking | 18 Hz    | 0.59 | 0.6 dB  |
| Peaking | 115 Hz   | 0.45 | -1.2 dB |
| Peaking | 302 Hz   | 2.9  | -0.9 dB |
| Peaking | 514 Hz   | 1.86 | 0.8 dB  |
| Peaking | 10544 Hz | 6.07 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Grind/Skullcandy%20Grind.png)