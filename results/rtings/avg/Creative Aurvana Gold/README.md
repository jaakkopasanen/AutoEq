# Creative Aurvana Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -12.0; 25 -12.4; 28 -12.8; 31 -12.8; 34 -12.6; 37 -12.4; 41 -12.0; 45 -11.8; 49 -11.6; 54 -11.4; 60 -11.3; 66 -11.2; 72 -11.2; 79 -11.2; 87 -11.4; 96 -11.5; 106 -11.7; 116 -11.9; 128 -12.0; 141 -12.1; 155 -12.1; 170 -12.1; 187 -12.1; 206 -11.9; 227 -11.9; 249 -11.8; 274 -11.9; 302 -12.0; 332 -12.1; 365 -12.2; 402 -12.4; 442 -12.6; 486 -12.4; 535 -11.0; 588 -8.8; 647 -6.6; 712 -5.4; 783 -5.5; 861 -5.5; 947 -5.5; 1042 -6.7; 1146 -6.8; 1261 -6.1; 1387 -5.4; 1526 -4.5; 1678 -3.6; 1846 -3.0; 2031 -2.5; 2234 -1.8; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.8; 5267 -6.8; 5793 -7.2; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.06 | -5.3 dB |
| Peaking | 504 Hz  | 1.34 | -4.7 dB |
| Peaking | 693 Hz  | 1.66 | 6.1 dB  |
| Peaking | 2630 Hz | 1.13 | 6.2 dB  |
| Peaking | 4113 Hz | 3.99 | 3.9 dB  |
| Peaking | 31 Hz   | 2.51 | -1.1 dB |
| Peaking | 67 Hz   | 2.23 | 0.8 dB  |
| Peaking | 4625 Hz | 7.47 | 2.6 dB  |
| Peaking | 5510 Hz | 3.44 | -3.6 dB |
| Peaking | 6570 Hz | 6.69 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)