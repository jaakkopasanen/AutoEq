# Phiaton MS 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.0; 49 -2.6; 54 -3.2; 60 -3.8; 66 -4.2; 72 -4.2; 79 -4.3; 87 -4.9; 96 -5.1; 106 -5.4; 116 -5.4; 128 -5.7; 141 -5.6; 155 -5.8; 170 -5.7; 187 -5.6; 206 -5.4; 227 -4.7; 249 -5.0; 274 -5.2; 302 -5.3; 332 -5.5; 365 -5.5; 402 -5.1; 442 -5.2; 486 -4.9; 535 -4.0; 588 -2.7; 647 -1.9; 712 -2.3; 783 -3.0; 861 -4.3; 947 -5.6; 1042 -7.1; 1146 -8.4; 1261 -9.2; 1387 -9.7; 1526 -9.4; 1678 -8.5; 1846 -8.2; 2031 -6.8; 2234 -4.7; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 28 Hz   | 0.64 | 6.4 dB  |
| Peaking | 241 Hz  | 2.56 | 1.2 dB  |
| Peaking | 692 Hz  | 1.74 | 5.3 dB  |
| Peaking | 1521 Hz | 1.15 | -6.6 dB |
| Peaking | 3408 Hz | 0.75 | 8.0 dB  |
| Peaking | 2073 Hz | 5.55 | -1.1 dB |
| Peaking | 2578 Hz | 4.91 | 1.9 dB  |
| Peaking | 3608 Hz | 2.8  | -1.2 dB |
| Peaking | 6319 Hz | 2.2  | 5.4 dB  |
| Peaking | 7330 Hz | 1.45 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)