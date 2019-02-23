# Etymotic EK5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.8; 41 -1.1; 45 -1.3; 49 -1.5; 54 -1.8; 60 -2.1; 66 -2.6; 72 -2.9; 79 -3.3; 87 -3.8; 96 -4.3; 106 -4.5; 116 -4.7; 128 -5.1; 141 -5.4; 155 -5.6; 170 -5.7; 187 -5.8; 206 -5.9; 227 -5.9; 249 -6.0; 274 -6.0; 302 -5.9; 332 -5.8; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.7; 535 -5.6; 588 -5.3; 647 -5.4; 712 -5.7; 783 -5.7; 861 -6.2; 947 -6.9; 1042 -7.8; 1146 -8.7; 1261 -9.7; 1387 -10.2; 1526 -11.2; 1678 -12.4; 1846 -13.1; 2031 -13.7; 2234 -13.4; 2457 -10.5; 2703 -10.0; 2973 -8.0; 3270 -6.5; 3597 -5.5; 3957 -5.3; 4353 -6.0; 4788 -6.2; 5267 -5.6; 5793 -4.9; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic EK5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic EK5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.43 | 6.2 dB  |
| Peaking | 692 Hz  | 1.08 | 1.9 dB  |
| Peaking | 2018 Hz | 1.09 | -8.1 dB |
| Peaking | 3473 Hz | 1.68 | 3.8 dB  |
| Peaking | 6517 Hz | 4.69 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20EK5/Etymotic%20EK5.png)