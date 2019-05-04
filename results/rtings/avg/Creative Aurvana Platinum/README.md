# Creative Aurvana Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.4; 25 -4.4; 28 -5.7; 31 -6.7; 34 -7.4; 37 -8.0; 41 -8.6; 45 -9.0; 49 -9.3; 54 -9.6; 60 -10.0; 66 -10.4; 72 -10.8; 79 -11.2; 87 -11.7; 96 -12.2; 106 -12.6; 116 -13.0; 128 -13.3; 141 -13.6; 155 -13.8; 170 -13.9; 187 -13.9; 206 -13.7; 227 -13.6; 249 -13.5; 274 -13.4; 302 -13.2; 332 -13.1; 365 -13.0; 402 -13.0; 442 -13.0; 486 -12.6; 535 -11.0; 588 -8.7; 647 -6.0; 712 -4.3; 783 -3.9; 861 -3.0; 947 -0.7; 1042 -1.0; 1146 -2.5; 1261 -4.2; 1387 -4.7; 1526 -3.7; 1678 -2.2; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.9; 3957 -4.0; 4353 -3.4; 4788 -2.8; 5267 -3.5; 5793 -4.4; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -7.8; 12418 -7.3; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.01 | 5.4 dB  |
| Peaking | 192 Hz   | 0.32 | -7.5 dB |
| Peaking | 466 Hz   | 2.91 | -2.9 dB |
| Peaking | 873 Hz   | 1.56 | 6.4 dB  |
| Peaking | 2635 Hz  | 0.81 | 6.3 dB  |
| Peaking | 1391 Hz  | 3.56 | -4.4 dB |
| Peaking | 1422 Hz  | 1.68 | 2.5 dB  |
| Peaking | 3949 Hz  | 9.92 | -1.9 dB |
| Peaking | 6531 Hz  | 8.33 | 3.5 dB  |
| Peaking | 11279 Hz | 1.85 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)