# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.0; 49 -1.3; 54 -1.6; 60 -2.0; 66 -2.5; 72 -2.9; 79 -3.4; 87 -3.8; 96 -4.3; 106 -4.7; 116 -5.2; 128 -5.6; 141 -5.9; 155 -6.1; 170 -6.2; 187 -6.2; 206 -6.2; 227 -6.1; 249 -6.1; 274 -6.1; 302 -6.1; 332 -6.0; 365 -5.9; 402 -5.8; 442 -5.8; 486 -5.6; 535 -5.3; 588 -4.8; 647 -4.2; 712 -4.1; 783 -3.7; 861 -3.5; 947 -3.5; 1042 -3.5; 1146 -3.5; 1261 -3.7; 1387 -4.3; 1526 -5.2; 1678 -6.6; 1846 -8.4; 2031 -10.2; 2234 -11.2; 2457 -10.6; 2703 -9.7; 2973 -8.3; 3270 -7.2; 3597 -7.0; 3957 -7.2; 4353 -6.7; 4788 -6.1; 5267 -6.9; 5793 -8.5; 6373 -10.9; 7010 -10.5; 7711 -10.6; 8482 -10.6; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -13.1; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.56 | 6.5 dB  |
| Peaking | 1102 Hz  | 0.85 | 3.7 dB  |
| Peaking | 2223 Hz  | 2.23 | -6.2 dB |
| Peaking | 7275 Hz  | 2.55 | -4.8 dB |
| Peaking | 19015 Hz | 1.44 | -8.2 dB |
| Peaking | 74 Hz    | 1.55 | 0.6 dB  |
| Peaking | 157 Hz   | 1.27 | -0.6 dB |
| Peaking | 4740 Hz  | 4.6  | 1.6 dB  |
| Peaking | 13703 Hz | 0.3  | -2.1 dB |
| Peaking | 13942 Hz | 0.64 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K702/AKG%20K702.png)