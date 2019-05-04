# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.8; 49 -1.2; 54 -1.6; 60 -2.0; 66 -2.4; 72 -2.7; 79 -3.1; 87 -3.5; 96 -4.0; 106 -4.4; 116 -4.9; 128 -5.3; 141 -5.6; 155 -5.8; 170 -6.0; 187 -6.0; 206 -6.0; 227 -6.0; 249 -6.0; 274 -6.0; 302 -6.0; 332 -6.0; 365 -5.8; 402 -5.8; 442 -5.7; 486 -5.7; 535 -5.3; 588 -4.7; 647 -4.4; 712 -4.2; 783 -3.9; 861 -3.6; 947 -3.6; 1042 -3.6; 1146 -3.7; 1261 -3.9; 1387 -4.5; 1526 -5.5; 1678 -6.9; 1846 -8.8; 2031 -10.7; 2234 -12.0; 2457 -11.6; 2703 -10.3; 2973 -8.4; 3270 -7.0; 3597 -6.8; 3957 -6.9; 4353 -6.3; 4788 -6.5; 5267 -7.3; 5793 -8.5; 6373 -9.9; 7010 -10.6; 7711 -11.5; 8482 -10.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -12.9; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 6.4 dB  |
| Peaking | 1075 Hz  | 0.86 | 3.5 dB  |
| Peaking | 2244 Hz  | 2.41 | -7.0 dB |
| Peaking | 7430 Hz  | 3.07 | -5.2 dB |
| Peaking | 19020 Hz | 1.44 | -8.0 dB |
| Peaking | 170 Hz   | 2.36 | -0.5 dB |
| Peaking | 2699 Hz  | 7.45 | -1.0 dB |
| Peaking | 4225 Hz  | 1.43 | 0.7 dB  |
| Peaking | 6109 Hz  | 5.22 | -1.5 dB |
| Peaking | 13358 Hz | 1    | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K702/AKG%20K702.png)