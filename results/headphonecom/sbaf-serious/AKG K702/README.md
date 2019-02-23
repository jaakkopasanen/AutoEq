# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.4; 49 -1.8; 54 -2.4; 60 -2.9; 66 -2.1; 72 -2.0; 79 -3.8; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.6; 128 -6.1; 141 -6.3; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.7; 227 -6.7; 249 -6.6; 274 -6.6; 302 -6.5; 332 -6.3; 365 -6.1; 402 -6.0; 442 -5.9; 486 -5.6; 535 -4.9; 588 -3.6; 647 -4.2; 712 -4.1; 783 -4.2; 861 -4.7; 947 -5.1; 1042 -5.2; 1146 -5.4; 1261 -5.7; 1387 -5.8; 1526 -6.4; 1678 -6.9; 1846 -8.0; 2031 -9.2; 2234 -9.6; 2457 -9.4; 2703 -8.3; 2973 -7.4; 3270 -6.2; 3597 -5.4; 3957 -5.9; 4353 -6.7; 4788 -6.4; 5267 -8.3; 5793 -12.1; 6373 -9.8; 7010 -8.0; 7711 -8.4; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.62 | 6.5 dB  |
| Peaking | 670 Hz  | 2.05 | 2.4 dB  |
| Peaking | 2278 Hz | 1.63 | -7.2 dB |
| Peaking | 2425 Hz | 0.69 | 3.8 dB  |
| Peaking | 5929 Hz | 4.09 | -6.4 dB |
| Peaking | 66 Hz   | 1.83 | -0.5 dB |
| Peaking | 70 Hz   | 5.81 | 2.7 dB  |
| Peaking | 190 Hz  | 1.09 | -0.7 dB |
| Peaking | 6820 Hz | 4.29 | 1.0 dB  |
| Peaking | 7563 Hz | 5.88 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K702/AKG%20K702.png)