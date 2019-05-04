# Sennheiser IE 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.7; 25 -12.7; 28 -12.7; 31 -12.6; 34 -12.6; 37 -12.6; 41 -12.6; 45 -12.5; 49 -12.5; 54 -12.5; 60 -12.5; 66 -12.6; 72 -12.6; 79 -12.6; 87 -12.6; 96 -12.6; 106 -12.5; 116 -12.4; 128 -12.4; 141 -12.5; 155 -12.6; 170 -12.4; 187 -12.2; 206 -11.8; 227 -11.4; 249 -11.0; 274 -10.7; 302 -10.2; 332 -9.8; 365 -9.3; 402 -9.0; 442 -8.7; 486 -8.4; 535 -8.1; 588 -7.9; 647 -7.7; 712 -7.5; 783 -7.3; 861 -7.4; 947 -7.5; 1042 -7.8; 1146 -7.9; 1261 -7.7; 1387 -7.2; 1526 -6.4; 1678 -5.4; 1846 -4.1; 2031 -2.5; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -2.9; 5793 -2.9; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -11.9; 10263 -15.4; 11289 -14.8; 12418 -16.2; 13660 -24.4; 15026 -32.0; 16529 -31.7; 18182 -28.1; 20000 -27.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.13 | -6.1 dB  |
| Peaking | 184 Hz   | 1.11 | -1.5 dB  |
| Peaking | 3734 Hz  | 0.56 | 10.6 dB  |
| Peaking | 9441 Hz  | 0.26 | 19.0 dB  |
| Peaking | 15596 Hz | 0.22 | -40.0 dB |
| Peaking | 1333 Hz  | 2.51 | -1.7 dB  |
| Peaking | 2264 Hz  | 4.99 | 2.4 dB   |
| Peaking | 6597 Hz  | 7.58 | 2.4 dB   |
| Peaking | 10113 Hz | 5.31 | -3.8 dB  |
| Peaking | 12257 Hz | 5.47 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -39.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%20800/Sennheiser%20IE%20800.png)