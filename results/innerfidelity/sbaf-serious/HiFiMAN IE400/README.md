# HiFiMAN IE400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.9; 25 -3.9; 28 -4.0; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.3; 66 -5.6; 72 -5.9; 79 -6.3; 87 -6.7; 96 -7.2; 106 -7.5; 116 -7.7; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.8; 227 -8.7; 249 -8.7; 274 -8.6; 302 -8.4; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.5; 486 -7.5; 535 -7.2; 588 -6.7; 647 -6.6; 712 -6.7; 783 -6.5; 861 -6.9; 947 -7.3; 1042 -7.8; 1146 -8.4; 1261 -9.1; 1387 -10.1; 1526 -11.2; 1678 -12.2; 1846 -12.7; 2031 -12.5; 2234 -10.7; 2457 -7.9; 2703 -5.7; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -2.2; 5267 -2.5; 5793 -4.0; 6373 -4.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN IE400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN IE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.71 | 2.6 dB  |
| Peaking | 52 Hz   |  1.37 | 1.0 dB  |
| Peaking | 197 Hz  |  0.76 | -2.5 dB |
| Peaking | 1949 Hz |  1.53 | -9.2 dB |
| Peaking | 3518 Hz |  1.21 | 8.5 dB  |
| Peaking | 759 Hz  |  2.84 | 0.9 dB  |
| Peaking | 1399 Hz |  4.77 | -0.5 dB |
| Peaking | 6885 Hz | 10.17 | 1.7 dB  |
| Peaking | 8407 Hz |  2.24 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20IE400/HiFiMAN%20IE400.png)