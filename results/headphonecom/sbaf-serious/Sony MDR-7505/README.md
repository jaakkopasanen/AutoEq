# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.5; 87 -1.5; 96 -1.2; 106 -2.6; 116 -3.7; 128 -4.6; 141 -5.3; 155 -5.9; 170 -6.2; 187 -6.7; 206 -6.8; 227 -6.3; 249 -5.6; 274 -5.5; 302 -5.9; 332 -7.0; 365 -8.3; 402 -8.1; 442 -7.8; 486 -7.8; 535 -7.9; 588 -8.0; 647 -8.3; 712 -7.5; 783 -7.0; 861 -7.6; 947 -8.4; 1042 -8.0; 1146 -7.6; 1261 -8.0; 1387 -8.5; 1526 -9.0; 1678 -8.5; 1846 -8.0; 2031 -7.6; 2234 -7.3; 2457 -7.1; 2703 -6.2; 2973 -7.2; 3270 -7.6; 3597 -7.7; 3957 -7.8; 4353 -8.5; 4788 -7.7; 5267 -5.9; 5793 -6.3; 6373 -7.4; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 58 Hz   |  0.15 | 6.6 dB  |
| Peaking | 165 Hz  |  1.28 | -4.9 dB |
| Peaking | 441 Hz  |  0.85 | -3.8 dB |
| Peaking | 1494 Hz |  1.59 | -2.1 dB |
| Peaking | 4258 Hz |  4.71 | -1.9 dB |
| Peaking | 289 Hz  |  5.65 | 1.0 dB  |
| Peaking | 368 Hz  |  3.7  | -1.1 dB |
| Peaking | 451 Hz  |  4.24 | 0.7 dB  |
| Peaking | 3367 Hz |  8.46 | -0.8 dB |
| Peaking | 7008 Hz | 11.82 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)