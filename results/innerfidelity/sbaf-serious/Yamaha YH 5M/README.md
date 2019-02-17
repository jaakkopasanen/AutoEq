# Yamaha YH 5M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.0; 87 -1.5; 96 -2.1; 106 -2.4; 116 -2.7; 128 -3.0; 141 -3.7; 155 -3.9; 170 -4.1; 187 -4.5; 206 -4.6; 227 -4.7; 249 -4.9; 274 -5.1; 302 -5.2; 332 -5.3; 365 -5.5; 402 -5.7; 442 -5.8; 486 -6.2; 535 -6.6; 588 -6.6; 647 -7.0; 712 -7.7; 783 -7.9; 861 -7.8; 947 -6.8; 1042 -6.0; 1146 -3.8; 1261 -1.7; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -1.5; 5267 -2.6; 5793 -1.7; 6373 -4.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH 5M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH 5M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.28 | 6.3 dB  |
| Peaking | 874 Hz  | 1.66 | -3.4 dB |
| Peaking | 1390 Hz | 1.85 | 4.6 dB  |
| Peaking | 2379 Hz | 0.97 | 4.5 dB  |
| Peaking | 4330 Hz | 1.32 | 4.0 dB  |
| Peaking | 70 Hz   | 4.68 | 0.3 dB  |
| Peaking | 5123 Hz | 4.88 | -2.0 dB |
| Peaking | 5623 Hz | 3.03 | 2.3 dB  |
| Peaking | 8534 Hz | 2.01 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH%205M/Yamaha%20YH%205M.png)