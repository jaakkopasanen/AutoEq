# Etymotic ER-6i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.1; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.8; 66 -3.2; 72 -3.5; 79 -3.8; 87 -4.2; 96 -4.4; 106 -4.7; 116 -4.9; 128 -5.2; 141 -5.5; 155 -5.8; 170 -5.9; 187 -6.1; 206 -6.2; 227 -6.2; 249 -6.2; 274 -6.2; 302 -6.1; 332 -6.0; 365 -6.0; 402 -6.0; 442 -6.1; 486 -6.0; 535 -5.8; 588 -5.6; 647 -5.6; 712 -5.5; 783 -5.6; 861 -5.9; 947 -6.5; 1042 -7.1; 1146 -7.7; 1261 -8.3; 1387 -9.0; 1526 -9.8; 1678 -10.5; 1846 -11.2; 2031 -11.3; 2234 -10.9; 2457 -10.0; 2703 -8.9; 2973 -7.1; 3270 -5.1; 3597 -4.0; 3957 -4.8; 4353 -6.4; 4788 -6.1; 5267 -3.4; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-6i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.68 | 4.6 dB  |
| Peaking | 55 Hz    | 1.06 | 2.0 dB  |
| Peaking | 1999 Hz  | 1.39 | -5.7 dB |
| Peaking | 3502 Hz  | 4.81 | 3.4 dB  |
| Peaking | 6089 Hz  | 4.18 | 6.7 dB  |
| Peaking | 217 Hz   | 2.06 | -0.5 dB |
| Peaking | 778 Hz   | 1.29 | 2.0 dB  |
| Peaking | 998 Hz   | 0.68 | -1.2 dB |
| Peaking | 1952 Hz  | 2.87 | 0.6 dB  |
| Peaking | 22050 Hz | 1.74 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i/Etymotic%20ER-6i.png)