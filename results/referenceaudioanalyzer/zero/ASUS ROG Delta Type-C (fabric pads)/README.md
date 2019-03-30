# ASUS ROG Delta Type-C (fabric pads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.7; 28 -6.0; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.7; 60 -7.8; 66 -8.0; 72 -8.1; 79 -8.1; 87 -8.1; 96 -8.4; 106 -8.4; 116 -8.4; 128 -8.4; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.4; 206 -8.1; 227 -8.1; 249 -7.9; 274 -7.5; 302 -7.2; 332 -6.8; 365 -6.1; 402 -5.0; 442 -3.8; 486 -2.5; 535 -1.0; 588 -0.5; 647 -1.3; 712 -2.0; 783 -2.6; 861 -2.9; 947 -2.5; 1042 -2.0; 1146 -2.2; 1261 -2.3; 1387 -2.6; 1526 -3.0; 1678 -3.2; 1846 -3.4; 2031 -3.1; 2234 -3.0; 2457 -3.7; 2703 -4.1; 2973 -3.7; 3270 -4.1; 3597 -5.1; 3957 -4.9; 4353 -6.4; 4788 -8.3; 5267 -8.4; 5793 -8.9; 6373 -9.9; 7010 -8.0; 7711 -4.7; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASUS ROG Delta Type-C (fabric pads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASUS ROG Delta Type-C (fabric pads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 0.48 | -2.7 dB |
| Peaking | 269 Hz  | 0.53 | -3.0 dB |
| Peaking | 555 Hz  | 2.23 | 4.5 dB  |
| Peaking | 1124 Hz | 0.48 | 2.6 dB  |
| Peaking | 5773 Hz | 2.18 | -5.2 dB |
| Peaking | 19 Hz   | 1.48 | 0.7 dB  |
| Peaking | 4759 Hz | 6.72 | -2.0 dB |
| Peaking | 6613 Hz | 5.15 | -4.6 dB |
| Peaking | 6729 Hz | 1.78 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASUS%20ROG%20Delta%20Type-C%20(fabric%20pads)/ASUS%20ROG%20Delta%20Type-C%20(fabric%20pads).png)