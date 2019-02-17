# Teac CT-H02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.6; 28 -4.8; 31 -4.9; 34 -4.9; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.9; 54 -5.0; 60 -5.1; 66 -5.2; 72 -5.3; 79 -5.6; 87 -5.7; 96 -5.8; 106 -6.1; 116 -6.5; 128 -6.3; 141 -5.8; 155 -6.6; 170 -6.3; 187 -6.9; 206 -7.7; 227 -8.1; 249 -8.0; 274 -7.8; 302 -8.0; 332 -8.0; 365 -7.9; 402 -7.9; 442 -7.8; 486 -7.9; 535 -7.9; 588 -7.7; 647 -7.8; 712 -7.5; 783 -7.1; 861 -7.2; 947 -6.7; 1042 -6.7; 1146 -6.9; 1261 -6.7; 1387 -6.7; 1526 -6.8; 1678 -6.9; 1846 -6.2; 2031 -5.0; 2234 -4.1; 2457 -2.1; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -1.3; 4788 -0.5; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.9; 8482 -12.1; 9330 -12.8; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.13 | 1.9 dB   |
| Peaking | 373 Hz  |  0.33 | -1.7 dB  |
| Peaking | 3002 Hz |  2.08 | 4.5 dB   |
| Peaking | 5943 Hz |  0.94 | 7.2 dB   |
| Peaking | 8776 Hz |  2.51 | -11.0 dB |
| Peaking | 179 Hz  |  2.93 | 1.5 dB   |
| Peaking | 206 Hz  |  2.29 | -1.4 dB  |
| Peaking | 1541 Hz |  0.72 | 0.8 dB   |
| Peaking | 1687 Hz |  2.47 | -1.8 dB  |
| Peaking | 5326 Hz | 10.97 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)