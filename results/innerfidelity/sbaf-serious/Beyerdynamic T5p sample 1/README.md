# Beyerdynamic T5p sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.4; 25 -7.3; 28 -7.0; 31 -6.7; 34 -6.4; 37 -6.1; 41 -5.8; 45 -5.5; 49 -5.4; 54 -5.1; 60 -4.5; 66 -3.7; 72 -3.3; 79 -4.2; 87 -6.2; 96 -8.2; 106 -8.9; 116 -9.0; 128 -8.7; 141 -8.1; 155 -7.1; 170 -6.8; 187 -7.2; 206 -6.7; 227 -6.1; 249 -5.6; 274 -5.1; 302 -4.8; 332 -4.5; 365 -4.3; 402 -4.2; 442 -4.0; 486 -4.2; 535 -3.9; 588 -3.0; 647 -0.9; 712 -3.8; 783 -4.5; 861 -5.0; 947 -5.2; 1042 -6.6; 1146 -6.1; 1261 -6.6; 1387 -8.8; 1526 -7.3; 1678 -7.4; 1846 -6.7; 2031 -7.2; 2234 -8.6; 2457 -7.1; 2703 -5.6; 2973 -4.8; 3270 -3.4; 3597 -2.5; 3957 -2.3; 4353 -3.4; 4788 -0.5; 5267 -0.8; 5793 -5.5; 6373 -6.4; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 74 Hz   |  1.82 | 5.4 dB  |
| Peaking | 103 Hz  |  1.46 | -4.6 dB |
| Peaking | 376 Hz  |  1.44 | 2.4 dB  |
| Peaking | 651 Hz  |  4.39 | 4.8 dB  |
| Peaking | 4608 Hz |  2.2  | 5.6 dB  |
| Peaking | 21 Hz   |  1.95 | -1.0 dB |
| Peaking | 1392 Hz |  6.61 | -2.5 dB |
| Peaking | 2265 Hz |  5.62 | -3.0 dB |
| Peaking | 3505 Hz |  2.7  | 1.9 dB  |
| Peaking | 4321 Hz | 11.13 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sample%201/Beyerdynamic%20T5p%20sample%201.png)