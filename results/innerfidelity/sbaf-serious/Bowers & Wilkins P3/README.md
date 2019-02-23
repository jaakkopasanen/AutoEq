# Bowers & Wilkins P3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.5; 25 -4.1; 28 -4.8; 31 -5.4; 34 -5.9; 37 -6.4; 41 -7.0; 45 -7.4; 49 -7.8; 54 -8.3; 60 -8.8; 66 -9.3; 72 -9.7; 79 -10.2; 87 -10.7; 96 -11.3; 106 -11.6; 116 -11.8; 128 -12.1; 141 -12.2; 155 -12.7; 170 -12.8; 187 -12.8; 206 -13.1; 227 -13.2; 249 -13.5; 274 -13.4; 302 -13.4; 332 -13.1; 365 -12.7; 402 -12.1; 442 -11.3; 486 -10.7; 535 -10.1; 588 -9.1; 647 -8.1; 712 -7.0; 783 -5.7; 861 -4.9; 947 -4.3; 1042 -3.6; 1146 -2.4; 1261 -1.6; 1387 -2.3; 1526 -2.0; 1678 -1.7; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -2.0; 3270 -3.4; 3597 -3.8; 3957 -3.3; 4353 -0.8; 4788 -0.5; 5267 -1.0; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -7.4; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.94 | 4.5 dB  |
| Peaking | 283 Hz  | 0.29 | -7.6 dB |
| Peaking | 1098 Hz | 0.75 | 6.7 dB  |
| Peaking | 2303 Hz | 1.66 | 4.6 dB  |
| Peaking | 5204 Hz | 2.05 | 5.6 dB  |
| Peaking | 2779 Hz | 6.34 | 1.1 dB  |
| Peaking | 3794 Hz | 3.35 | -0.8 dB |
| Peaking | 4401 Hz | 5.03 | 2.5 dB  |
| Peaking | 6469 Hz | 1.37 | -3.5 dB |
| Peaking | 6539 Hz | 4.33 | 5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P3/Bowers%20&%20Wilkins%20P3.png)