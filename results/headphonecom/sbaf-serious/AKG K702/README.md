# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.1; 37 -1.6; 41 -2.2; 45 -2.6; 49 -3.1; 54 -3.7; 60 -4.2; 66 -3.4; 72 -3.2; 79 -5.1; 87 -5.8; 96 -6.3; 106 -6.5; 116 -6.9; 128 -7.3; 141 -7.6; 155 -7.6; 170 -7.7; 187 -7.9; 206 -7.9; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.3; 442 -7.2; 486 -6.8; 535 -6.2; 588 -4.9; 647 -5.5; 712 -5.4; 783 -5.5; 861 -6.0; 947 -6.4; 1042 -6.4; 1146 -6.7; 1261 -7.0; 1387 -7.1; 1526 -7.7; 1678 -8.1; 1846 -9.3; 2031 -10.5; 2234 -10.9; 2457 -10.6; 2703 -9.6; 2973 -8.7; 3270 -7.4; 3597 -6.7; 3957 -7.2; 4353 -8.0; 4788 -7.6; 5267 -9.6; 5793 -13.4; 6373 -11.1; 7010 -9.3; 7711 -9.7; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -15.3
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.35 | 6.2 dB  |
| Peaking | 207 Hz  | 0.52 | -2.8 dB |
| Peaking | 1152 Hz | 0.22 | 1.7 dB  |
| Peaking | 2200 Hz | 1.54 | -5.8 dB |
| Peaking | 6005 Hz | 3.01 | -6.8 dB |
| Peaking | 70 Hz   | 8.72 | 1.2 dB  |
| Peaking | 1176 Hz | 2.02 | -1.1 dB |
| Peaking | 2095 Hz | 0.34 | 0.7 dB  |
| Peaking | 2615 Hz | 2.66 | -0.9 dB |
| Peaking | 7860 Hz | 7.57 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K702/AKG%20K702.png)