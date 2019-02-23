# Yuin PK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.6; 72 -2.6; 79 -3.5; 87 -4.4; 96 -5.0; 106 -5.1; 116 -5.3; 128 -5.4; 141 -5.6; 155 -5.5; 170 -5.4; 187 -5.6; 206 -5.4; 227 -5.5; 249 -5.5; 274 -5.6; 302 -5.7; 332 -5.7; 365 -5.7; 402 -5.9; 442 -5.6; 486 -6.0; 535 -6.3; 588 -6.0; 647 -6.3; 712 -6.6; 783 -6.6; 861 -6.9; 947 -7.2; 1042 -7.4; 1146 -7.6; 1261 -8.3; 1387 -9.1; 1526 -9.7; 1678 -10.3; 1846 -10.2; 2031 -9.4; 2234 -8.4; 2457 -6.8; 2703 -6.0; 2973 -4.1; 3270 -3.0; 3597 -2.5; 3957 -3.8; 4353 -6.3; 4788 -7.8; 5267 -7.9; 5793 -9.1; 6373 -8.3; 7010 -7.5; 7711 -7.3; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.6  | 6.7 dB  |
| Peaking | 375 Hz  |  0.97 | 0.8 dB  |
| Peaking | 1757 Hz |  1.59 | -4.3 dB |
| Peaking | 3481 Hz |  2.13 | 5.6 dB  |
| Peaking | 5415 Hz |  1.75 | -3.1 dB |
| Peaking | 37 Hz   |  2.83 | -1.1 dB |
| Peaking | 59 Hz   |  2.94 | 1.5 dB  |
| Peaking | 96 Hz   |  2.32 | -0.9 dB |
| Peaking | 4529 Hz | 11.33 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)