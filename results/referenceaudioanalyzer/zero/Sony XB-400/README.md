# Sony XB-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -13.0; 25 -13.9; 28 -15.0; 31 -15.8; 34 -16.4; 37 -16.9; 41 -17.4; 45 -17.8; 49 -18.1; 54 -18.4; 60 -18.5; 66 -18.5; 72 -18.5; 79 -18.5; 87 -18.7; 96 -18.8; 106 -18.8; 116 -18.6; 128 -17.9; 141 -16.9; 155 -15.6; 170 -14.0; 187 -12.2; 206 -9.8; 227 -7.0; 249 -4.3; 274 -2.6; 302 -2.3; 332 -2.4; 365 -3.9; 402 -7.3; 442 -9.6; 486 -10.0; 535 -9.2; 588 -8.5; 647 -8.1; 712 -7.7; 783 -7.2; 861 -6.7; 947 -6.1; 1042 -5.3; 1146 -4.2; 1261 -3.3; 1387 -2.5; 1526 -1.9; 1678 -1.4; 1846 -1.6; 2031 -1.9; 2234 -2.2; 2457 -2.3; 2703 -2.3; 2973 -2.2; 3270 -2.3; 3597 -2.3; 3957 -2.3; 4353 -2.0; 4788 -0.7; 5267 -0.5; 5793 -6.3; 6373 -10.2; 7010 -9.8; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -9.5; 13660 -11.7; 15026 -9.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XB-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XB-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.29 | -4.1 dB  |
| Peaking | 160 Hz   | 0.21 | -11.2 dB |
| Peaking | 285 Hz   | 1.33 | 16.4 dB  |
| Peaking | 1692 Hz  | 0.73 | 6.9 dB   |
| Peaking | 4789 Hz  | 4.87 | 5.2 dB   |
| Peaking | 357 Hz   | 8.14 | 2.4 dB   |
| Peaking | 455 Hz   | 5.76 | -2.2 dB  |
| Peaking | 5952 Hz  | 1.33 | 3.9 dB   |
| Peaking | 6534 Hz  | 3.15 | -9.0 dB  |
| Peaking | 13673 Hz | 2.97 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -9.2 dB  |
| Peaking | 125 Hz   | 1.41 | -12.5 dB |
| Peaking | 250 Hz   | 1.41 | 6.0 dB   |
| Peaking | 500 Hz   | 1.41 | -3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XB-400/Sony%20XB-400.png)