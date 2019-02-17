# Monoprice 8320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.0; 87 -1.4; 96 -2.0; 106 -2.4; 116 -2.6; 128 -3.0; 141 -3.5; 155 -3.9; 170 -4.1; 187 -4.4; 206 -4.7; 227 -4.9; 249 -5.1; 274 -5.3; 302 -5.4; 332 -5.5; 365 -5.6; 402 -5.7; 442 -5.5; 486 -5.7; 535 -5.6; 588 -5.3; 647 -5.3; 712 -5.6; 783 -5.7; 861 -5.9; 947 -5.9; 1042 -6.8; 1146 -7.6; 1261 -8.5; 1387 -9.5; 1526 -10.8; 1678 -12.1; 1846 -13.5; 2031 -15.0; 2234 -16.3; 2457 -15.1; 2703 -12.1; 2973 -8.6; 3270 -5.7; 3597 -5.1; 3957 -6.5; 4353 -9.5; 4788 -7.7; 5267 -8.0; 5793 -4.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice 8320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.31 | 6.4 dB   |
| Peaking | 700 Hz  | 1.67 | 1.3 dB   |
| Peaking | 2125 Hz | 2.12 | -10.2 dB |
| Peaking | 5506 Hz | 5.38 | -5.0 dB  |
| Peaking | 6152 Hz | 4.36 | 8.2 dB   |
| Peaking | 922 Hz  | 8.36 | 0.8 dB   |
| Peaking | 1483 Hz | 4.57 | -1.2 dB  |
| Peaking | 2569 Hz | 5.42 | -2.6 dB  |
| Peaking | 3479 Hz | 2.69 | 3.8 dB   |
| Peaking | 4369 Hz | 6.87 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208320/Monoprice%208320.png)