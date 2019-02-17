# AKG Q701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.7; 31 -2.2; 34 -2.7; 37 -3.0; 41 -3.4; 45 -3.7; 49 -4.0; 54 -4.3; 60 -4.6; 66 -5.0; 72 -5.3; 79 -5.7; 87 -6.2; 96 -6.7; 106 -7.1; 116 -7.6; 128 -8.0; 141 -8.4; 155 -8.7; 170 -8.8; 187 -8.9; 206 -8.9; 227 -8.9; 249 -8.9; 274 -9.0; 302 -9.0; 332 -9.0; 365 -9.0; 402 -9.0; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.4; 647 -7.4; 712 -7.1; 783 -6.7; 861 -6.6; 947 -6.8; 1042 -6.6; 1146 -6.7; 1261 -7.1; 1387 -7.5; 1526 -8.5; 1678 -10.0; 1846 -11.4; 2031 -12.6; 2234 -13.0; 2457 -12.0; 2703 -11.0; 2973 -9.8; 3270 -8.4; 3597 -8.9; 3957 -9.4; 4353 -9.7; 4788 -9.5; 5267 -10.0; 5793 -11.4; 6373 -14.4; 7010 -14.1; 7711 -13.6; 8482 -13.9; 9330 -10.4; 10263 -6.7; 11289 -8.1; 12418 -9.1; 13660 -6.7; 15026 -6.6; 16529 -9.0; 18182 -14.3; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.02 | 6.0 dB  |
| Peaking | 2204 Hz  | 1.88 | -6.3 dB |
| Peaking | 6610 Hz  | 2.31 | -7.0 dB |
| Peaking | 8399 Hz  | 4.68 | -4.8 dB |
| Peaking | 19025 Hz | 1.24 | -9.3 dB |
| Peaking | 64 Hz    | 0.78 | 3.3 dB  |
| Peaking | 190 Hz   | 0.19 | -3.1 dB |
| Peaking | 920 Hz   | 0.91 | 2.3 dB  |
| Peaking | 4224 Hz  | 7.49 | -1.2 dB |
| Peaking | 15225 Hz | 3.65 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20Q701/AKG%20Q701.png)