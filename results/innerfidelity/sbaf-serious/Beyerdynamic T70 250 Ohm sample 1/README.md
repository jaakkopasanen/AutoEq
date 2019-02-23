# Beyerdynamic T70 250 Ohm sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.4; 25 -1.6; 28 -1.8; 31 -2.1; 34 -2.2; 37 -2.4; 41 -2.6; 45 -2.7; 49 -2.7; 54 -2.7; 60 -2.6; 66 -2.6; 72 -2.9; 79 -3.5; 87 -4.5; 96 -5.3; 106 -6.1; 116 -6.5; 128 -7.0; 141 -7.3; 155 -6.9; 170 -6.9; 187 -7.1; 206 -7.1; 227 -6.6; 249 -6.7; 274 -6.6; 302 -6.9; 332 -7.2; 365 -7.5; 402 -7.9; 442 -8.0; 486 -7.3; 535 -6.2; 588 -6.1; 647 -6.3; 712 -6.4; 783 -6.3; 861 -6.4; 947 -6.3; 1042 -6.2; 1146 -6.2; 1261 -6.2; 1387 -6.4; 1526 -6.7; 1678 -6.9; 1846 -6.5; 2031 -5.4; 2234 -3.0; 2457 -2.2; 2703 -3.0; 2973 -4.0; 3270 -4.2; 3597 -4.8; 3957 -0.5; 4353 -2.9; 4788 -4.7; 5267 -2.1; 5793 -0.8; 6373 -4.0; 7010 -8.2; 7711 -12.6; 8482 -15.1; 9330 -15.0; 10263 -11.0; 11289 -6.3; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.66 | 4.9 dB   |
| Peaking | 2505 Hz  | 3.96 | 4.3 dB   |
| Peaking | 4039 Hz  | 7.34 | 5.8 dB   |
| Peaking | 5801 Hz  | 3.76 | 6.9 dB   |
| Peaking | 8672 Hz  | 2.68 | -10.6 dB |
| Peaking | 72 Hz    | 1.61 | 3.3 dB   |
| Peaking | 89 Hz    | 0.52 | -1.8 dB  |
| Peaking | 135 Hz   | 3.52 | -0.6 dB  |
| Peaking | 417 Hz   | 3.55 | -1.7 dB  |
| Peaking | 11558 Hz | 5.8  | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sample%201/Beyerdynamic%20T70%20250%20Ohm%20sample%201.png)