# Bowers & Wilkins P5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.4; 34 -2.7; 37 -3.1; 41 -3.5; 45 -3.9; 49 -4.3; 54 -4.7; 60 -5.2; 66 -5.6; 72 -6.1; 79 -6.5; 87 -6.9; 96 -7.4; 106 -7.8; 116 -8.1; 128 -8.4; 141 -8.7; 155 -8.7; 170 -8.7; 187 -8.5; 206 -8.2; 227 -7.7; 249 -7.4; 274 -7.1; 302 -6.9; 332 -6.2; 365 -5.3; 402 -4.6; 442 -4.2; 486 -4.1; 535 -4.2; 588 -4.6; 647 -5.0; 712 -5.2; 783 -5.0; 861 -4.8; 947 -4.4; 1042 -4.1; 1146 -3.7; 1261 -3.3; 1387 -3.1; 1526 -2.9; 1678 -2.9; 1846 -3.0; 2031 -3.8; 2234 -5.0; 2457 -6.0; 2703 -6.8; 2973 -7.9; 3270 -8.8; 3597 -9.0; 3957 -8.1; 4353 -7.2; 4788 -6.7; 5267 -6.4; 5793 -7.0; 6373 -8.6; 7010 -11.4; 7711 -13.1; 8482 -11.8; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.24 | 5.9 dB  |
| Peaking | 483 Hz   | 3.22 | 2.3 dB  |
| Peaking | 1542 Hz  | 1.03 | 3.9 dB  |
| Peaking | 3294 Hz  | 2.58 | -3.4 dB |
| Peaking | 7747 Hz  | 3.64 | -7.4 dB |
| Peaking | 51 Hz    | 1.8  | 1.2 dB  |
| Peaking | 153 Hz   | 1    | -2.5 dB |
| Peaking | 391 Hz   | 4.19 | 1.2 dB  |
| Peaking | 5294 Hz  | 6.57 | 1.0 dB  |
| Peaking | 10074 Hz | 6.77 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bowers%20&%20Wilkins%20P5/Bowers%20&%20Wilkins%20P5.png)