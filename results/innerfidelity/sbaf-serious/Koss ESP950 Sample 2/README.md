# Koss ESP950 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -0.6; 87 -0.9; 96 -1.8; 106 -2.8; 116 -3.5; 128 -3.6; 141 -3.7; 155 -3.8; 170 -4.0; 187 -4.3; 206 -4.4; 227 -4.3; 249 -4.4; 274 -4.4; 302 -4.3; 332 -4.4; 365 -4.4; 402 -4.6; 442 -4.7; 486 -5.0; 535 -5.2; 588 -5.0; 647 -5.3; 712 -5.5; 783 -5.6; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -7.0; 1261 -7.6; 1387 -8.3; 1526 -8.2; 1678 -7.4; 1846 -5.3; 2031 -3.4; 2234 -2.0; 2457 -1.8; 2703 -3.4; 2973 -4.0; 3270 -3.5; 3597 -2.0; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -2.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.9; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.35 | 6.5 dB  |
| Peaking | 419 Hz   | 0.82 | 1.5 dB  |
| Peaking | 1493 Hz  | 2.21 | -3.1 dB |
| Peaking | 2262 Hz  | 2.78 | 4.6 dB  |
| Peaking | 4761 Hz  | 1.63 | 6.7 dB  |
| Peaking | 84 Hz    | 3.53 | 1.1 dB  |
| Peaking | 118 Hz   | 3.13 | -0.8 dB |
| Peaking | 6349 Hz  | 5.64 | 2.0 dB  |
| Peaking | 9108 Hz  | 3.6  | -3.1 dB |
| Peaking | 20905 Hz | 1.32 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%202/Koss%20ESP950%20sample%202.png)