# Phiaton MS 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.4; 54 -2.3; 60 -2.9; 66 -3.4; 72 -3.6; 79 -3.6; 87 -3.7; 96 -4.0; 106 -4.2; 116 -4.3; 128 -4.4; 141 -4.4; 155 -4.3; 170 -4.2; 187 -4.1; 206 -3.7; 227 -3.4; 249 -3.4; 274 -3.3; 302 -3.4; 332 -3.5; 365 -3.3; 402 -2.8; 442 -2.9; 486 -2.5; 535 -2.1; 588 -1.9; 647 -1.8; 712 -2.3; 783 -3.5; 861 -4.5; 947 -5.7; 1042 -7.0; 1146 -8.2; 1261 -8.6; 1387 -8.6; 1526 -7.9; 1678 -7.4; 1846 -7.4; 2031 -5.4; 2234 -3.2; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.54 | 6.3 dB  |
| Peaking | 274 Hz  | 0.74 | 2.4 dB  |
| Peaking | 648 Hz  | 1.31 | 4.6 dB  |
| Peaking | 1427 Hz | 1.08 | -5.8 dB |
| Peaking | 3348 Hz | 0.72 | 7.8 dB  |
| Peaking | 1953 Hz | 5.78 | -1.4 dB |
| Peaking | 2465 Hz | 4.13 | 1.9 dB  |
| Peaking | 3482 Hz | 2.56 | -1.2 dB |
| Peaking | 6271 Hz | 2.16 | 5.5 dB  |
| Peaking | 7395 Hz | 1.46 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)