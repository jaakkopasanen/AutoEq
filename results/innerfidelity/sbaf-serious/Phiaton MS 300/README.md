# Phiaton MS 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.0; 31 -1.9; 34 -2.8; 37 -3.6; 41 -4.5; 45 -5.4; 49 -6.0; 54 -6.6; 60 -7.2; 66 -7.6; 72 -7.6; 79 -7.7; 87 -8.3; 96 -8.5; 106 -8.8; 116 -8.8; 128 -9.1; 141 -9.0; 155 -9.2; 170 -9.1; 187 -9.0; 206 -8.8; 227 -8.1; 249 -8.4; 274 -8.6; 302 -8.7; 332 -8.9; 365 -8.9; 402 -8.5; 442 -8.6; 486 -8.3; 535 -7.4; 588 -6.1; 647 -5.3; 712 -5.7; 783 -6.4; 861 -7.7; 947 -9.0; 1042 -10.5; 1146 -11.8; 1261 -12.6; 1387 -13.1; 1526 -12.8; 1678 -11.9; 1846 -11.6; 2031 -10.2; 2234 -8.1; 2457 -5.2; 2703 -2.7; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.4; 6373 -3.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.19 | 6.6 dB  |
| Peaking | 126 Hz  | 0.68 | -2.8 dB |
| Peaking | 350 Hz  | 2.82 | -1.7 dB |
| Peaking | 1571 Hz | 1.39 | -8.6 dB |
| Peaking | 3690 Hz | 1.02 | 8.0 dB  |
| Peaking | 689 Hz  | 3.85 | 2.7 dB  |
| Peaking | 1132 Hz | 4.49 | -1.7 dB |
| Peaking | 4041 Hz | 3.29 | -2.4 dB |
| Peaking | 5257 Hz | 1.17 | 2.7 dB  |
| Peaking | 7877 Hz | 1.26 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)