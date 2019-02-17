# AKG K67 Tiesto
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.2; 25 -6.6; 28 -7.1; 31 -7.4; 34 -7.5; 37 -7.6; 41 -7.6; 45 -7.4; 49 -7.0; 54 -6.8; 60 -6.9; 66 -7.2; 72 -7.4; 79 -8.1; 87 -8.6; 96 -8.9; 106 -9.2; 116 -9.2; 128 -9.0; 141 -8.2; 155 -6.4; 170 -4.7; 187 -2.5; 206 -1.3; 227 -0.6; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -1.0; 442 -1.6; 486 -2.4; 535 -2.8; 588 -2.9; 647 -3.5; 712 -4.2; 783 -4.7; 861 -5.6; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -6.9; 1526 -7.4; 1678 -7.0; 1846 -5.8; 2031 -4.1; 2234 -3.1; 2457 -1.9; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -1.1; 5267 -2.1; 5793 -4.6; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K67 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K67 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.56 | -3.3 dB |
| Peaking | 129 Hz  | 1.35 | -6.4 dB |
| Peaking | 223 Hz  | 0.49 | 9.2 dB  |
| Peaking | 1446 Hz | 1.05 | -3.8 dB |
| Peaking | 3276 Hz | 0.87 | 7.2 dB  |
| Peaking | 35 Hz   | 3.35 | -0.6 dB |
| Peaking | 3376 Hz | 8.25 | -0.3 dB |
| Peaking | 4910 Hz | 4.84 | 2.5 dB  |
| Peaking | 6603 Hz | 4.77 | 4.8 dB  |
| Peaking | 6678 Hz | 1.54 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 7.1 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K67%20Tiesto/AKG%20K67%20Tiesto.png)