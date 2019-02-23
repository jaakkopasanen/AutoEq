# Koss ESP950 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.2; 31 -1.4; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.7; 49 -1.7; 54 -1.8; 60 -1.9; 66 -2.1; 72 -2.1; 79 -2.2; 87 -2.4; 96 -3.4; 106 -4.3; 116 -5.0; 128 -5.2; 141 -5.3; 155 -5.4; 170 -5.6; 187 -5.8; 206 -5.9; 227 -5.9; 249 -6.0; 274 -5.9; 302 -5.9; 332 -5.9; 365 -6.0; 402 -6.1; 442 -6.2; 486 -6.5; 535 -6.7; 588 -6.6; 647 -6.8; 712 -7.0; 783 -7.1; 861 -7.6; 947 -7.9; 1042 -8.1; 1146 -8.5; 1261 -9.2; 1387 -9.8; 1526 -9.7; 1678 -9.0; 1846 -6.8; 2031 -4.9; 2234 -3.5; 2457 -3.3; 2703 -5.0; 2973 -5.6; 3270 -5.1; 3597 -3.5; 3957 -1.8; 4353 -1.5; 4788 -1.7; 5267 -1.7; 5793 -2.4; 6373 -3.5; 7010 -3.3; 7711 -5.5; 8482 -8.3; 9330 -10.4; 10263 -7.9; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.63 | 4.9 dB  |
| Peaking | 71 Hz   | 1.75 | 2.6 dB  |
| Peaking | 1325 Hz | 1.42 | -4.4 dB |
| Peaking | 5142 Hz | 0.71 | 4.3 dB  |
| Peaking | 9270 Hz | 3.11 | -6.8 dB |
| Peaking | 338 Hz  | 1.81 | 1.2 dB  |
| Peaking | 340 Hz  | 1.02 | -1.3 dB |
| Peaking | 2341 Hz | 3.2  | 4.6 dB  |
| Peaking | 3026 Hz | 1.33 | -3.7 dB |
| Peaking | 4037 Hz | 2.46 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%202/Koss%20ESP950%20sample%202.png)