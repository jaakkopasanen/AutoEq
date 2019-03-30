# Creative Aurvana Live! 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.4; 28 -5.6; 31 -5.5; 34 -5.5; 37 -5.5; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.7; 60 -7.3; 66 -7.7; 72 -8.0; 79 -8.4; 87 -8.7; 96 -8.9; 106 -9.0; 116 -9.1; 128 -9.3; 141 -9.2; 155 -9.0; 170 -8.7; 187 -8.3; 206 -7.8; 227 -7.2; 249 -6.4; 274 -5.7; 302 -5.1; 332 -4.7; 365 -4.4; 402 -4.0; 442 -3.7; 486 -3.9; 535 -4.5; 588 -5.3; 647 -5.9; 712 -6.3; 783 -6.4; 861 -6.3; 947 -6.0; 1042 -5.4; 1146 -4.5; 1261 -3.4; 1387 -2.2; 1526 -1.2; 1678 -0.7; 1846 -0.5; 2031 -0.6; 2234 -0.9; 2457 -1.5; 2703 -2.1; 2973 -1.5; 3270 -0.7; 3597 -1.1; 3957 -3.0; 4353 -4.6; 4788 -4.5; 5267 -2.6; 5793 -1.2; 6373 -1.6; 7010 -2.6; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -5.1; 13660 -5.6; 15026 -6.0; 16529 -5.2; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Live! 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Live! 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 94 Hz    | 0.8  | -4.0 dB |
| Peaking | 167 Hz   | 1.63 | -2.5 dB |
| Peaking | 1892 Hz  | 2.22 | 4.3 dB  |
| Peaking | 3289 Hz  | 3.76 | 3.3 dB  |
| Peaking | 6077 Hz  | 4.41 | 3.4 dB  |
| Peaking | 444 Hz   | 2.1  | 1.8 dB  |
| Peaking | 798 Hz   | 1.35 | -2.5 dB |
| Peaking | 1432 Hz  | 3.62 | 1.6 dB  |
| Peaking | 4511 Hz  | 8.99 | -1.5 dB |
| Peaking | 14814 Hz | 1.97 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20Aurvana%20Live!%202/Creative%20Aurvana%20Live!%202.png)