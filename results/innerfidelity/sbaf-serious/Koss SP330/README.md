# Koss SP330
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.6; 25 -9.6; 28 -9.8; 31 -9.9; 34 -10.0; 37 -10.0; 41 -10.0; 45 -10.0; 49 -10.0; 54 -10.0; 60 -9.8; 66 -9.7; 72 -9.8; 79 -10.1; 87 -10.3; 96 -10.4; 106 -10.3; 116 -10.2; 128 -10.1; 141 -9.7; 155 -9.4; 170 -9.0; 187 -8.1; 206 -7.7; 227 -7.4; 249 -6.6; 274 -5.8; 302 -5.3; 332 -5.8; 365 -6.6; 402 -7.2; 442 -7.5; 486 -7.8; 535 -7.7; 588 -7.3; 647 -7.1; 712 -6.8; 783 -5.8; 861 -6.2; 947 -5.8; 1042 -5.4; 1146 -4.9; 1261 -4.6; 1387 -4.6; 1526 -4.7; 1678 -4.8; 1846 -4.7; 2031 -4.3; 2234 -4.5; 2457 -4.4; 2703 -4.7; 2973 -5.0; 3270 -4.7; 3597 -5.2; 3957 -5.9; 4353 -7.7; 4788 -7.4; 5267 -4.5; 5793 -1.9; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.8; 9330 -6.7; 10263 -5.7; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SP330 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP330 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.43 | -4.3 dB |
| Peaking | 120 Hz  | 1.14 | -3.3 dB |
| Peaking | 520 Hz  | 2.83 | -2.2 dB |
| Peaking | 4579 Hz | 6.68 | -3.3 dB |
| Peaking | 6225 Hz | 4.19 | 5.5 dB  |
| Peaking | 301 Hz  | 1.35 | -1.4 dB |
| Peaking | 302 Hz  | 3.06 | 2.8 dB  |
| Peaking | 817 Hz  | 1.87 | -0.6 dB |
| Peaking | 1685 Hz | 0.74 | 1.3 dB  |
| Peaking | 9108 Hz | 3.69 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP330/Koss%20SP330.png)