# Monoprice 8323
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -2.2; 45 -3.6; 49 -4.7; 54 -5.8; 60 -6.6; 66 -7.2; 72 -7.5; 79 -7.6; 87 -7.7; 96 -7.8; 106 -7.8; 116 -7.6; 128 -7.8; 141 -7.9; 155 -8.1; 170 -7.6; 187 -8.0; 206 -8.0; 227 -7.9; 249 -7.8; 274 -7.4; 302 -6.8; 332 -6.5; 365 -6.6; 402 -7.0; 442 -7.5; 486 -8.2; 535 -8.5; 588 -8.6; 647 -8.9; 712 -9.2; 783 -9.3; 861 -9.6; 947 -9.8; 1042 -9.6; 1146 -9.5; 1261 -10.1; 1387 -10.1; 1526 -10.8; 1678 -10.8; 1846 -9.7; 2031 -8.3; 2234 -6.7; 2457 -4.4; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -1.5; 5267 -2.9; 5793 -1.7; 6373 -1.0; 7010 -4.0; 7711 -7.5; 8482 -11.2; 9330 -11.8; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice 8323 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8323 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 1.61 | 7.2 dB   |
| Peaking | 2098 Hz | 0.52 | -9.4 dB  |
| Peaking | 3019 Hz | 1.03 | 12.7 dB  |
| Peaking | 6881 Hz | 0.95 | 7.2 dB   |
| Peaking | 8646 Hz | 2.26 | -11.1 dB |
| Peaking | 15 Hz   | 0.28 | 1.2 dB   |
| Peaking | 139 Hz  | 0.31 | -1.8 dB  |
| Peaking | 350 Hz  | 2.08 | 2.1 dB   |
| Peaking | 1130 Hz | 5.04 | 1.1 dB   |
| Peaking | 4240 Hz | 6.41 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208323/Monoprice%208323.png)