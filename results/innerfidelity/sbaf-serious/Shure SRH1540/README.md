# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.3; 28 -7.0; 31 -7.6; 34 -8.0; 37 -8.4; 41 -8.8; 45 -9.1; 49 -9.2; 54 -9.4; 60 -9.5; 66 -9.4; 72 -9.2; 79 -8.8; 87 -8.5; 96 -8.2; 106 -8.2; 116 -8.2; 128 -8.1; 141 -7.6; 155 -6.5; 170 -5.3; 187 -5.6; 206 -5.1; 227 -4.7; 249 -4.7; 274 -4.6; 302 -4.9; 332 -5.1; 365 -4.8; 402 -4.5; 442 -3.9; 486 -3.5; 535 -3.0; 588 -2.2; 647 -1.8; 712 -1.4; 783 -1.0; 861 -0.9; 947 -0.9; 1042 -1.1; 1146 -1.0; 1261 -0.9; 1387 -1.4; 1526 -2.2; 1678 -3.2; 1846 -4.2; 2031 -4.4; 2234 -4.1; 2457 -3.8; 2703 -3.1; 2973 -2.3; 3270 -2.5; 3597 -2.3; 3957 -2.0; 4353 -1.9; 4788 -1.5; 5267 -0.5; 5793 -3.2; 6373 -4.9; 7010 -2.7; 7711 -3.2; 8482 -3.7; 9330 -4.9; 10263 -3.5; 11289 -3.5; 12418 -3.5; 13660 -3.5; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 55 Hz   |  0.6  | -5.9 dB |
| Peaking | 127 Hz  |  2.38 | -2.0 dB |
| Peaking | 354 Hz  |  2.35 | -1.4 dB |
| Peaking | 904 Hz  |  1.22 | 3.1 dB  |
| Peaking | 4841 Hz |  3.23 | 2.5 dB  |
| Peaking | 1379 Hz |  3.19 | 1.6 dB  |
| Peaking | 2165 Hz |  1.35 | -3.0 dB |
| Peaking | 2806 Hz |  1.31 | 2.3 dB  |
| Peaking | 6209 Hz | 12.06 | -2.6 dB |
| Peaking | 9188 Hz |  8.6  | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)