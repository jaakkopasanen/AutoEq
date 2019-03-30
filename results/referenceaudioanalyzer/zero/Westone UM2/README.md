# Westone UM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -8.0; 25 -8.4; 28 -8.9; 31 -9.3; 34 -9.6; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.3; 54 -10.4; 60 -10.4; 66 -10.5; 72 -10.7; 79 -10.8; 87 -10.8; 96 -10.8; 106 -11.1; 116 -11.1; 128 -11.1; 141 -10.8; 155 -10.8; 170 -10.8; 187 -10.8; 206 -10.7; 227 -10.4; 249 -10.4; 274 -10.4; 302 -10.2; 332 -10.1; 365 -9.8; 402 -9.7; 442 -9.5; 486 -9.2; 535 -9.0; 588 -8.7; 647 -8.3; 712 -8.1; 783 -7.8; 861 -7.6; 947 -7.5; 1042 -7.5; 1146 -7.6; 1261 -8.0; 1387 -8.4; 1526 -8.7; 1678 -8.7; 1846 -8.1; 2031 -7.5; 2234 -6.7; 2457 -5.8; 2703 -5.2; 2973 -5.4; 3270 -6.0; 3597 -5.8; 3957 -3.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.4  | -3.7 dB |
| Peaking | 290 Hz  | 0.51 | -2.7 dB |
| Peaking | 1636 Hz | 2.13 | -2.2 dB |
| Peaking | 2604 Hz | 5.77 | 1.0 dB  |
| Peaking | 5205 Hz | 1.98 | 7.0 dB  |
| Peaking | 3559 Hz | 7.83 | -1.3 dB |
| Peaking | 4304 Hz | 7.15 | 2.5 dB  |
| Peaking | 6450 Hz | 4.22 | 4.9 dB  |
| Peaking | 6622 Hz | 1.57 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%20UM2/Westone%20UM2.png)