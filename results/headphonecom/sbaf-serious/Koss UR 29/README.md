# Koss UR 29
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.0; 87 -1.7; 96 -2.2; 106 -2.7; 116 -3.0; 128 -3.2; 141 -3.7; 155 -3.8; 170 -3.7; 187 -3.8; 206 -4.0; 227 -4.3; 249 -4.6; 274 -4.7; 302 -4.6; 332 -4.4; 365 -4.2; 402 -4.3; 442 -4.2; 486 -4.4; 535 -4.8; 588 -5.4; 647 -6.3; 712 -6.3; 783 -6.1; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -5.8; 1261 -5.6; 1387 -5.9; 1526 -6.2; 1678 -7.0; 1846 -8.6; 2031 -8.8; 2234 -8.4; 2457 -6.2; 2703 -3.8; 2973 -2.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR 29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.19 | 4.9 dB  |
| Peaking | 69 Hz   | 0.41 | 2.4 dB  |
| Peaking | 406 Hz  | 1.72 | 1.8 dB  |
| Peaking | 2072 Hz | 3.14 | -4.8 dB |
| Peaking | 4128 Hz | 1.1  | 7.1 dB  |
| Peaking | 891 Hz  | 5.77 | -0.8 dB |
| Peaking | 3132 Hz | 5.13 | 1.1 dB  |
| Peaking | 4160 Hz | 3.68 | -1.2 dB |
| Peaking | 6102 Hz | 3.89 | 2.9 dB  |
| Peaking | 8741 Hz | 3.5  | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2029/Koss%20UR%2029.png)