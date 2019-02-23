# Astro A50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.4; 25 -1.7; 28 -2.1; 31 -2.5; 34 -2.7; 37 -2.9; 41 -3.2; 45 -3.5; 49 -3.7; 54 -4.0; 60 -4.4; 66 -4.9; 72 -5.2; 79 -5.5; 87 -5.8; 96 -6.1; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.7; 155 -6.6; 170 -6.5; 187 -6.3; 206 -6.1; 227 -5.9; 249 -5.9; 274 -5.9; 302 -5.8; 332 -5.6; 365 -5.3; 402 -4.5; 442 -3.7; 486 -3.1; 535 -2.4; 588 -1.0; 647 -0.5; 712 -1.8; 783 -2.5; 861 -2.7; 947 -5.0; 1042 -5.7; 1146 -5.6; 1261 -5.4; 1387 -4.9; 1526 -4.2; 1678 -3.8; 1846 -3.4; 2031 -3.5; 2234 -2.7; 2457 -2.0; 2703 -1.6; 2973 -2.1; 3270 -2.5; 3597 -2.3; 3957 -1.8; 4353 -1.9; 4788 -2.5; 5267 -5.5; 5793 -5.1; 6373 -9.8; 7010 -9.2; 7711 -7.2; 8482 -6.9; 9330 -5.9; 10263 -4.6; 11289 -4.9; 12418 -8.1; 13660 -8.3; 15026 -4.9; 16529 -4.6; 18182 -4.6; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.89 | 3.5 dB  |
| Peaking | 632 Hz   | 3.87 | 4.4 dB  |
| Peaking | 4007 Hz  | 1.01 | 3.9 dB  |
| Peaking | 6735 Hz  | 1.89 | -6.3 dB |
| Peaking | 20200 Hz | 1.2  | -5.5 dB |
| Peaking | 136 Hz   | 1.2  | -2.3 dB |
| Peaking | 282 Hz   | 2.84 | -1.1 dB |
| Peaking | 1138 Hz  | 4.55 | -1.8 dB |
| Peaking | 13323 Hz | 2.73 | -5.9 dB |
| Peaking | 14023 Hz | 0.66 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A50/Astro%20A50.png)