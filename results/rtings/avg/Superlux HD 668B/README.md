# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -3.0; 31 -3.9; 34 -4.7; 37 -5.5; 41 -6.3; 45 -6.9; 49 -7.4; 54 -7.9; 60 -8.4; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.1; 141 -9.7; 155 -9.2; 170 -8.6; 187 -8.0; 206 -7.7; 227 -7.6; 249 -7.6; 274 -7.6; 302 -7.7; 332 -7.7; 365 -7.3; 402 -7.3; 442 -7.3; 486 -7.2; 535 -6.3; 588 -6.5; 647 -6.5; 712 -6.3; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.3; 1146 -5.2; 1261 -5.4; 1387 -5.7; 1526 -6.5; 1678 -7.9; 1846 -9.7; 2031 -11.0; 2234 -10.5; 2457 -9.7; 2703 -8.7; 2973 -8.1; 3270 -8.0; 3597 -6.6; 3957 -5.2; 4353 -3.7; 4788 -3.8; 5267 -12.0; 5793 -13.2; 6373 -10.4; 7010 -9.5; 7711 -11.2; 8482 -13.5; 9330 -14.3; 10263 -13.8; 11289 -13.2; 12418 -11.2; 13660 -10.7; 15026 -13.6; 16529 -13.1; 18182 -10.0; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.08 | 4.1 dB  |
| Peaking | 2129 Hz  | 2.52 | -5.5 dB |
| Peaking | 6082 Hz  | 1.95 | -3.7 dB |
| Peaking | 9552 Hz  | 2.15 | -5.5 dB |
| Peaking | 16485 Hz | 0.53 | -7.6 dB |
| Peaking | 71 Hz    | 1.59 | -2.3 dB |
| Peaking | 119 Hz   | 1.11 | -4.3 dB |
| Peaking | 355 Hz   | 1.19 | -1.7 dB |
| Peaking | 4648 Hz  | 4.37 | 5.9 dB  |
| Peaking | 5456 Hz  | 8.47 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB   |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 16000 Hz | 1.41 | -10.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20668B/Superlux%20HD%20668B.png)