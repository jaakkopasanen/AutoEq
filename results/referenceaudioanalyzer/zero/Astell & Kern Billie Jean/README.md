# Astell & Kern Billie Jean
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.8; 25 -13.8; 28 -13.9; 31 -13.9; 34 -14.0; 37 -14.0; 41 -14.0; 45 -14.0; 49 -13.9; 54 -13.7; 60 -13.7; 66 -13.7; 72 -13.7; 79 -13.7; 87 -13.5; 96 -13.3; 106 -13.1; 116 -12.8; 128 -12.6; 141 -12.3; 155 -12.0; 170 -11.7; 187 -11.4; 206 -11.1; 227 -10.6; 249 -10.2; 274 -10.0; 302 -9.7; 332 -9.2; 365 -8.6; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.8; 588 -6.3; 647 -5.9; 712 -5.5; 783 -5.1; 861 -4.9; 947 -4.9; 1042 -4.9; 1146 -5.1; 1261 -5.6; 1387 -6.3; 1526 -7.0; 1678 -7.2; 1846 -6.5; 2031 -4.9; 2234 -3.9; 2457 -4.2; 2703 -3.9; 2973 -2.5; 3270 -1.2; 3597 -1.4; 3957 -2.3; 4353 -2.0; 4788 -1.5; 5267 -2.2; 5793 -1.9; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Billie Jean GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Billie Jean ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.14 | -8.1 dB |
| Peaking | 783 Hz  | 1.76 | 1.8 dB  |
| Peaking | 3437 Hz | 2.14 | 4.1 dB  |
| Peaking | 6329 Hz | 1.74 | 6.2 dB  |
| Peaking | 7774 Hz | 2.07 | -3.5 dB |
| Peaking | 1133 Hz | 3.08 | 1.0 dB  |
| Peaking | 1673 Hz | 2.3  | -2.1 dB |
| Peaking | 2160 Hz | 4.93 | 1.7 dB  |
| Peaking | 4717 Hz | 8.61 | 1.2 dB  |
| Peaking | 5581 Hz | 9.73 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Astell%20&%20Kern%20Billie%20Jean/Astell%20&%20Kern%20Billie%20Jean.png)