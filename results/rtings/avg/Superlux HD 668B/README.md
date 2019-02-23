# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -2.3; 34 -3.1; 37 -3.8; 41 -4.6; 45 -5.3; 49 -5.7; 54 -6.2; 60 -6.8; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.5; 96 -8.7; 106 -8.7; 116 -8.7; 128 -8.5; 141 -8.1; 155 -7.6; 170 -6.9; 187 -6.3; 206 -6.0; 227 -5.9; 249 -6.0; 274 -6.0; 302 -6.1; 332 -6.0; 365 -5.6; 402 -5.6; 442 -5.7; 486 -5.6; 535 -4.6; 588 -4.8; 647 -4.8; 712 -4.7; 783 -4.4; 861 -4.0; 947 -3.9; 1042 -3.6; 1146 -3.5; 1261 -3.7; 1387 -4.1; 1526 -4.9; 1678 -6.2; 1846 -8.0; 2031 -9.4; 2234 -8.9; 2457 -8.0; 2703 -7.0; 2973 -6.4; 3270 -6.3; 3597 -5.0; 3957 -3.5; 4353 -2.0; 4788 -2.2; 5267 -10.4; 5793 -11.6; 6373 -8.8; 7010 -7.8; 7711 -9.6; 8482 -11.9; 9330 -12.6; 10263 -12.2; 11289 -11.6; 12418 -9.6; 13660 -9.0; 15026 -11.9; 16529 -11.4; 18182 -8.4; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 2    | 6.9 dB  |
| Peaking | 4624 Hz  | 3.38 | 7.3 dB  |
| Peaking | 5489 Hz  | 6.04 | -8.7 dB |
| Peaking | 9617 Hz  | 1.79 | -6.1 dB |
| Peaking | 15966 Hz | 1.39 | -5.4 dB |
| Peaking | 97 Hz    | 0.36 | 2.3 dB  |
| Peaking | 101 Hz   | 0.86 | -4.8 dB |
| Peaking | 1059 Hz  | 0.72 | 1.5 dB  |
| Peaking | 1466 Hz  | 0.9  | 2.6 dB  |
| Peaking | 2062 Hz  | 2.08 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20668B/Superlux%20HD%20668B.png)