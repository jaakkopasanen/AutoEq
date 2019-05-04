# Marshall Major II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.5; 25 -7.5; 28 -7.4; 31 -7.3; 34 -7.1; 37 -7.0; 41 -6.7; 45 -6.6; 49 -6.5; 54 -6.6; 60 -6.7; 66 -6.8; 72 -6.9; 79 -7.0; 87 -7.2; 96 -7.3; 106 -7.3; 116 -7.4; 128 -7.4; 141 -7.4; 155 -7.3; 170 -7.1; 187 -6.7; 206 -6.2; 227 -5.7; 249 -5.3; 274 -5.6; 302 -6.1; 332 -6.6; 365 -7.2; 402 -8.0; 442 -8.8; 486 -9.4; 535 -9.4; 588 -9.3; 647 -8.9; 712 -8.5; 783 -8.1; 861 -7.8; 947 -7.7; 1042 -7.5; 1146 -7.0; 1261 -7.1; 1387 -6.9; 1526 -6.2; 1678 -5.5; 1846 -5.0; 2031 -4.4; 2234 -3.2; 2457 -1.9; 2703 -1.2; 2973 -1.2; 3270 -1.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -1.1; 5793 -0.5; 6373 -2.5; 7010 -7.3; 7711 -8.5; 8482 -5.4; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -7.4; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.22 | -1.9 dB |
| Peaking | 668 Hz  | 0.79 | -3.8 dB |
| Peaking | 3322 Hz | 1.16 | 4.5 dB  |
| Peaking | 5992 Hz | 2.18 | 4.8 dB  |
| Peaking | 7287 Hz | 3.83 | -6.5 dB |
| Peaking | 143 Hz  | 0.83 | -3.9 dB |
| Peaking | 294 Hz  | 0.3  | 4.1 dB  |
| Peaking | 474 Hz  | 1.34 | -4.0 dB |
| Peaking | 1343 Hz | 0.93 | -1.8 dB |
| Peaking | 2508 Hz | 5.97 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Marshall%20Major%20II/Marshall%20Major%20II.png)