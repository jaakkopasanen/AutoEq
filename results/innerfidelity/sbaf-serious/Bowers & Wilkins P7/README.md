# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.2; 28 -6.6; 31 -6.9; 34 -7.2; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.8; 54 -7.6; 60 -7.7; 66 -8.3; 72 -8.6; 79 -8.7; 87 -8.6; 96 -8.2; 106 -7.3; 116 -6.8; 128 -7.4; 141 -8.2; 155 -8.2; 170 -7.0; 187 -7.6; 206 -7.0; 227 -6.4; 249 -5.7; 274 -5.0; 302 -4.5; 332 -4.3; 365 -4.1; 402 -4.2; 442 -4.0; 486 -4.1; 535 -4.2; 588 -4.0; 647 -4.2; 712 -4.9; 783 -5.5; 861 -6.2; 947 -6.0; 1042 -6.4; 1146 -6.9; 1261 -7.7; 1387 -8.9; 1526 -9.8; 1678 -10.5; 1846 -10.5; 2031 -10.1; 2234 -9.4; 2457 -7.5; 2703 -4.1; 2973 -2.2; 3270 -2.4; 3597 -4.6; 3957 -6.1; 4353 -6.0; 4788 -5.0; 5267 -3.6; 5793 -4.4; 6373 -0.5; 7010 -3.0; 7711 -5.3; 8482 -5.5; 9330 -5.9; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 1.04 | -3.1 dB |
| Peaking | 150 Hz  | 3.68 | -2.1 dB |
| Peaking | 1846 Hz | 1.79 | -5.8 dB |
| Peaking | 3027 Hz | 4.2  | 5.2 dB  |
| Peaking | 6501 Hz | 6.03 | 5.3 dB  |
| Peaking | 35 Hz   | 2.72 | -0.7 dB |
| Peaking | 201 Hz  | 3.71 | -1.5 dB |
| Peaking | 448 Hz  | 0.92 | 2.2 dB  |
| Peaking | 2024 Hz | 0.17 | -0.4 dB |
| Peaking | 5269 Hz | 9.35 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)