# Beyerdynamic T70 250 Ohm sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.6; 28 -1.9; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.6; 45 -2.7; 49 -2.8; 54 -2.7; 60 -2.7; 66 -2.7; 72 -2.9; 79 -3.6; 87 -4.5; 96 -5.4; 106 -6.2; 116 -6.6; 128 -7.1; 141 -7.4; 155 -7.0; 170 -6.9; 187 -7.2; 206 -7.1; 227 -6.7; 249 -6.8; 274 -6.7; 302 -7.0; 332 -7.3; 365 -7.6; 402 -7.9; 442 -8.1; 486 -7.4; 535 -6.3; 588 -6.2; 647 -6.3; 712 -6.5; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.3; 1146 -6.3; 1261 -6.3; 1387 -6.5; 1526 -6.8; 1678 -7.0; 1846 -6.6; 2031 -5.5; 2234 -3.1; 2457 -2.3; 2703 -3.1; 2973 -4.1; 3270 -4.3; 3597 -4.8; 3957 -0.5; 4353 -3.0; 4788 -4.8; 5267 -2.2; 5793 -0.9; 6373 -4.0; 7010 -8.3; 7711 -12.7; 8482 -15.2; 9330 -15.0; 10263 -11.0; 11289 -6.4; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.66 | 4.9 dB   |
| Peaking | 2505 Hz  | 3.92 | 4.3 dB   |
| Peaking | 4051 Hz  | 7.33 | 5.8 dB   |
| Peaking | 5788 Hz  | 3.76 | 6.9 dB   |
| Peaking | 8662 Hz  | 2.68 | -10.6 dB |
| Peaking | 71 Hz    | 1.62 | 3.2 dB   |
| Peaking | 88 Hz    | 0.5  | -1.6 dB  |
| Peaking | 135 Hz   | 2.86 | -0.6 dB  |
| Peaking | 416 Hz   | 3.59 | -1.7 dB  |
| Peaking | 11618 Hz | 5.8  | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sample%201/Beyerdynamic%20T70%20250%20Ohm%20sample%201.png)