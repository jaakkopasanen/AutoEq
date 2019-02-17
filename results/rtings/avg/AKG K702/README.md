# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.7; 31 -2.3; 34 -2.7; 37 -3.1; 41 -3.6; 45 -4.0; 49 -4.3; 54 -4.6; 60 -5.0; 66 -5.5; 72 -5.9; 79 -6.4; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.1; 249 -9.1; 274 -9.1; 302 -9.1; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.8; 486 -8.6; 535 -8.3; 588 -7.8; 647 -7.2; 712 -7.1; 783 -6.7; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.7; 1387 -7.4; 1526 -8.2; 1678 -9.6; 1846 -11.4; 2031 -13.2; 2234 -14.2; 2457 -13.6; 2703 -12.7; 2973 -11.3; 3270 -10.2; 3597 -10.0; 3957 -10.2; 4353 -9.7; 4788 -9.1; 5267 -9.9; 5793 -11.5; 6373 -13.9; 7010 -13.5; 7711 -13.6; 8482 -13.6; 9330 -9.7; 10263 -6.5; 11289 -7.3; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -9.9; 18182 -16.1; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 14 Hz    |  0.37 | 6.7 dB   |
| Peaking | 203 Hz   |  0.58 | -3.2 dB  |
| Peaking | 2351 Hz  |  1.92 | -7.6 dB  |
| Peaking | 7106 Hz  |  1.78 | -7.6 dB  |
| Peaking | 19003 Hz |  1.29 | -11.6 dB |
| Peaking | 1038 Hz  |  0.58 | -2.4 dB  |
| Peaking | 1052 Hz  |  1    | 3.7 dB   |
| Peaking | 8495 Hz  | 12    | -2.6 dB  |
| Peaking | 14656 Hz |  2.34 | 2.1 dB   |
| Peaking | 22049 Hz |  1.67 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K702/AKG%20K702.png)