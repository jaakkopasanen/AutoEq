# ASTRO Gaming A10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.3; 25 -7.1; 28 -8.1; 31 -9.0; 34 -9.8; 37 -10.6; 41 -11.4; 45 -12.2; 49 -12.7; 54 -13.0; 60 -13.2; 66 -13.3; 72 -13.4; 79 -13.3; 87 -13.1; 96 -12.9; 106 -12.5; 116 -12.0; 128 -11.5; 141 -10.9; 155 -10.3; 170 -9.7; 187 -9.1; 206 -8.5; 227 -8.0; 249 -7.5; 274 -7.2; 302 -7.2; 332 -6.7; 365 -5.8; 402 -4.8; 442 -3.7; 486 -2.6; 535 -1.0; 588 -0.5; 647 -0.5; 712 -0.5; 783 -2.7; 861 -7.1; 947 -10.4; 1042 -12.4; 1146 -13.1; 1261 -12.8; 1387 -11.6; 1526 -9.8; 1678 -7.9; 1846 -5.9; 2031 -4.7; 2234 -4.2; 2457 -3.6; 2703 -2.9; 2973 -2.0; 3270 -1.4; 3597 -2.2; 3957 -3.8; 4353 -4.4; 4788 -7.5; 5267 -12.0; 5793 -14.0; 6373 -13.4; 7010 -10.5; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASTRO Gaming A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASTRO Gaming A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 77 Hz   |  0.58 | -7.1 dB  |
| Peaking | 675 Hz  |  1.3  | 11.7 dB  |
| Peaking | 1113 Hz |  1.13 | -13.1 dB |
| Peaking | 3424 Hz |  0.59 | 7.6 dB   |
| Peaking | 5815 Hz |  2.18 | -12.9 dB |
| Peaking | 15 Hz   |  1.16 | 3.6 dB   |
| Peaking | 44 Hz   |  2.22 | -1.2 dB  |
| Peaking | 321 Hz  |  6.23 | -0.7 dB  |
| Peaking | 519 Hz  |  7.71 | 0.7 dB   |
| Peaking | 6645 Hz | 11.8  | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 7.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASTRO%20Gaming%20A10/ASTRO%20Gaming%20A10.png)