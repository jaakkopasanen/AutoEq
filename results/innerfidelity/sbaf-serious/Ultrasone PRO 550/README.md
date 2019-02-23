# Ultrasone PRO 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.7; 31 -4.1; 34 -5.2; 37 -6.0; 41 -6.7; 45 -7.2; 49 -7.3; 54 -7.4; 60 -6.7; 66 -6.8; 72 -7.7; 79 -7.9; 87 -8.1; 96 -8.0; 106 -7.6; 116 -7.4; 128 -7.1; 141 -6.7; 155 -6.1; 170 -5.2; 187 -4.2; 206 -3.0; 227 -1.7; 249 -0.9; 274 -3.2; 302 -2.6; 332 -4.9; 365 -7.4; 402 -8.7; 442 -9.0; 486 -9.2; 535 -9.2; 588 -8.2; 647 -6.6; 712 -8.0; 783 -8.6; 861 -9.2; 947 -9.6; 1042 -9.6; 1146 -9.0; 1261 -9.2; 1387 -9.3; 1526 -10.2; 1678 -9.6; 1846 -7.8; 2031 -5.5; 2234 -5.5; 2457 -7.9; 2703 -6.0; 2973 -5.8; 3270 -7.5; 3597 -7.6; 3957 -6.3; 4353 -2.5; 4788 -3.2; 5267 -3.0; 5793 -3.6; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -10.0; 9330 -10.2; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -9.9; 18182 -11.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.71 | 6.7 dB  |
| Peaking | 240 Hz   | 1.89 | 7.7 dB  |
| Peaking | 2582 Hz  | 0.01 | -2.3 dB |
| Peaking | 4808 Hz  | 1.74 | 5.5 dB  |
| Peaking | 6415 Hz  | 5.85 | 5.8 dB  |
| Peaking | 1677 Hz  | 2.79 | -3.4 dB |
| Peaking | 2026 Hz  | 2.21 | 4.8 dB  |
| Peaking | 4084 Hz  | 0.15 | -0.7 dB |
| Peaking | 13463 Hz | 1.52 | 3.2 dB  |
| Peaking | 17787 Hz | 2.74 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)