# Creative Aurvana Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.8; 25 -13.3; 28 -13.6; 31 -13.4; 34 -13.2; 37 -13.0; 41 -12.7; 45 -12.4; 49 -12.2; 54 -12.0; 60 -11.9; 66 -11.9; 72 -11.9; 79 -12.0; 87 -12.1; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.7; 141 -12.8; 155 -12.8; 170 -12.8; 187 -12.7; 206 -12.5; 227 -12.4; 249 -12.4; 274 -12.4; 302 -12.5; 332 -12.6; 365 -12.8; 402 -12.9; 442 -13.1; 486 -12.9; 535 -11.4; 588 -9.2; 647 -7.0; 712 -5.8; 783 -5.8; 861 -6.0; 947 -5.8; 1042 -7.0; 1146 -7.1; 1261 -6.3; 1387 -5.7; 1526 -4.7; 1678 -3.9; 1846 -3.2; 2031 -2.5; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.9; 5267 -6.7; 5793 -7.9; 6373 -5.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.13 | -6.3 dB |
| Peaking | 405 Hz  | 1.78 | -4.2 dB |
| Peaking | 2847 Hz | 0.91 | 6.1 dB  |
| Peaking | 4353 Hz | 3.48 | 3.0 dB  |
| Peaking | 5516 Hz | 5.73 | -4.7 dB |
| Peaking | 71 Hz   | 1.56 | 1.1 dB  |
| Peaking | 222 Hz  | 0.77 | -1.3 dB |
| Peaking | 520 Hz  | 2.74 | -4.9 dB |
| Peaking | 613 Hz  | 0.92 | 4.5 dB  |
| Peaking | 1153 Hz | 2.1  | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)