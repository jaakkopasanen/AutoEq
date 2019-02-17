# Focal Spirit One 2013 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.8; 25 -9.7; 28 -9.5; 31 -9.4; 34 -9.2; 37 -9.1; 41 -8.8; 45 -8.6; 49 -8.4; 54 -8.3; 60 -8.3; 66 -8.0; 72 -7.4; 79 -6.9; 87 -8.2; 96 -10.8; 106 -11.1; 116 -10.6; 128 -10.4; 141 -10.8; 155 -10.5; 170 -10.3; 187 -10.2; 206 -9.8; 227 -9.3; 249 -8.7; 274 -7.9; 302 -7.9; 332 -7.9; 365 -8.3; 402 -8.8; 442 -8.8; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.9; 712 -7.7; 783 -7.1; 861 -7.0; 947 -6.7; 1042 -6.3; 1146 -5.9; 1261 -5.7; 1387 -5.8; 1526 -6.0; 1678 -5.9; 1846 -5.7; 2031 -5.1; 2234 -4.5; 2457 -3.6; 2703 -3.1; 2973 -3.1; 3270 -3.6; 3597 -4.5; 3957 -3.0; 4353 -6.1; 4788 -6.3; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One 2013 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One 2013 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.96 | -3.4 dB |
| Peaking | 140 Hz  |  1.01 | -4.4 dB |
| Peaking | 487 Hz  |  1.67 | -2.1 dB |
| Peaking | 2810 Hz |  1.79 | 3.4 dB  |
| Peaking | 5975 Hz |  4.16 | 6.5 dB  |
| Peaking | 80 Hz   |  5.17 | 2.2 dB  |
| Peaking | 97 Hz   |  6.13 | -2.0 dB |
| Peaking | 1222 Hz |  5.58 | 0.7 dB  |
| Peaking | 3927 Hz | 18.12 | 1.9 dB  |
| Peaking | 9707 Hz |  2.1  | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%202013%20B/Focal%20Spirit%20One%202013%20B.png)