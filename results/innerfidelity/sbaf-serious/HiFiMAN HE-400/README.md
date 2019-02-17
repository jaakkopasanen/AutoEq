# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.8; 106 -0.9; 116 -1.1; 128 -1.4; 141 -1.5; 155 -1.7; 170 -2.0; 187 -2.1; 206 -1.6; 227 -1.6; 249 -2.4; 274 -1.1; 302 -1.6; 332 -2.3; 365 -2.3; 402 -2.2; 442 -2.6; 486 -2.5; 535 -1.6; 588 -0.7; 647 -1.9; 712 -3.1; 783 -3.6; 861 -5.4; 947 -6.3; 1042 -5.3; 1146 -4.2; 1261 -3.9; 1387 -1.8; 1526 -0.8; 1678 -0.9; 1846 -0.5; 2031 -0.9; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.2  | 6.2 dB  |
| Peaking | 311 Hz   | 1.31 | 2.4 dB  |
| Peaking | 580 Hz   | 4.12 | 3.8 dB  |
| Peaking | 3729 Hz  | 0.42 | 6.8 dB  |
| Peaking | 9038 Hz  | 1.55 | -4.1 dB |
| Peaking | 964 Hz   | 5.63 | -2.9 dB |
| Peaking | 1606 Hz  | 3.38 | 1.9 dB  |
| Peaking | 5490 Hz  | 1.09 | -1.5 dB |
| Peaking | 5930 Hz  | 3.19 | 3.1 dB  |
| Peaking | 13630 Hz | 4.96 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)