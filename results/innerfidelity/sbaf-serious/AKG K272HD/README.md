# AKG K272HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.3; 41 -2.2; 45 -3.1; 49 -3.8; 54 -4.4; 60 -5.1; 66 -6.0; 72 -6.7; 79 -7.5; 87 -7.6; 96 -5.3; 106 -2.5; 116 -3.4; 128 -6.3; 141 -7.3; 155 -7.2; 170 -6.5; 187 -7.0; 206 -7.0; 227 -7.5; 249 -7.8; 274 -8.0; 302 -8.0; 332 -8.1; 365 -8.1; 402 -8.2; 442 -8.1; 486 -8.2; 535 -8.4; 588 -8.6; 647 -9.5; 712 -6.3; 783 -6.1; 861 -6.0; 947 -6.0; 1042 -6.8; 1146 -6.8; 1261 -7.6; 1387 -8.3; 1526 -9.3; 1678 -9.3; 1846 -8.1; 2031 -5.2; 2234 -4.2; 2457 -2.6; 2703 -2.1; 2973 -1.5; 3270 -1.9; 3597 -1.0; 3957 -0.5; 4353 -1.2; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -10.6; 9330 -13.0; 10263 -9.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.66 | 4.7 dB   |
| Peaking | 34 Hz   | 1.61 | 4.6 dB   |
| Peaking | 1591 Hz | 2.26 | -5.0 dB  |
| Peaking | 4845 Hz | 0.57 | 7.0 dB   |
| Peaking | 9120 Hz | 2.64 | -10.5 dB |
| Peaking | 84 Hz   | 4.35 | -2.3 dB  |
| Peaking | 108 Hz  | 5.86 | 4.9 dB   |
| Peaking | 366 Hz  | 0.77 | -1.8 dB  |
| Peaking | 639 Hz  | 3.79 | -4.2 dB  |
| Peaking | 724 Hz  | 2.35 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)