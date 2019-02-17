# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.2; 25 -3.2; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.8; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.7; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.7; 106 -7.0; 116 -7.2; 128 -7.6; 141 -7.9; 155 -8.1; 170 -8.2; 187 -8.3; 206 -8.4; 227 -8.5; 249 -8.5; 274 -8.5; 302 -8.4; 332 -8.3; 365 -8.2; 402 -8.1; 442 -7.9; 486 -7.8; 535 -7.2; 588 -6.8; 647 -6.5; 712 -6.2; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.2; 1526 -7.6; 1678 -7.7; 1846 -7.4; 2031 -7.1; 2234 -6.9; 2457 -6.0; 2703 -3.2; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -7.0; 4353 -7.6; 4788 -5.8; 5267 -4.5; 5793 -6.0; 6373 -9.0; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.64 | 3.3 dB  |
| Peaking | 54 Hz   | 1.21 | 1.3 dB  |
| Peaking | 221 Hz  | 0.65 | -2.2 dB |
| Peaking | 3167 Hz | 4.31 | 7.2 dB  |
| Peaking | 797 Hz  | 1.63 | 1.6 dB  |
| Peaking | 1151 Hz | 0.38 | -0.7 dB |
| Peaking | 1919 Hz | 1.35 | -0.9 dB |
| Peaking | 2816 Hz | 7.25 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GR8/Grado%20GR8.png)