# Beyerdynamic DT 770 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.5; 25 -7.8; 28 -8.2; 31 -8.3; 34 -8.5; 37 -8.4; 41 -8.0; 45 -7.0; 49 -6.5; 54 -6.4; 60 -2.7; 66 -2.0; 72 -6.1; 79 -8.5; 87 -9.7; 96 -10.2; 106 -10.5; 116 -10.3; 128 -9.8; 141 -8.6; 155 -7.0; 170 -6.8; 187 -5.7; 206 -4.9; 227 -4.9; 249 -5.2; 274 -5.7; 302 -5.8; 332 -5.9; 365 -6.1; 402 -6.2; 442 -6.4; 486 -6.3; 535 -6.5; 588 -6.5; 647 -6.6; 712 -6.6; 783 -6.6; 861 -6.3; 947 -5.6; 1042 -5.7; 1146 -5.4; 1261 -5.3; 1387 -5.1; 1526 -5.5; 1678 -6.2; 1846 -6.5; 2031 -6.4; 2234 -5.8; 2457 -4.7; 2703 -3.7; 2973 -2.9; 3270 -2.2; 3597 -0.5; 3957 -0.5; 4353 -4.9; 4788 -8.6; 5267 -7.3; 5793 -8.6; 6373 -12.0; 7010 -9.7; 7711 -10.1; 8482 -12.6; 9330 -13.5; 10263 -10.8; 11289 -9.0; 12418 -10.6; 13660 -9.1; 15026 -6.5; 16529 -7.3; 18182 -13.9; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.75 | -2.1 dB  |
| Peaking | 63 Hz    | 6.19 | 6.7 dB   |
| Peaking | 102 Hz   | 2.29 | -4.6 dB  |
| Peaking | 3609 Hz  | 1.86 | 8.5 dB   |
| Peaking | 8204 Hz  | 0.55 | -5.7 dB  |
| Peaking | 131 Hz   | 5.24 | -1.6 dB  |
| Peaking | 220 Hz   | 2.05 | 2.0 dB   |
| Peaking | 1247 Hz  | 2.85 | 1.4 dB   |
| Peaking | 15909 Hz | 1.37 | 6.2 dB   |
| Peaking | 19106 Hz | 0.64 | -10.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%20250%20Ohm/Beyerdynamic%20DT%20770%20250%20Ohm.png)