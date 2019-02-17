# Pioneer SE Master 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.7; 28 -2.4; 31 -2.9; 34 -3.1; 37 -3.3; 41 -3.7; 45 -4.4; 49 -5.1; 54 -5.9; 60 -6.6; 66 -7.2; 72 -7.7; 79 -8.3; 87 -8.8; 96 -9.3; 106 -9.7; 116 -9.9; 128 -10.2; 141 -10.2; 155 -10.4; 170 -10.2; 187 -10.2; 206 -10.0; 227 -9.6; 249 -9.3; 274 -8.9; 302 -8.4; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.5; 486 -6.2; 535 -5.6; 588 -4.8; 647 -4.5; 712 -4.4; 783 -3.9; 861 -3.8; 947 -3.5; 1042 -3.0; 1146 -2.2; 1261 -1.2; 1387 -1.0; 1526 -1.5; 1678 -1.9; 1846 -2.8; 2031 -4.3; 2234 -5.4; 2457 -5.6; 2703 -6.0; 2973 -6.0; 3270 -4.4; 3597 -2.7; 3957 -2.6; 4353 -4.7; 4788 -6.5; 5267 -7.6; 5793 -12.6; 6373 -13.5; 7010 -7.5; 7711 -6.1; 8482 -5.2; 9330 -4.2; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -6.2; 18182 -12.6; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE Master 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE Master 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.67 | 4.2 dB   |
| Peaking | 121 Hz   | 0.6  | -6.4 dB  |
| Peaking | 279 Hz   | 1.02 | -3.0 dB  |
| Peaking | 2691 Hz  | 4.61 | -2.9 dB  |
| Peaking | 6119 Hz  | 4.3  | -12.2 dB |
| Peaking | 484 Hz   | 3.69 | -0.7 dB  |
| Peaking | 1400 Hz  | 2.28 | 2.8 dB   |
| Peaking | 2217 Hz  | 5.41 | -1.8 dB  |
| Peaking | 3807 Hz  | 8.38 | 2.2 dB   |
| Peaking | 19255 Hz | 1.2  | -12.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE%20Master%201/Pioneer%20SE%20Master%201.png)