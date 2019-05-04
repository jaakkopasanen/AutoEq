# Bowers & Wilkins P5 Series 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -8.0; 28 -8.4; 31 -8.6; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.9; 60 -8.9; 66 -9.0; 72 -9.0; 79 -9.0; 87 -9.0; 96 -9.0; 106 -8.8; 116 -8.7; 128 -8.4; 141 -7.9; 155 -7.5; 170 -7.0; 187 -6.5; 206 -6.0; 227 -5.4; 249 -4.7; 274 -3.9; 302 -2.9; 332 -1.8; 365 -0.7; 402 -0.5; 442 -1.2; 486 -2.0; 535 -2.5; 588 -2.8; 647 -3.1; 712 -3.3; 783 -3.6; 861 -3.8; 947 -4.3; 1042 -4.9; 1146 -5.6; 1261 -6.5; 1387 -7.5; 1526 -8.8; 1678 -9.9; 1846 -11.1; 2031 -11.7; 2234 -11.7; 2457 -11.1; 2703 -9.3; 2973 -6.1; 3270 -4.3; 3597 -4.9; 3957 -5.3; 4353 -5.1; 4788 -4.3; 5267 -3.8; 5793 -4.6; 6373 -5.0; 7010 -3.8; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.2; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.78 | -2.0 dB  |
| Peaking | 131 Hz  | 0.34 | -4.4 dB  |
| Peaking | 387 Hz  | 0.75 | 6.5 dB   |
| Peaking | 2205 Hz | 1.36 | -10.0 dB |
| Peaking | 3124 Hz | 0.99 | 4.0 dB   |
| Peaking | 559 Hz  | 3.13 | -1.1 dB  |
| Peaking | 927 Hz  | 0.66 | 0.6 dB   |
| Peaking | 1545 Hz | 3.29 | -1.0 dB  |
| Peaking | 2645 Hz | 7.91 | -1.1 dB  |
| Peaking | 3141 Hz | 8.95 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)