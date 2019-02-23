# Aurex HR V9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.8; 37 -2.2; 41 -2.6; 45 -2.9; 49 -3.2; 54 -3.6; 60 -3.9; 66 -4.2; 72 -4.5; 79 -4.8; 87 -5.2; 96 -5.3; 106 -6.0; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.1; 170 -7.2; 187 -7.4; 206 -7.4; 227 -7.4; 249 -7.5; 274 -7.3; 302 -7.3; 332 -7.3; 365 -7.4; 402 -7.4; 442 -7.3; 486 -7.5; 535 -7.6; 588 -7.3; 647 -7.4; 712 -7.7; 783 -7.8; 861 -8.5; 947 -8.8; 1042 -8.6; 1146 -8.4; 1261 -7.6; 1387 -7.2; 1526 -6.5; 1678 -6.0; 1846 -5.8; 2031 -7.4; 2234 -8.6; 2457 -7.9; 2703 -6.9; 2973 -5.6; 3270 -4.9; 3597 -4.4; 3957 -4.4; 4353 -5.2; 4788 -5.0; 5267 -3.1; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurex HR V9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurex HR V9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.62 | 6.0 dB  |
| Peaking | 70 Hz   | 1.57 | 0.9 dB  |
| Peaking | 545 Hz  | 0.25 | -1.4 dB |
| Peaking | 1724 Hz | 6.17 | 1.7 dB  |
| Peaking | 5923 Hz | 3.05 | 6.1 dB  |
| Peaking | 1000 Hz | 0.77 | 1.7 dB  |
| Peaking | 1001 Hz | 1.79 | -2.8 dB |
| Peaking | 2290 Hz | 5.02 | -2.3 dB |
| Peaking | 3507 Hz | 3.42 | 2.1 dB  |
| Peaking | 8950 Hz | 4.63 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurex%20HR%20V9/Aurex%20HR%20V9.png)