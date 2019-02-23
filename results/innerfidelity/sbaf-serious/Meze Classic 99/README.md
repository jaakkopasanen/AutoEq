# Meze Classic 99
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.6; 28 -2.7; 31 -3.7; 34 -4.4; 37 -5.0; 41 -5.5; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.0; 87 -6.9; 96 -7.2; 106 -6.9; 116 -6.8; 128 -7.2; 141 -7.9; 155 -7.9; 170 -7.3; 187 -7.6; 206 -7.7; 227 -7.5; 249 -7.4; 274 -7.3; 302 -7.5; 332 -7.7; 365 -8.0; 402 -8.3; 442 -8.3; 486 -8.8; 535 -9.1; 588 -8.9; 647 -9.0; 712 -9.0; 783 -8.8; 861 -8.8; 947 -8.5; 1042 -8.1; 1146 -8.2; 1261 -8.4; 1387 -8.6; 1526 -8.8; 1678 -8.8; 1846 -8.5; 2031 -7.9; 2234 -7.6; 2457 -6.9; 2703 -6.1; 2973 -5.4; 3270 -4.0; 3597 -2.8; 3957 -1.7; 4353 -5.4; 4788 -5.0; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Classic 99 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classic 99 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.29 | 6.5 dB  |
| Peaking | 131 Hz  |  0.11 | -0.7 dB |
| Peaking | 1763 Hz |  0.22 | -2.0 dB |
| Peaking | 3598 Hz |  2.62 | 5.4 dB  |
| Peaking | 5893 Hz |  2.96 | 7.5 dB  |
| Peaking | 301 Hz  |  1.75 | 1.0 dB  |
| Peaking | 566 Hz  |  0.39 | -0.6 dB |
| Peaking | 1079 Hz |  3.58 | 1.1 dB  |
| Peaking | 2577 Hz |  4.6  | 0.8 dB  |
| Peaking | 4546 Hz | 14.44 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classic%2099/Meze%20Classic%2099.png)