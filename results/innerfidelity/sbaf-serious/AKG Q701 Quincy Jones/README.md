# AKG Q701 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.0; 49 -1.5; 54 -2.0; 60 -2.6; 66 -3.0; 72 -3.1; 79 -3.1; 87 -3.5; 96 -4.3; 106 -4.7; 116 -5.1; 128 -5.7; 141 -6.0; 155 -6.3; 170 -6.3; 187 -6.4; 206 -6.6; 227 -6.5; 249 -6.5; 274 -6.5; 302 -6.3; 332 -6.2; 365 -6.0; 402 -5.9; 442 -5.6; 486 -5.5; 535 -5.3; 588 -3.8; 647 -4.1; 712 -4.0; 783 -3.8; 861 -4.3; 947 -4.6; 1042 -4.7; 1146 -5.1; 1261 -5.7; 1387 -6.7; 1526 -7.9; 1678 -9.0; 1846 -10.0; 2031 -10.3; 2234 -9.9; 2457 -8.6; 2703 -7.1; 2973 -5.9; 3270 -4.7; 3597 -4.3; 3957 -5.2; 4353 -7.2; 4788 -6.6; 5267 -6.7; 5793 -8.3; 6373 -9.5; 7010 -9.2; 7711 -9.5; 8482 -10.2; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.57 | 6.5 dB  |
| Peaking | 802 Hz   | 1.24 | 3.0 dB  |
| Peaking | 1995 Hz  | 2.04 | -4.5 dB |
| Peaking | 3384 Hz  | 3.25 | 3.2 dB  |
| Peaking | 7416 Hz  | 1.94 | -3.5 dB |
| Peaking | 84 Hz    | 3.18 | 1.0 dB  |
| Peaking | 176 Hz   | 1.03 | -0.7 dB |
| Peaking | 602 Hz   | 2.89 | -0.5 dB |
| Peaking | 603 Hz   | 6.89 | 1.5 dB  |
| Peaking | 10357 Hz | 5.79 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)