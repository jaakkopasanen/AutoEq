# JVC HA-SR85
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.7; 37 -3.2; 41 -5.1; 45 -6.7; 49 -7.8; 54 -8.9; 60 -9.7; 66 -10.1; 72 -10.2; 79 -10.1; 87 -10.0; 96 -10.0; 106 -10.0; 116 -9.8; 128 -9.7; 141 -9.4; 155 -9.0; 170 -8.6; 187 -8.2; 206 -8.1; 227 -7.8; 249 -7.7; 274 -7.3; 302 -6.9; 332 -6.3; 365 -5.6; 402 -5.2; 442 -5.2; 486 -5.3; 535 -6.1; 588 -7.4; 647 -8.6; 712 -9.5; 783 -9.8; 861 -9.6; 947 -9.3; 1042 -9.4; 1146 -9.7; 1261 -9.3; 1387 -8.5; 1526 -7.7; 1678 -6.8; 1846 -5.6; 2031 -4.0; 2234 -2.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -5.3; 4788 -7.7; 5267 -9.0; 5793 -9.3; 6373 -8.3; 7010 -6.7; 7711 -6.3; 8482 -7.1; 9330 -7.7; 10263 -7.2; 11289 -6.7; 12418 -7.0; 13660 -7.3; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-SR85 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-SR85 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  0.91 | 8.6 dB  |
| Peaking | 67 Hz    |  0.63 | -5.7 dB |
| Peaking | 1152 Hz  |  1.19 | -4.7 dB |
| Peaking | 3214 Hz  |  0.97 | 8.8 dB  |
| Peaking | 5263 Hz  |  1.69 | -6.6 dB |
| Peaking | 443 Hz   |  2.43 | 2.4 dB  |
| Peaking | 717 Hz   |  3.88 | -2.0 dB |
| Peaking | 3835 Hz  | 13.46 | 1.4 dB  |
| Peaking | 12147 Hz |  1.11 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-SR85/JVC%20HA-SR85.png)