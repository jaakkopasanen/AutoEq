# Pioneer SE-M290
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.5; 34 -3.5; 37 -4.3; 41 -5.3; 45 -6.0; 49 -6.6; 54 -7.1; 60 -7.7; 66 -8.1; 72 -7.4; 79 -6.1; 87 -7.5; 96 -9.1; 106 -9.5; 116 -9.8; 128 -10.1; 141 -10.3; 155 -10.2; 170 -10.0; 187 -10.2; 206 -10.2; 227 -10.0; 249 -9.7; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.3; 402 -7.7; 442 -7.0; 486 -6.8; 535 -6.6; 588 -6.6; 647 -6.9; 712 -7.3; 783 -7.7; 861 -7.4; 947 -6.8; 1042 -6.2; 1146 -5.0; 1261 -3.2; 1387 -2.1; 1526 -1.2; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -1.0; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-M290 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-M290 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.66 | 6.4 dB  |
| Peaking | 50 Hz   | 2    | -1.9 dB |
| Peaking | 171 Hz  | 0.63 | -4.3 dB |
| Peaking | 893 Hz  | 1.86 | -3.8 dB |
| Peaking | 2489 Hz | 0.45 | 6.9 dB  |
| Peaking | 78 Hz   | 9.45 | 1.8 dB  |
| Peaking | 1627 Hz | 4.71 | 0.9 dB  |
| Peaking | 2574 Hz | 2.07 | -0.9 dB |
| Peaking | 6343 Hz | 1.62 | 5.4 dB  |
| Peaking | 7635 Hz | 1.4  | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-M290/Pioneer%20SE-M290.png)