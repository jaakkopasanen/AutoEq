# Beyerdynamic T5p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.2; 28 -6.2; 31 -6.1; 34 -6.0; 37 -6.0; 41 -5.8; 45 -5.7; 49 -5.6; 54 -5.4; 60 -5.1; 66 -4.7; 72 -4.4; 79 -4.6; 87 -5.8; 96 -7.3; 106 -8.7; 116 -9.2; 128 -9.6; 141 -9.4; 155 -8.5; 170 -7.7; 187 -8.5; 206 -8.1; 227 -7.4; 249 -6.9; 274 -6.3; 302 -5.8; 332 -5.5; 365 -5.3; 402 -5.3; 442 -5.1; 486 -5.4; 535 -5.4; 588 -4.4; 647 -1.8; 712 -4.5; 783 -4.8; 861 -5.9; 947 -6.1; 1042 -6.4; 1146 -6.9; 1261 -8.0; 1387 -8.5; 1526 -8.6; 1678 -8.9; 1846 -8.4; 2031 -8.3; 2234 -9.5; 2457 -7.5; 2703 -5.8; 2973 -5.0; 3270 -3.8; 3597 -2.8; 3957 -1.8; 4353 -4.1; 4788 -0.5; 5267 -1.0; 5793 -5.7; 6373 -6.4; 7010 -4.2; 7711 -6.3; 8482 -8.7; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 77 Hz   |  1.31 | 3.9 dB  |
| Peaking | 118 Hz  |  1.31 | -4.8 dB |
| Peaking | 646 Hz  |  1.69 | 3.5 dB  |
| Peaking | 1819 Hz |  1.1  | -3.2 dB |
| Peaking | 4211 Hz |  1.56 | 5.5 dB  |
| Peaking | 345 Hz  |  1.86 | 2.9 dB  |
| Peaking | 349 Hz  |  1.14 | -1.9 dB |
| Peaking | 5092 Hz |  9.3  | 3.1 dB  |
| Peaking | 5968 Hz | 10.01 | -2.6 dB |
| Peaking | 8646 Hz |  7.36 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)