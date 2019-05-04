# Sony WH-H900N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.6; 25 -4.5; 28 -4.3; 31 -4.2; 34 -4.1; 37 -4.0; 41 -4.0; 45 -4.0; 49 -3.9; 54 -4.0; 60 -4.0; 66 -4.1; 72 -4.3; 79 -4.4; 87 -4.7; 96 -4.9; 106 -5.1; 116 -5.3; 128 -5.3; 141 -5.3; 155 -5.1; 170 -4.8; 187 -4.5; 206 -4.1; 227 -3.7; 249 -3.3; 274 -3.1; 302 -2.9; 332 -2.6; 365 -2.3; 402 -1.9; 442 -1.6; 486 -1.7; 535 -1.8; 588 -2.2; 647 -2.3; 712 -2.4; 783 -1.2; 861 -1.5; 947 -3.0; 1042 -3.6; 1146 -4.0; 1261 -4.0; 1387 -3.7; 1526 -4.6; 1678 -5.4; 1846 -5.9; 2031 -6.0; 2234 -5.5; 2457 -3.7; 2703 -4.1; 2973 -6.3; 3270 -3.8; 3597 -1.8; 3957 -7.2; 4353 -7.0; 4788 -3.2; 5267 -3.8; 5793 -2.8; 6373 -0.5; 7010 -1.1; 7711 -3.4; 8482 -5.4; 9330 -3.6; 10263 -3.6; 11289 -4.1; 12418 -3.7; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-H900N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-H900N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 466 Hz  |  2.17 | 2.2 dB  |
| Peaking | 819 Hz  |  5.43 | 2.5 dB  |
| Peaking | 1928 Hz |  2.51 | -2.6 dB |
| Peaking | 4140 Hz | 10.84 | -5.6 dB |
| Peaking | 6584 Hz |  7.35 | 4.4 dB  |
| Peaking | 14 Hz   |  0.8  | -1.9 dB |
| Peaking | 125 Hz  |  1.43 | -1.9 dB |
| Peaking | 3011 Hz | 10.48 | -2.7 dB |
| Peaking | 3533 Hz | 10.68 | 3.0 dB  |
| Peaking | 8385 Hz |  9.28 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-H900N/Sony%20WH-H900N.png)