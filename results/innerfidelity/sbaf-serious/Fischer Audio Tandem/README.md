# Fischer Audio Tandem
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.0; 41 -1.7; 45 -2.3; 49 -2.8; 54 -3.5; 60 -4.3; 66 -5.0; 72 -5.7; 79 -6.4; 87 -7.1; 96 -7.9; 106 -8.4; 116 -8.8; 128 -9.4; 141 -9.8; 155 -10.1; 170 -10.4; 187 -10.6; 206 -10.7; 227 -10.8; 249 -10.9; 274 -10.8; 302 -10.7; 332 -10.7; 365 -10.5; 402 -10.3; 442 -10.0; 486 -9.9; 535 -9.7; 588 -9.2; 647 -9.0; 712 -9.0; 783 -8.8; 861 -8.7; 947 -8.7; 1042 -9.1; 1146 -9.3; 1261 -9.1; 1387 -8.9; 1526 -8.7; 1678 -8.6; 1846 -7.8; 2031 -6.7; 2234 -5.5; 2457 -3.8; 2703 -2.1; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -2.5; 4353 -6.2; 4788 -5.9; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Tandem GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Tandem ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 29 Hz   |  0.46 | 6.9 dB  |
| Peaking | 202 Hz  |  0.35 | -4.9 dB |
| Peaking | 1454 Hz |  1.22 | -2.4 dB |
| Peaking | 3119 Hz |  2.22 | 7.1 dB  |
| Peaking | 6010 Hz |  4.37 | 6.3 dB  |
| Peaking | 2507 Hz | 10.57 | 0.7 dB  |
| Peaking | 3826 Hz |  7.16 | 3.1 dB  |
| Peaking | 4499 Hz |  3.29 | -3.1 dB |
| Peaking | 5294 Hz |  6.94 | 2.6 dB  |
| Peaking | 8283 Hz |  5.12 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20Tandem/Fischer%20Audio%20Tandem.png)