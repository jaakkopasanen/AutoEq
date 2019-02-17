# Piaton PS 210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.1; 54 -1.6; 60 -2.3; 66 -2.9; 72 -3.5; 79 -4.1; 87 -4.6; 96 -5.1; 106 -5.6; 116 -6.0; 128 -6.5; 141 -6.9; 155 -7.2; 170 -7.6; 187 -7.8; 206 -8.1; 227 -8.2; 249 -8.4; 274 -8.4; 302 -8.3; 332 -8.4; 365 -8.4; 402 -8.4; 442 -8.7; 486 -8.4; 535 -8.2; 588 -8.2; 647 -8.2; 712 -8.3; 783 -7.9; 861 -7.5; 947 -6.9; 1042 -6.3; 1146 -5.6; 1261 -5.2; 1387 -5.0; 1526 -5.3; 1678 -5.9; 1846 -7.0; 2031 -8.5; 2234 -10.2; 2457 -10.5; 2703 -7.5; 2973 -3.7; 3270 -0.6; 3597 -0.5; 3957 -1.8; 4353 -5.4; 4788 -4.9; 5267 -0.9; 5793 -1.8; 6373 -5.9; 7010 -7.6; 7711 -12.4; 8482 -13.0; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Piaton PS 210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.85 | 7.0 dB  |
| Peaking | 2399 Hz |  4.1  | -5.9 dB |
| Peaking | 3420 Hz |  3.1  | 7.2 dB  |
| Peaking | 5528 Hz |  5.81 | 6.3 dB  |
| Peaking | 8080 Hz |  4.99 | -8.3 dB |
| Peaking | 70 Hz   |  1.23 | 1.4 dB  |
| Peaking | 373 Hz  |  0.34 | -2.2 dB |
| Peaking | 1327 Hz |  2.05 | 2.7 dB  |
| Peaking | 4538 Hz | 12.36 | -1.8 dB |
| Peaking | 9725 Hz |  8.71 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Piaton%20PS%20210/Piaton%20PS%20210.png)