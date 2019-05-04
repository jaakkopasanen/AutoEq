# Astro A40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.5; 28 -7.9; 31 -8.2; 34 -8.5; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.3; 54 -9.6; 60 -9.9; 66 -10.3; 72 -10.6; 79 -11.0; 87 -11.3; 96 -11.5; 106 -11.7; 116 -11.8; 128 -11.9; 141 -11.7; 155 -11.5; 170 -11.2; 187 -10.7; 206 -10.2; 227 -9.6; 249 -9.1; 274 -8.8; 302 -8.4; 332 -8.0; 365 -7.3; 402 -6.5; 442 -6.3; 486 -6.5; 535 -6.4; 588 -6.2; 647 -6.0; 712 -5.8; 783 -5.7; 861 -5.5; 947 -5.5; 1042 -5.9; 1146 -6.1; 1261 -6.3; 1387 -6.7; 1526 -7.0; 1678 -7.0; 1846 -5.5; 2031 -4.6; 2234 -5.0; 2457 -3.8; 2703 -2.9; 2973 -2.4; 3270 -4.4; 3597 -3.8; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -4.5; 5793 -7.4; 6373 -9.8; 7010 -8.5; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 79 Hz   |  0.66 | -3.7 dB |
| Peaking | 156 Hz  |  1.13 | -3.3 dB |
| Peaking | 2710 Hz |  3.08 | 3.2 dB  |
| Peaking | 4412 Hz |  2.67 | 6.8 dB  |
| Peaking | 6348 Hz |  3.71 | -4.7 dB |
| Peaking | 281 Hz  |  2.53 | -0.8 dB |
| Peaking | 1184 Hz |  0.46 | 1.5 dB  |
| Peaking | 1703 Hz |  1.5  | -2.7 dB |
| Peaking | 1947 Hz |  6.78 | 2.4 dB  |
| Peaking | 3422 Hz | 13.51 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A40/Astro%20A40.png)