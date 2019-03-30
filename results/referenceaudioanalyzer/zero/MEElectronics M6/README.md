# MEElectronics M6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.5; 23 -17.9; 25 -18.3; 28 -18.7; 31 -18.9; 34 -19.0; 37 -19.0; 41 -18.9; 45 -18.8; 49 -18.7; 54 -18.4; 60 -18.0; 66 -17.6; 72 -17.2; 79 -16.8; 87 -16.2; 96 -15.5; 106 -14.8; 116 -14.2; 128 -13.5; 141 -12.7; 155 -12.0; 170 -11.2; 187 -10.4; 206 -9.6; 227 -8.8; 249 -8.0; 274 -7.1; 302 -6.3; 332 -5.6; 365 -5.1; 402 -4.5; 442 -3.8; 486 -3.0; 535 -2.2; 588 -1.7; 647 -1.1; 712 -0.6; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.2; 2031 -2.5; 2234 -4.3; 2457 -6.7; 2703 -9.7; 2973 -12.0; 3270 -12.4; 3597 -11.1; 3957 -9.5; 4353 -9.7; 4788 -13.6; 5267 -16.8; 5793 -16.0; 6373 -10.4; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -8.1; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEElectronics M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEElectronics M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 38 Hz    |  0.25 | -12.6 dB |
| Peaking | 1630 Hz  |  0.23 | 7.9 dB   |
| Peaking | 3078 Hz  |  1.87 | -12.0 dB |
| Peaking | 5407 Hz  |  2.94 | -14.3 dB |
| Peaking | 9644 Hz  |  4.76 | -2.8 dB  |
| Peaking | 1172 Hz  |  3.42 | -0.6 dB  |
| Peaking | 1779 Hz  |  5.55 | 0.8 dB   |
| Peaking | 6069 Hz  | 10.49 | -1.8 dB  |
| Peaking | 7100 Hz  |  6.1  | 1.9 dB   |
| Peaking | 13374 Hz |  1.39 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MEElectronics%20M6/MEElectronics%20M6.png)