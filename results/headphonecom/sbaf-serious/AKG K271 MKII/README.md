# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -1.8; 96 -2.7; 106 -3.6; 116 -4.3; 128 -5.1; 141 -5.9; 155 -6.4; 170 -6.0; 187 -6.4; 206 -6.8; 227 -6.4; 249 -6.6; 274 -6.3; 302 -6.7; 332 -7.1; 365 -7.1; 402 -7.3; 442 -7.7; 486 -8.0; 535 -8.1; 588 -8.5; 647 -9.8; 712 -6.7; 783 -5.4; 861 -5.6; 947 -5.9; 1042 -6.9; 1146 -7.5; 1261 -8.0; 1387 -8.9; 1526 -9.5; 1678 -9.7; 1846 -9.1; 2031 -6.7; 2234 -4.5; 2457 -6.2; 2703 -6.6; 2973 -6.3; 3270 -3.9; 3597 -3.3; 3957 -4.3; 4353 -5.9; 4788 -4.3; 5267 -1.8; 5793 -0.9; 6373 -2.0; 7010 -4.3; 7711 -10.3; 8482 -14.5; 9330 -14.8; 10263 -11.3; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.58 | 7.0 dB   |
| Peaking | 1566 Hz | 2.99 | -3.6 dB  |
| Peaking | 3493 Hz | 5.41 | 3.1 dB   |
| Peaking | 6058 Hz | 2.37 | 7.4 dB   |
| Peaking | 8820 Hz | 2.84 | -10.8 dB |
| Peaking | 21 Hz   | 2.88 | 2.0 dB   |
| Peaking | 78 Hz   | 4.92 | 1.9 dB   |
| Peaking | 712 Hz  | 1.52 | -5.3 dB  |
| Peaking | 747 Hz  | 9.11 | 3.5 dB   |
| Peaking | 853 Hz  | 2.35 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)