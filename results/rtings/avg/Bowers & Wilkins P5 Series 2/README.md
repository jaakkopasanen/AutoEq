# Bowers & Wilkins P5 Series 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.2; 28 -8.5; 31 -8.8; 34 -8.9; 37 -9.0; 41 -9.0; 45 -8.9; 49 -8.9; 54 -9.0; 60 -9.0; 66 -9.1; 72 -9.2; 79 -9.2; 87 -9.2; 96 -9.1; 106 -9.0; 116 -8.9; 128 -8.5; 141 -8.1; 155 -7.6; 170 -7.2; 187 -6.7; 206 -6.1; 227 -5.5; 249 -4.7; 274 -3.9; 302 -2.9; 332 -1.8; 365 -0.7; 402 -0.5; 442 -1.2; 486 -1.9; 535 -2.4; 588 -2.7; 647 -3.0; 712 -3.2; 783 -3.4; 861 -3.7; 947 -4.1; 1042 -4.7; 1146 -5.4; 1261 -6.2; 1387 -7.3; 1526 -8.5; 1678 -9.6; 1846 -10.7; 2031 -11.2; 2234 -10.9; 2457 -10.1; 2703 -8.8; 2973 -6.0; 3270 -4.5; 3597 -5.1; 3957 -5.6; 4353 -5.4; 4788 -3.9; 5267 -3.3; 5793 -4.6; 6373 -6.0; 7010 -3.7; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.3; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.82 | -2.1 dB |
| Peaking | 129 Hz  | 0.33 | -4.7 dB |
| Peaking | 385 Hz  | 0.75 | 6.6 dB  |
| Peaking | 2113 Hz | 1.4  | -8.8 dB |
| Peaking | 3043 Hz | 0.79 | 2.7 dB  |
| Peaking | 576 Hz  | 2.2  | -2.0 dB |
| Peaking | 620 Hz  | 1.16 | 1.4 dB  |
| Peaking | 3267 Hz | 4.84 | 2.4 dB  |
| Peaking | 4023 Hz | 1.31 | -1.8 dB |
| Peaking | 5086 Hz | 5.48 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)