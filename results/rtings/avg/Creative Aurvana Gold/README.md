# Creative Aurvana Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -12.3; 25 -12.8; 28 -13.1; 31 -13.0; 34 -12.7; 37 -12.5; 41 -12.2; 45 -11.9; 49 -11.7; 54 -11.6; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.5; 87 -11.6; 96 -11.7; 106 -11.9; 116 -12.1; 128 -12.2; 141 -12.3; 155 -12.3; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.9; 249 -11.9; 274 -11.9; 302 -12.0; 332 -12.1; 365 -12.3; 402 -12.5; 442 -12.6; 486 -12.4; 535 -10.9; 588 -8.7; 647 -6.5; 712 -5.3; 783 -5.3; 861 -5.5; 947 -5.3; 1042 -6.5; 1146 -6.7; 1261 -5.9; 1387 -5.3; 1526 -4.3; 1678 -3.4; 1846 -2.7; 2031 -2.0; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -6.2; 5793 -7.4; 6373 -4.8; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.06 | -5.5 dB |
| Peaking | 525 Hz  | 1.28 | -4.6 dB |
| Peaking | 654 Hz  | 2.25 | 5.1 dB  |
| Peaking | 816 Hz  | 2.33 | 2.3 dB  |
| Peaking | 2840 Hz | 0.93 | 7.1 dB  |
| Peaking | 31 Hz   | 2.91 | -1.1 dB |
| Peaking | 3088 Hz | 2.25 | -2.3 dB |
| Peaking | 5450 Hz | 1.03 | 5.7 dB  |
| Peaking | 5568 Hz | 3.92 | -8.3 dB |
| Peaking | 8331 Hz | 1.4  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)