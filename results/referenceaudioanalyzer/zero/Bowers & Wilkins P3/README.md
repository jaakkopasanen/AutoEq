# Bowers & Wilkins P3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.4; 54 -2.1; 60 -2.9; 66 -3.4; 72 -3.7; 79 -4.0; 87 -4.3; 96 -4.5; 106 -4.8; 116 -5.2; 128 -5.6; 141 -5.8; 155 -6.1; 170 -6.1; 187 -6.2; 206 -6.4; 227 -6.7; 249 -6.8; 274 -7.0; 302 -7.1; 332 -7.1; 365 -7.1; 402 -6.9; 442 -6.5; 486 -6.1; 535 -5.8; 588 -5.9; 647 -6.1; 712 -6.3; 783 -6.5; 861 -6.8; 947 -6.4; 1042 -5.5; 1146 -4.5; 1261 -3.7; 1387 -3.1; 1526 -2.3; 1678 -1.8; 1846 -1.9; 2031 -1.7; 2234 -2.0; 2457 -2.8; 2703 -4.3; 2973 -6.1; 3270 -7.5; 3597 -7.8; 3957 -7.1; 4353 -5.3; 4788 -4.5; 5267 -8.0; 5793 -10.9; 6373 -11.9; 7010 -12.9; 7711 -14.6; 8482 -15.3; 9330 -14.0; 10263 -11.1; 11289 -8.7; 12418 -7.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.62 | 6.5 dB  |
| Peaking | 1940 Hz  | 1.33 | 5.6 dB  |
| Peaking | 3401 Hz  | 3.47 | -2.3 dB |
| Peaking | 4662 Hz  | 6.48 | 4.2 dB  |
| Peaking | 8034 Hz  | 1.52 | -9.2 dB |
| Peaking | 297 Hz   | 1.94 | -1.0 dB |
| Peaking | 880 Hz   | 5.67 | -1.2 dB |
| Peaking | 5940 Hz  | 5.4  | -2.1 dB |
| Peaking | 9461 Hz  | 2.39 | -3.3 dB |
| Peaking | 10290 Hz | 0.83 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.8 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bowers%20&%20Wilkins%20P3/Bowers%20&%20Wilkins%20P3.png)