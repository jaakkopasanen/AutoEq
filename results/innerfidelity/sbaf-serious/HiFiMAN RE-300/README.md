# HiFiMAN RE-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.8; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.3; 45 -9.5; 49 -9.6; 54 -9.9; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.1; 87 -11.5; 96 -11.9; 106 -12.1; 116 -12.3; 128 -12.5; 141 -12.7; 155 -12.8; 170 -12.8; 187 -12.7; 206 -12.7; 227 -12.4; 249 -12.2; 274 -12.0; 302 -11.6; 332 -11.2; 365 -10.8; 402 -10.4; 442 -9.8; 486 -9.5; 535 -8.9; 588 -8.2; 647 -7.8; 712 -7.7; 783 -7.4; 861 -7.6; 947 -8.1; 1042 -8.9; 1146 -8.9; 1261 -9.3; 1387 -10.9; 1526 -11.9; 1678 -11.7; 1846 -10.1; 2031 -7.1; 2234 -3.8; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -6.1; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.24 | -2.0 dB |
| Peaking | 129 Hz  |  0.68 | -3.3 dB |
| Peaking | 276 Hz  |  0.73 | -3.5 dB |
| Peaking | 1642 Hz |  1.7  | -9.8 dB |
| Peaking | 2947 Hz |  0.79 | 8.7 dB  |
| Peaking | 1076 Hz | 12.02 | -0.9 dB |
| Peaking | 2451 Hz |  8.53 | 1.8 dB  |
| Peaking | 3187 Hz |  3.55 | -1.0 dB |
| Peaking | 5390 Hz |  2.57 | 6.0 dB  |
| Peaking | 6249 Hz |  1.46 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-300/HiFiMAN%20RE-300.png)