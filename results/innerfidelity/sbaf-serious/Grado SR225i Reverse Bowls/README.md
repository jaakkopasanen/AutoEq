# Grado SR225i Reverse Bowls
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -2.0; 54 -3.0; 60 -3.9; 66 -4.7; 72 -5.4; 79 -6.1; 87 -6.7; 96 -7.1; 106 -7.3; 116 -7.3; 128 -7.4; 141 -7.4; 155 -7.4; 170 -7.2; 187 -7.1; 206 -6.8; 227 -6.6; 249 -6.5; 274 -6.0; 302 -6.1; 332 -6.0; 365 -5.7; 402 -5.7; 442 -5.5; 486 -5.4; 535 -5.2; 588 -4.8; 647 -4.7; 712 -4.8; 783 -4.6; 861 -4.8; 947 -4.9; 1042 -4.9; 1146 -5.1; 1261 -5.6; 1387 -6.5; 1526 -7.6; 1678 -8.2; 1846 -9.7; 2031 -12.7; 2234 -11.6; 2457 -8.7; 2703 -6.6; 2973 -5.9; 3270 -4.5; 3597 -5.9; 3957 -4.5; 4353 -2.7; 4788 -2.9; 5267 -4.5; 5793 -2.9; 6373 -4.8; 7010 -8.5; 7711 -9.4; 8482 -10.4; 9330 -11.0; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Reverse Bowls GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Reverse Bowls ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  1.1  | 7.1 dB  |
| Peaking | 785 Hz  |  1.08 | 2.0 dB  |
| Peaking | 2089 Hz |  3.2  | -7.7 dB |
| Peaking | 5873 Hz |  0.76 | 5.3 dB  |
| Peaking | 8220 Hz |  1.76 | -8.1 dB |
| Peaking | 49 Hz   |  2.83 | 1.7 dB  |
| Peaking | 119 Hz  |  1.23 | -1.6 dB |
| Peaking | 3684 Hz | 10.8  | -1.9 dB |
| Peaking | 5071 Hz |  0.73 | 0.4 dB  |
| Peaking | 7052 Hz | 11.73 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Reverse%20Bowls/Grado%20SR225i%20Reverse%20Bowls.png)