# Astro A20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -3.0; 34 -3.7; 37 -4.2; 41 -4.8; 45 -5.3; 49 -5.8; 54 -6.3; 60 -6.8; 66 -7.2; 72 -7.4; 79 -7.7; 87 -7.8; 96 -7.9; 106 -8.0; 116 -7.9; 128 -7.9; 141 -7.6; 155 -7.1; 170 -6.8; 187 -6.3; 206 -5.7; 227 -5.1; 249 -4.4; 274 -4.2; 302 -4.3; 332 -3.1; 365 -2.0; 402 -1.5; 442 -2.3; 486 -3.0; 535 -3.7; 588 -4.2; 647 -3.7; 712 -3.0; 783 -3.2; 861 -3.0; 947 -2.9; 1042 -2.4; 1146 -1.6; 1261 -1.2; 1387 -0.8; 1526 -0.8; 1678 -0.9; 1846 -1.2; 2031 -1.2; 2234 -1.3; 2457 -1.3; 2703 -2.2; 2973 -4.3; 3270 -5.9; 3597 -7.1; 3957 -8.2; 4353 -7.1; 4788 -8.4; 5267 -12.4; 5793 -11.9; 6373 -10.9; 7010 -11.2; 7711 -11.2; 8482 -11.2; 9330 -7.7; 10263 -5.1; 11289 -5.1; 12418 -6.4; 13660 -8.4; 15026 -7.6; 16529 -7.4; 18182 -7.9; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 3.02 | 4.9 dB  |
| Peaking | 396 Hz   | 3.78 | 3.5 dB  |
| Peaking | 1774 Hz  | 0.78 | 5.1 dB  |
| Peaking | 5731 Hz  | 1.16 | -7.2 dB |
| Peaking | 8196 Hz  | 4.68 | -3.3 dB |
| Peaking | 102 Hz   | 1.09 | -3.3 dB |
| Peaking | 3658 Hz  | 3.19 | -4.3 dB |
| Peaking | 3862 Hz  | 1.56 | 3.4 dB  |
| Peaking | 10698 Hz | 2.27 | 4.2 dB  |
| Peaking | 15566 Hz | 0.31 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A20/Astro%20A20.png)