# Creative Aurvana Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.7; 25 -4.7; 28 -5.9; 31 -6.9; 34 -7.6; 37 -8.2; 41 -8.7; 45 -9.2; 49 -9.5; 54 -9.8; 60 -10.2; 66 -10.6; 72 -11.0; 79 -11.4; 87 -11.9; 96 -12.4; 106 -12.8; 116 -13.2; 128 -13.5; 141 -13.8; 155 -14.0; 170 -14.1; 187 -14.1; 206 -13.9; 227 -13.7; 249 -13.5; 274 -13.4; 302 -13.3; 332 -13.1; 365 -13.1; 402 -13.1; 442 -13.0; 486 -12.5; 535 -11.0; 588 -8.6; 647 -5.9; 712 -4.1; 783 -3.7; 861 -3.0; 947 -0.6; 1042 -0.8; 1146 -2.4; 1261 -4.0; 1387 -4.5; 1526 -3.5; 1678 -2.0; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.0; 3957 -4.3; 4353 -3.8; 4788 -2.4; 5267 -3.0; 5793 -4.5; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -8.0; 10263 -7.0; 11289 -6.8; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.02 | 5.2 dB  |
| Peaking | 186 Hz  | 0.34 | -7.6 dB |
| Peaking | 465 Hz  | 2.69 | -3.1 dB |
| Peaking | 873 Hz  | 1.52 | 6.4 dB  |
| Peaking | 2600 Hz | 0.84 | 6.3 dB  |
| Peaking | 1382 Hz | 1.83 | 2.3 dB  |
| Peaking | 1392 Hz | 3.82 | -4.3 dB |
| Peaking | 4006 Hz | 7.99 | -2.4 dB |
| Peaking | 6969 Hz | 1.52 | 3.7 dB  |
| Peaking | 8441 Hz | 1.57 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)