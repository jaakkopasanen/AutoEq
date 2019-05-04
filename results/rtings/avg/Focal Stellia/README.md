# Focal Stellia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -3.8; 25 -3.7; 28 -3.7; 31 -3.7; 34 -3.9; 37 -4.1; 41 -4.5; 45 -4.9; 49 -5.3; 54 -5.7; 60 -6.1; 66 -6.6; 72 -7.1; 79 -7.7; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.2; 128 -9.3; 141 -9.1; 155 -8.9; 170 -8.4; 187 -7.6; 206 -6.7; 227 -5.9; 249 -5.2; 274 -5.0; 302 -5.0; 332 -5.3; 365 -5.6; 402 -6.0; 442 -6.6; 486 -7.0; 535 -7.3; 588 -7.4; 647 -7.5; 712 -7.4; 783 -7.4; 861 -7.5; 947 -7.5; 1042 -7.4; 1146 -7.4; 1261 -7.5; 1387 -7.9; 1526 -8.3; 1678 -8.8; 1846 -9.8; 2031 -9.4; 2234 -8.3; 2457 -8.2; 2703 -7.3; 2973 -6.2; 3270 -4.5; 3597 -6.0; 3957 -2.1; 4353 -0.5; 4788 -3.7; 5267 -3.3; 5793 -2.8; 6373 -3.9; 7010 -4.1; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.8; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Stellia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Stellia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  0.93 | 3.0 dB  |
| Peaking | 116 Hz   |  1.63 | -3.4 dB |
| Peaking | 1856 Hz  |  1.58 | -3.1 dB |
| Peaking | 4233 Hz  |  4.6  | 6.0 dB  |
| Peaking | 5909 Hz  |  2.96 | 3.3 dB  |
| Peaking | 170 Hz   |  2.77 | -1.5 dB |
| Peaking | 284 Hz   |  1.34 | 2.2 dB  |
| Peaking | 593 Hz   |  1.29 | -1.2 dB |
| Peaking | 3210 Hz  | 12.06 | 1.8 dB  |
| Peaking | 19839 Hz |  2.08 | -6.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Stellia/Focal%20Stellia.png)