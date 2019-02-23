# Stax SR-007 SZ3-1576
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -2.0; 31 -3.5; 34 -4.7; 37 -5.6; 41 -6.2; 45 -6.3; 49 -6.1; 54 -5.5; 60 -5.3; 66 -6.2; 72 -7.6; 79 -7.6; 87 -7.1; 96 -7.0; 106 -7.0; 116 -6.9; 128 -7.0; 141 -6.9; 155 -7.0; 170 -7.1; 187 -7.1; 206 -7.2; 227 -7.1; 249 -7.2; 274 -7.2; 302 -7.4; 332 -7.4; 365 -7.5; 402 -7.6; 442 -7.7; 486 -7.9; 535 -6.5; 588 -6.5; 647 -7.8; 712 -8.6; 783 -9.0; 861 -9.8; 947 -10.2; 1042 -9.7; 1146 -9.4; 1261 -6.4; 1387 -5.0; 1526 -9.3; 1678 -10.0; 1846 -7.6; 2031 -5.9; 2234 -4.4; 2457 -3.6; 2703 -3.3; 2973 -1.6; 3270 -0.6; 3597 -0.7; 3957 -1.4; 4353 -3.9; 4788 -6.3; 5267 -5.4; 5793 -4.2; 6373 -6.3; 7010 -4.9; 7711 -6.2; 8482 -6.9; 9330 -9.7; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 SZ3-1576 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 SZ3-1576 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  2.19 | 6.6 dB  |
| Peaking | 912 Hz  |  2.12 | -3.9 dB |
| Peaking | 1665 Hz |  7.56 | -4.5 dB |
| Peaking | 3332 Hz |  1.78 | 6.2 dB  |
| Peaking | 9492 Hz |  6.17 | -3.9 dB |
| Peaking | 78 Hz   |  5.36 | -1.3 dB |
| Peaking | 318 Hz  |  0.72 | -0.9 dB |
| Peaking | 566 Hz  | 10.35 | 2.1 dB  |
| Peaking | 4879 Hz |  5.18 | -4.5 dB |
| Peaking | 5048 Hz |  2.28 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007%20SZ3-1576/Stax%20SR-007%20SZ3-1576.png)