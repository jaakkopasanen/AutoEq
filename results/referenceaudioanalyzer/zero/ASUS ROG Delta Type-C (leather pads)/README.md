# ASUS ROG Delta Type-C (leather pads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.5; 28 -5.7; 31 -5.9; 34 -6.0; 37 -6.2; 41 -6.4; 45 -6.5; 49 -6.6; 54 -6.7; 60 -6.8; 66 -7.0; 72 -7.0; 79 -7.0; 87 -7.3; 96 -7.3; 106 -7.3; 116 -7.3; 128 -7.3; 141 -7.3; 155 -7.2; 170 -7.0; 187 -7.0; 206 -7.3; 227 -7.3; 249 -7.0; 274 -6.9; 302 -6.6; 332 -6.6; 365 -6.2; 402 -5.5; 442 -4.5; 486 -3.2; 535 -1.8; 588 -1.1; 647 -1.5; 712 -2.3; 783 -3.2; 861 -3.5; 947 -3.2; 1042 -2.5; 1146 -1.9; 1261 -1.5; 1387 -1.4; 1526 -1.7; 1678 -2.0; 1846 -2.4; 2031 -3.0; 2234 -3.9; 2457 -4.4; 2703 -4.1; 2973 -3.4; 3270 -3.5; 3597 -2.7; 3957 -0.5; 4353 -2.0; 4788 -3.4; 5267 -3.3; 5793 -5.4; 6373 -9.0; 7010 -8.8; 7711 -4.6; 8482 -4.0; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASUS ROG Delta Type-C (leather pads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASUS ROG Delta Type-C (leather pads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 0.26 | -3.9 dB |
| Peaking | 320 Hz  | 1.25 | -3.2 dB |
| Peaking | 529 Hz  | 0.46 | 4.5 dB  |
| Peaking | 4063 Hz | 5.24 | 3.5 dB  |
| Peaking | 6650 Hz | 5.28 | -6.2 dB |
| Peaking | 422 Hz  | 3.6  | -1.0 dB |
| Peaking | 585 Hz  | 2.99 | 1.8 dB  |
| Peaking | 865 Hz  | 1.93 | -3.3 dB |
| Peaking | 1269 Hz | 0.76 | 1.9 dB  |
| Peaking | 2427 Hz | 2.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASUS%20ROG%20Delta%20Type-C%20(leather%20pads)/ASUS%20ROG%20Delta%20Type-C%20(leather%20pads).png)