# Sennheiser Momentum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.1; 25 -6.4; 28 -6.6; 31 -6.9; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.2; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.7; 116 -9.6; 128 -9.6; 141 -9.8; 155 -10.4; 170 -10.3; 187 -10.4; 206 -10.7; 227 -10.6; 249 -10.4; 274 -9.9; 302 -9.7; 332 -9.1; 365 -8.3; 402 -7.9; 442 -7.9; 486 -7.8; 535 -7.9; 588 -7.9; 647 -8.2; 712 -8.7; 783 -9.0; 861 -9.2; 947 -9.3; 1042 -9.4; 1146 -9.3; 1261 -9.7; 1387 -10.4; 1526 -11.0; 1678 -10.9; 1846 -10.7; 2031 -9.7; 2234 -8.2; 2457 -6.1; 2703 -4.1; 2973 -2.7; 3270 -0.7; 3597 -0.7; 3957 -0.6; 4353 -0.5; 4788 -0.8; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 99 Hz   | 0.77 | -2.4 dB |
| Peaking | 222 Hz  | 1.16 | -3.3 dB |
| Peaking | 1807 Hz | 0.77 | -6.2 dB |
| Peaking | 3469 Hz | 1.24 | 9.0 dB  |
| Peaking | 5942 Hz | 3.9  | 4.5 dB  |
| Peaking | 20 Hz   | 1.88 | 0.9 dB  |
| Peaking | 815 Hz  | 3.81 | -0.6 dB |
| Peaking | 1199 Hz | 6.3  | 0.8 dB  |
| Peaking | 6650 Hz | 8.87 | 1.7 dB  |
| Peaking | 7998 Hz | 2.49 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)