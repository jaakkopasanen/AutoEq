# Yuin PK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.4; 87 -2.1; 96 -2.7; 106 -3.1; 116 -3.2; 128 -3.4; 141 -3.6; 155 -3.8; 170 -3.7; 187 -3.9; 206 -3.8; 227 -4.0; 249 -3.9; 274 -3.9; 302 -3.9; 332 -3.9; 365 -4.0; 402 -4.2; 442 -4.5; 486 -4.8; 535 -4.9; 588 -5.0; 647 -5.2; 712 -5.4; 783 -5.6; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.9; 1526 -8.9; 1678 -9.8; 1846 -10.5; 2031 -10.8; 2234 -10.5; 2457 -9.6; 2703 -7.9; 2973 -6.1; 3270 -4.6; 3597 -4.1; 3957 -5.5; 4353 -8.0; 4788 -9.1; 5267 -9.3; 5793 -9.6; 6373 -10.1; 7010 -9.0; 7711 -8.5; 8482 -8.5; 9330 -8.1; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.37 | 6.4 dB  |
| Peaking | 374 Hz   | 0.6  | 2.0 dB  |
| Peaking | 2046 Hz  | 1.55 | -4.8 dB |
| Peaking | 3480 Hz  | 2.5  | 5.3 dB  |
| Peaking | 5577 Hz  | 1.1  | -3.8 dB |
| Peaking | 40 Hz    | 2.18 | -0.5 dB |
| Peaking | 70 Hz    | 3.08 | 1.0 dB  |
| Peaking | 96 Hz    | 2.42 | -0.5 dB |
| Peaking | 11317 Hz | 4.47 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)