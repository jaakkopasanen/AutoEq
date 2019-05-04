# Astro A10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.8; 25 -4.5; 28 -5.5; 31 -6.3; 34 -7.0; 37 -7.6; 41 -8.3; 45 -8.8; 49 -9.3; 54 -9.7; 60 -10.1; 66 -10.3; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.7; 106 -10.5; 116 -10.3; 128 -10.1; 141 -9.7; 155 -9.4; 170 -8.9; 187 -8.4; 206 -7.8; 227 -7.5; 249 -7.6; 274 -7.5; 302 -7.6; 332 -6.7; 365 -6.3; 402 -5.8; 442 -5.4; 486 -4.8; 535 -3.0; 588 -0.6; 647 -0.5; 712 -0.5; 783 -3.3; 861 -7.1; 947 -10.1; 1042 -12.0; 1146 -12.5; 1261 -11.9; 1387 -11.3; 1526 -9.9; 1678 -8.5; 1846 -7.3; 2031 -5.7; 2234 -6.0; 2457 -5.3; 2703 -4.7; 2973 -4.1; 3270 -3.5; 3597 -2.7; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -5.3; 5793 -6.7; 6373 -7.7; 7010 -9.9; 7711 -10.3; 8482 -8.8; 9330 -6.5; 10263 -6.5; 11289 -7.1; 12418 -9.3; 13660 -9.9; 15026 -9.9; 16529 -7.1; 18182 -6.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  1.23 | 4.5 dB  |
| Peaking | 82 Hz    |  0.54 | -4.5 dB |
| Peaking | 669 Hz   |  2.02 | 8.7 dB  |
| Peaking | 1108 Hz  |  1.83 | -8.2 dB |
| Peaking | 4095 Hz  |  2.76 | 6.8 dB  |
| Peaking | 1473 Hz  |  5.01 | -1.3 dB |
| Peaking | 2384 Hz  |  1.83 | 1.4 dB  |
| Peaking | 4813 Hz  | 11.43 | 3.0 dB  |
| Peaking | 7324 Hz  |  3.14 | -4.4 dB |
| Peaking | 14176 Hz |  2.06 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A10/Astro%20A10.png)