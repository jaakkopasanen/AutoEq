# Stax SR-207 EP507 Leather Pads SerNum SB2 2217
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.6; 45 -2.7; 49 -2.7; 54 -2.7; 60 -2.9; 66 -3.4; 72 -3.5; 79 -3.7; 87 -3.9; 96 -4.2; 106 -4.4; 116 -4.5; 128 -4.8; 141 -4.9; 155 -5.1; 170 -5.2; 187 -5.3; 206 -5.2; 227 -5.2; 249 -5.4; 274 -5.3; 302 -5.4; 332 -5.2; 365 -5.2; 402 -5.3; 442 -5.2; 486 -5.4; 535 -5.6; 588 -5.4; 647 -5.4; 712 -5.8; 783 -5.9; 861 -6.4; 947 -6.8; 1042 -7.5; 1146 -8.0; 1261 -8.8; 1387 -9.9; 1526 -10.6; 1678 -10.8; 1846 -9.2; 2031 -6.7; 2234 -4.5; 2457 -3.4; 2703 -5.2; 2973 -5.6; 3270 -6.3; 3597 -5.6; 3957 -4.4; 4353 -5.0; 4788 -7.3; 5267 -5.7; 5793 -7.1; 6373 -6.8; 7010 -4.2; 7711 -5.9; 8482 -9.4; 9330 -10.4; 10263 -7.0; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.6; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-207 EP507 Leather Pads SerNum SB2 2217 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-207 EP507 Leather Pads SerNum SB2 2217 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.15 | 5.0 dB  |
| Peaking | 503 Hz  | 0.65 | 0.9 dB  |
| Peaking | 1630 Hz | 1.68 | -6.0 dB |
| Peaking | 2320 Hz | 2.43 | 4.6 dB  |
| Peaking | 9110 Hz | 6.15 | -5.2 dB |
| Peaking | 12 Hz   | 2.11 | 1.3 dB  |
| Peaking | 4128 Hz | 6.1  | 4.0 dB  |
| Peaking | 4229 Hz | 2.63 | -1.7 dB |
| Peaking | 6176 Hz | 8.69 | -1.6 dB |
| Peaking | 7004 Hz | 7.12 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-207%20EP507%20Leather%20Pads%20SerNum%20SB2%202217/Stax%20SR-207%20EP507%20Leather%20Pads%20SerNum%20SB2%202217.png)