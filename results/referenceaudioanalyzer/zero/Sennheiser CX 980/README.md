# Sennheiser CX 980
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.6; 23 -19.7; 25 -19.7; 28 -19.7; 31 -19.6; 34 -19.4; 37 -19.3; 41 -19.1; 45 -19.0; 49 -18.8; 54 -18.6; 60 -18.3; 66 -18.0; 72 -17.7; 79 -17.3; 87 -16.9; 96 -16.5; 106 -16.0; 116 -15.5; 128 -14.9; 141 -14.4; 155 -14.0; 170 -13.5; 187 -12.8; 206 -12.1; 227 -11.5; 249 -11.2; 274 -10.9; 302 -10.4; 332 -9.6; 365 -8.8; 402 -8.0; 442 -7.3; 486 -6.5; 535 -5.8; 588 -5.1; 647 -4.4; 712 -3.7; 783 -3.1; 861 -2.5; 947 -2.0; 1042 -1.6; 1146 -1.1; 1261 -0.9; 1387 -0.6; 1526 -0.5; 1678 -0.6; 1846 -1.0; 2031 -1.8; 2234 -2.6; 2457 -2.8; 2703 -2.4; 2973 -1.9; 3270 -1.6; 3597 -1.4; 3957 -2.2; 4353 -4.1; 4788 -6.1; 5267 -7.6; 5793 -8.3; 6373 -7.2; 7010 -4.0; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 980 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 980 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.1  | -13.8 dB |
| Peaking | 1304 Hz | 0.67 | 5.5 dB   |
| Peaking | 3588 Hz | 2.71 | 3.3 dB   |
| Peaking | 5527 Hz | 3.72 | -3.9 dB  |
| Peaking | 284 Hz  | 0.69 | 0.6 dB   |
| Peaking | 303 Hz  | 1.91 | -1.3 dB  |
| Peaking | 6373 Hz | 6.38 | -1.1 dB  |
| Peaking | 7028 Hz | 8.58 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.7 dB |
| Peaking | 62 Hz    | 1.41 | -9.0 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20980/Sennheiser%20CX%20980.png)