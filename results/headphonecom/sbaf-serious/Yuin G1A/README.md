# Yuin G1A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.6; 60 -2.8; 66 -3.9; 72 -4.6; 79 -5.1; 87 -6.1; 96 -7.0; 106 -7.7; 116 -8.2; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.2; 187 -9.1; 206 -9.1; 227 -8.9; 249 -8.6; 274 -8.5; 302 -8.2; 332 -7.8; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.8; 535 -6.4; 588 -6.4; 647 -6.2; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.9; 1261 -7.1; 1387 -7.4; 1526 -7.9; 1678 -9.3; 1846 -10.1; 2031 -10.8; 2234 -10.7; 2457 -10.2; 2703 -7.6; 2973 -4.7; 3270 -0.5; 3597 -0.5; 3957 -2.8; 4353 -9.5; 4788 -15.1; 5267 -10.3; 5793 -5.6; 6373 -1.2; 7010 -5.1; 7711 -6.6; 8482 -8.1; 9330 -10.5; 10263 -8.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin G1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 1.17 | 7.3 dB   |
| Peaking | 2244 Hz | 1.79 | -6.2 dB  |
| Peaking | 3571 Hz | 2.33 | 10.8 dB  |
| Peaking | 4760 Hz | 3.44 | -11.8 dB |
| Peaking | 6298 Hz | 6.57 | 7.1 dB   |
| Peaking | 33 Hz   | 1.74 | -6.4 dB  |
| Peaking | 36 Hz   | 0.43 | 5.6 dB   |
| Peaking | 137 Hz  | 0.57 | -4.4 dB  |
| Peaking | 705 Hz  | 1.19 | 1.1 dB   |
| Peaking | 9466 Hz | 5.43 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G1A/Yuin%20G1A.png)