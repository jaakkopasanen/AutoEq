# TDK BA200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.4; 28 -6.5; 31 -6.6; 34 -6.7; 37 -6.8; 41 -6.9; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.6; 106 -9.8; 116 -9.9; 128 -10.3; 141 -10.4; 155 -10.6; 170 -10.6; 187 -10.7; 206 -10.7; 227 -10.5; 249 -10.4; 274 -10.2; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.1; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.1; 647 -6.8; 712 -6.5; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.9; 1526 -8.5; 1678 -9.1; 1846 -9.2; 2031 -8.8; 2234 -8.1; 2457 -6.6; 2703 -5.0; 2973 -2.8; 3270 -0.8; 3597 -0.5; 3957 -0.9; 4353 -3.4; 4788 -2.9; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -10.9; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK BA200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 180 Hz  | 0.6  | -4.4 dB |
| Peaking | 1914 Hz | 2.2  | -3.6 dB |
| Peaking | 3464 Hz | 2.46 | 6.3 dB  |
| Peaking | 5905 Hz | 2.56 | 6.1 dB  |
| Peaking | 9118 Hz | 4.18 | -5.5 dB |
| Peaking | 23 Hz   | 1.13 | 0.4 dB  |
| Peaking | 383 Hz  | 2.27 | -0.7 dB |
| Peaking | 794 Hz  | 1.73 | 1.1 dB  |
| Peaking | 1492 Hz | 4.9  | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20BA200/TDK%20BA200.png)