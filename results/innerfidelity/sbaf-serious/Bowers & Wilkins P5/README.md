# Bowers & Wilkins P5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.4; 31 -1.8; 34 -2.1; 37 -2.4; 41 -2.7; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.9; 72 -5.5; 79 -6.1; 87 -6.8; 96 -7.5; 106 -8.1; 116 -8.5; 128 -9.2; 141 -9.7; 155 -10.1; 170 -10.1; 187 -10.4; 206 -10.5; 227 -10.3; 249 -9.9; 274 -9.1; 302 -8.0; 332 -7.1; 365 -6.2; 402 -5.4; 442 -4.6; 486 -4.5; 535 -4.6; 588 -4.4; 647 -4.6; 712 -4.9; 783 -4.8; 861 -5.0; 947 -5.0; 1042 -5.0; 1146 -5.0; 1261 -5.2; 1387 -5.7; 1526 -6.4; 1678 -6.8; 1846 -7.3; 2031 -7.3; 2234 -8.0; 2457 -7.8; 2703 -7.0; 2973 -6.5; 3270 -5.7; 3597 -5.0; 3957 -3.5; 4353 -3.3; 4788 -2.9; 5267 -2.2; 5793 -1.9; 6373 -1.2; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.1; 18182 -5.4; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.11 | 4.4 dB  |
| Peaking | 43 Hz   | 1.79 | 1.5 dB  |
| Peaking | 175 Hz  | 1    | -5.9 dB |
| Peaking | 2280 Hz | 1.94 | -3.3 dB |
| Peaking | 5714 Hz | 1.86 | 3.7 dB  |
| Peaking | 99 Hz   | 4.48 | -0.8 dB |
| Peaking | 265 Hz  | 3.41 | -1.5 dB |
| Peaking | 491 Hz  | 1.35 | 1.5 dB  |
| Peaking | 4049 Hz | 9.84 | 1.0 dB  |
| Peaking | 8395 Hz | 4.47 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5/Bowers%20&%20Wilkins%20P5.png)