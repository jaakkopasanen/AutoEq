# Etymotic ER-6i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -0.9; 31 -1.0; 34 -1.1; 37 -1.2; 41 -1.5; 45 -1.6; 49 -1.8; 54 -2.0; 60 -2.3; 66 -2.8; 72 -3.1; 79 -3.4; 87 -3.7; 96 -4.0; 106 -4.3; 116 -4.5; 128 -4.8; 141 -5.1; 155 -5.3; 170 -5.5; 187 -5.6; 206 -5.7; 227 -5.7; 249 -5.8; 274 -5.8; 302 -5.7; 332 -5.5; 365 -5.6; 402 -5.6; 442 -5.6; 486 -5.5; 535 -5.4; 588 -5.1; 647 -5.1; 712 -5.1; 783 -5.2; 861 -5.5; 947 -6.0; 1042 -6.6; 1146 -7.3; 1261 -7.8; 1387 -8.6; 1526 -9.3; 1678 -10.0; 1846 -10.7; 2031 -10.8; 2234 -10.4; 2457 -9.6; 2703 -8.4; 2973 -6.7; 3270 -4.7; 3597 -3.6; 3957 -4.4; 4353 -6.0; 4788 -5.6; 5267 -2.9; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.36 | 3.5 dB  |
| Peaking | 2007 Hz | 1.8  | -5.0 dB |
| Peaking | 3533 Hz | 4.63 | 3.6 dB  |
| Peaking | 6005 Hz | 3.89 | 6.7 dB  |
| Peaking | 19 Hz   | 0.98 | 2.7 dB  |
| Peaking | 50 Hz   | 1.77 | 0.7 dB  |
| Peaking | 714 Hz  | 1.18 | 1.6 dB  |
| Peaking | 1351 Hz | 2.29 | -1.0 dB |
| Peaking | 8097 Hz | 5.4  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i/Etymotic%20ER-6i.png)