# Nocs NS300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.0; 31 -1.9; 34 -2.9; 37 -3.6; 41 -4.5; 45 -5.2; 49 -5.8; 54 -6.3; 60 -6.8; 66 -7.2; 72 -7.6; 79 -7.8; 87 -7.6; 96 -7.5; 106 -6.8; 116 -5.9; 128 -6.1; 141 -6.6; 155 -6.5; 170 -5.5; 187 -5.2; 206 -4.1; 227 -2.9; 249 -3.0; 274 -2.9; 302 -4.4; 332 -6.8; 365 -7.8; 402 -8.3; 442 -8.6; 486 -9.1; 535 -9.3; 588 -9.3; 647 -9.7; 712 -10.1; 783 -10.2; 861 -10.5; 947 -10.3; 1042 -9.4; 1146 -8.1; 1261 -7.0; 1387 -6.9; 1526 -5.6; 1678 -5.7; 1846 -5.1; 2031 -5.2; 2234 -5.7; 2457 -6.0; 2703 -7.0; 2973 -7.3; 3270 -7.9; 3597 -6.6; 3957 -5.1; 4353 -3.4; 4788 -5.2; 5267 -5.1; 5793 -3.1; 6373 -4.5; 7010 -7.2; 7711 -7.4; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.34 | 6.6 dB  |
| Peaking | 247 Hz  | 1.16 | 8.1 dB  |
| Peaking | 843 Hz  | 0.14 | -5.5 dB |
| Peaking | 1765 Hz | 1.16 | 6.2 dB  |
| Peaking | 4968 Hz | 1.35 | 5.0 dB  |
| Peaking | 94 Hz   | 1.18 | -1.0 dB |
| Peaking | 117 Hz  | 3.91 | 2.1 dB  |
| Peaking | 6083 Hz | 6.28 | 4.6 dB  |
| Peaking | 6359 Hz | 1.69 | -3.9 dB |
| Peaking | 6976 Hz | 0.7  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS300/Nocs%20NS300.png)