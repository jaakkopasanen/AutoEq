# Bowers & Wilkins P3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -6.1; 25 -6.6; 28 -7.3; 31 -7.9; 34 -8.5; 37 -9.0; 41 -9.5; 45 -10.0; 49 -10.4; 54 -10.9; 60 -11.4; 66 -11.8; 72 -12.3; 79 -12.7; 87 -13.3; 96 -13.8; 106 -14.2; 116 -14.4; 128 -14.7; 141 -14.8; 155 -15.2; 170 -15.3; 187 -15.4; 206 -15.7; 227 -15.8; 249 -16.0; 274 -16.0; 302 -15.9; 332 -15.7; 365 -15.3; 402 -14.7; 442 -13.8; 486 -13.3; 535 -12.7; 588 -11.7; 647 -10.6; 712 -9.5; 783 -8.3; 861 -7.4; 947 -6.8; 1042 -6.2; 1146 -5.0; 1261 -4.2; 1387 -4.9; 1526 -4.5; 1678 -4.2; 1846 -3.3; 2031 -2.7; 2234 -2.7; 2457 -2.5; 2703 -3.2; 2973 -4.5; 3270 -6.0; 3597 -6.4; 3957 -5.9; 4353 -3.0; 4788 -0.5; 5267 -3.3; 5793 -4.1; 6373 -3.3; 7010 -5.6; 7711 -8.5; 8482 -10.0; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -9.4; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 105 Hz  | 0.54 | -5.5 dB |
| Peaking | 333 Hz  | 0.59 | -7.9 dB |
| Peaking | 1691 Hz | 0.71 | 4.1 dB  |
| Peaking | 4868 Hz | 5.1  | 5.6 dB  |
| Peaking | 8510 Hz | 5.33 | -4.3 dB |
| Peaking | 21 Hz   | 2.53 | 2.0 dB  |
| Peaking | 1649 Hz | 2.73 | -2.3 dB |
| Peaking | 2174 Hz | 1.02 | 1.9 dB  |
| Peaking | 3496 Hz | 3.22 | -2.8 dB |
| Peaking | 6380 Hz | 8.59 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -8.2 dB |
| Peaking | 500 Hz   | 1.41 | -5.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P3/Bowers%20&%20Wilkins%20P3.png)