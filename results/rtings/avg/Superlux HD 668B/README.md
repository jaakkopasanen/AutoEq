# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.0; 34 -2.9; 37 -3.6; 41 -4.4; 45 -5.1; 49 -5.6; 54 -6.1; 60 -6.7; 66 -7.1; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.5; 106 -8.5; 116 -8.4; 128 -8.3; 141 -7.9; 155 -7.4; 170 -6.8; 187 -6.1; 206 -5.9; 227 -5.9; 249 -5.9; 274 -5.9; 302 -6.0; 332 -6.0; 365 -5.6; 402 -5.6; 442 -5.6; 486 -5.7; 535 -4.8; 588 -4.8; 647 -5.0; 712 -4.8; 783 -4.5; 861 -4.1; 947 -4.0; 1042 -3.8; 1146 -3.7; 1261 -3.9; 1387 -4.2; 1526 -5.1; 1678 -6.5; 1846 -8.4; 2031 -9.8; 2234 -9.7; 2457 -9.0; 2703 -7.6; 2973 -6.5; 3270 -6.1; 3597 -4.7; 3957 -3.1; 4353 -1.6; 4788 -2.8; 5267 -10.5; 5793 -11.6; 6373 -7.7; 7010 -7.9; 7711 -10.4; 8482 -11.5; 9330 -11.0; 10263 -11.7; 11289 -12.5; 12418 -9.7; 13660 -8.3; 15026 -11.6; 16529 -11.2; 18182 -8.1; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.87 | 6.7 dB  |
| Peaking | 4499 Hz  | 3.72 | 6.9 dB  |
| Peaking | 5527 Hz  | 7.07 | -7.4 dB |
| Peaking | 9937 Hz  | 1.27 | -5.4 dB |
| Peaking | 16105 Hz | 1.96 | -5.1 dB |
| Peaking | 103 Hz   | 1.06 | -3.3 dB |
| Peaking | 256 Hz   | 0.07 | 1.1 dB  |
| Peaking | 921 Hz   | 1.53 | 0.7 dB  |
| Peaking | 1336 Hz  | 1.37 | 2.3 dB  |
| Peaking | 2099 Hz  | 2.23 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20668B/Superlux%20HD%20668B.png)