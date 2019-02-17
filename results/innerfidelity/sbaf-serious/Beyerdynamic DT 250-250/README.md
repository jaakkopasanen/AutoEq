# Beyerdynamic DT 250-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.2; 37 -1.5; 41 -1.9; 45 -2.3; 49 -2.5; 54 -2.8; 60 -3.0; 66 -3.1; 72 -3.2; 79 -2.4; 87 -1.9; 96 -2.5; 106 -2.6; 116 -3.1; 128 -4.4; 141 -5.0; 155 -5.0; 170 -4.5; 187 -5.4; 206 -5.5; 227 -5.4; 249 -5.3; 274 -5.3; 302 -5.5; 332 -5.4; 365 -5.2; 402 -5.2; 442 -5.2; 486 -5.5; 535 -5.6; 588 -5.5; 647 -5.8; 712 -6.2; 783 -6.2; 861 -6.7; 947 -7.1; 1042 -6.0; 1146 -6.3; 1261 -7.6; 1387 -8.6; 1526 -9.4; 1678 -9.7; 1846 -9.2; 2031 -8.1; 2234 -7.1; 2457 -5.9; 2703 -4.7; 2973 -2.9; 3270 -1.5; 3597 -2.5; 3957 -3.9; 4353 -4.9; 4788 -4.3; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.44 | 3.1 dB  |
| Peaking | 29 Hz   | 1.14 | 3.9 dB  |
| Peaking | 87 Hz   | 0.68 | 3.4 dB  |
| Peaking | 3320 Hz | 4.51 | 5.3 dB  |
| Peaking | 5872 Hz | 3.57 | 6.6 dB  |
| Peaking | 99 Hz   | 1.93 | 2.9 dB  |
| Peaking | 107 Hz  | 0.89 | -3.1 dB |
| Peaking | 450 Hz  | 0.09 | 0.9 dB  |
| Peaking | 1654 Hz | 2.01 | -4.4 dB |
| Peaking | 9343 Hz | 4.31 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)