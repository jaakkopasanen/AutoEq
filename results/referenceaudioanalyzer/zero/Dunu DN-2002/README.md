# Dunu DN-2002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.3; 28 -2.2; 31 -2.9; 34 -3.5; 37 -4.0; 41 -4.5; 45 -5.1; 49 -5.5; 54 -6.0; 60 -6.5; 66 -6.8; 72 -7.1; 79 -7.4; 87 -7.7; 96 -7.9; 106 -8.1; 116 -8.2; 128 -8.4; 141 -8.5; 155 -8.8; 170 -9.1; 187 -9.3; 206 -9.4; 227 -9.4; 249 -9.7; 274 -9.7; 302 -9.7; 332 -9.7; 365 -9.6; 402 -9.4; 442 -9.4; 486 -9.2; 535 -9.0; 588 -8.8; 647 -8.6; 712 -8.3; 783 -7.9; 861 -7.5; 947 -7.1; 1042 -6.6; 1146 -6.2; 1261 -5.9; 1387 -5.6; 1526 -5.3; 1678 -5.1; 1846 -4.9; 2031 -4.9; 2234 -4.9; 2457 -4.9; 2703 -5.4; 2973 -6.5; 3270 -7.3; 3597 -6.6; 3957 -5.2; 4353 -4.8; 4788 -4.2; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN-2002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN-2002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.96 | 6.0 dB  |
| Peaking | 289 Hz  | 0.37 | -3.3 dB |
| Peaking | 1660 Hz | 1.24 | 2.2 dB  |
| Peaking | 6028 Hz | 2.71 | 7.1 dB  |
| Peaking | 7643 Hz | 1.77 | -1.6 dB |
| Peaking | 3126 Hz | 1.78 | 1.6 dB  |
| Peaking | 3245 Hz | 4.02 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DN-2002/Dunu%20DN-2002.png)