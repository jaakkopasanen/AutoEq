# Denon AH-D7000 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.2; 28 -2.5; 31 -3.8; 34 -4.8; 37 -5.3; 41 -5.4; 45 -5.6; 49 -6.2; 54 -6.3; 60 -6.0; 66 -6.1; 72 -6.2; 79 -6.3; 87 -6.3; 96 -6.1; 106 -5.9; 116 -5.7; 128 -5.7; 141 -5.7; 155 -5.6; 170 -5.3; 187 -5.3; 206 -5.2; 227 -4.9; 249 -4.7; 274 -4.3; 302 -3.9; 332 -3.5; 365 -3.3; 402 -3.1; 442 -3.6; 486 -4.3; 535 -5.2; 588 -5.9; 647 -6.2; 712 -6.8; 783 -7.4; 861 -6.6; 947 -6.0; 1042 -6.5; 1146 -6.2; 1261 -5.6; 1387 -5.2; 1526 -5.2; 1678 -4.7; 1846 -4.3; 2031 -4.5; 2234 -4.0; 2457 -3.2; 2703 -2.8; 2973 -3.8; 3270 -5.4; 3597 -6.0; 3957 -5.6; 4353 -5.6; 4788 -8.2; 5267 -7.0; 5793 -7.9; 6373 -8.9; 7010 -8.5; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.83 | 6.2 dB  |
| Peaking | 486 Hz  |  0.68 | 4.8 dB  |
| Peaking | 674 Hz  |  1.31 | -4.3 dB |
| Peaking | 2518 Hz |  1.79 | 3.3 dB  |
| Peaking | 6343 Hz |  2.74 | -2.7 dB |
| Peaking | 1800 Hz |  3.88 | 0.7 dB  |
| Peaking | 2094 Hz |  6.53 | -0.9 dB |
| Peaking | 4798 Hz | 16.38 | -1.7 dB |
| Peaking | 8339 Hz |  6.88 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000%20(balanced)/Denon%20AH-D7000%20(balanced).png)