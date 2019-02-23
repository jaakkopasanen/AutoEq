# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.7; 28 -3.8; 31 -3.9; 34 -4.0; 37 -4.2; 41 -4.3; 45 -4.5; 49 -4.6; 54 -4.8; 60 -5.2; 66 -5.5; 72 -5.9; 79 -6.3; 87 -6.7; 96 -7.2; 106 -7.5; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.8; 187 -8.8; 206 -9.0; 227 -9.0; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.8; 365 -8.7; 402 -8.7; 442 -8.4; 486 -8.3; 535 -7.8; 588 -7.3; 647 -7.0; 712 -6.7; 783 -6.5; 861 -6.7; 947 -6.8; 1042 -7.1; 1146 -7.3; 1261 -7.4; 1387 -7.8; 1526 -8.1; 1678 -8.2; 1846 -7.9; 2031 -7.6; 2234 -7.5; 2457 -6.5; 2703 -3.8; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -7.6; 4353 -8.1; 4788 -6.3; 5267 -5.0; 5793 -6.5; 6373 -9.5; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  0.73 | 2.8 dB  |
| Peaking | 53 Hz   |  1.41 | 1.2 dB  |
| Peaking | 225 Hz  |  0.63 | -2.7 dB |
| Peaking | 2885 Hz |  0.85 | -3.8 dB |
| Peaking | 3103 Hz |  2.84 | 10.8 dB |
| Peaking | 819 Hz  |  1.6  | 1.3 dB  |
| Peaking | 2002 Hz |  0.22 | -0.7 dB |
| Peaking | 3527 Hz | 16.78 | 3.2 dB  |
| Peaking | 6267 Hz |  2.59 | 4.8 dB  |
| Peaking | 6337 Hz |  6.59 | -7.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GR8/Grado%20GR8.png)