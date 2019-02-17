# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.2; 37 -3.5; 41 -3.9; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -5.5; 87 -5.8; 96 -6.2; 106 -6.1; 116 -6.5; 128 -7.2; 141 -7.7; 155 -7.8; 170 -7.5; 187 -7.7; 206 -7.7; 227 -7.6; 249 -7.6; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.5; 402 -6.1; 442 -5.5; 486 -5.2; 535 -3.6; 588 -2.6; 647 -2.3; 712 -1.8; 783 -1.7; 861 -2.2; 947 -2.6; 1042 -3.1; 1146 -3.6; 1261 -3.5; 1387 -4.1; 1526 -5.2; 1678 -6.4; 1846 -6.9; 2031 -8.2; 2234 -8.3; 2457 -7.5; 2703 -5.7; 2973 -4.1; 3270 -2.6; 3597 -2.8; 3957 -3.8; 4353 -6.1; 4788 -6.3; 5267 -5.4; 5793 -6.8; 6373 -8.9; 7010 -9.4; 7711 -9.5; 8482 -9.9; 9330 -7.0; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -5.6; 18182 -8.3; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 176 Hz   | 0.6  | -5.2 dB |
| Peaking | 2118 Hz  | 2.64 | -5.8 dB |
| Peaking | 6620 Hz  | 2.27 | -5.7 dB |
| Peaking | 8410 Hz  | 4.51 | -5.3 dB |
| Peaking | 18718 Hz | 1.34 | -6.3 dB |
| Peaking | 21 Hz    | 2.58 | 2.6 dB  |
| Peaking | 740 Hz   | 2.92 | 2.4 dB  |
| Peaking | 3484 Hz  | 3.22 | 5.0 dB  |
| Peaking | 3714 Hz  | 1.63 | -3.3 dB |
| Peaking | 11985 Hz | 1.4  | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702/AKG%20K702.png)