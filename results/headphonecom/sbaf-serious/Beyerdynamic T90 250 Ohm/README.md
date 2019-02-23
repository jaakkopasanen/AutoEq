# Beyerdynamic T90 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.9; 25 -2.1; 28 -2.3; 31 -2.6; 34 -2.7; 37 -2.9; 41 -2.9; 45 -2.9; 49 -2.9; 54 -2.8; 60 -2.0; 66 -3.4; 72 -4.5; 79 -5.0; 87 -5.3; 96 -5.7; 106 -6.1; 116 -6.4; 128 -6.8; 141 -7.2; 155 -7.4; 170 -7.3; 187 -7.6; 206 -7.6; 227 -7.6; 249 -7.5; 274 -7.4; 302 -7.2; 332 -6.8; 365 -6.5; 402 -5.9; 442 -5.7; 486 -5.3; 535 -4.6; 588 -3.8; 647 -3.6; 712 -2.8; 783 -2.5; 861 -2.1; 947 -2.4; 1042 -2.7; 1146 -2.9; 1261 -3.2; 1387 -4.2; 1526 -4.9; 1678 -5.4; 1846 -6.2; 2031 -6.4; 2234 -6.1; 2457 -6.1; 2703 -6.6; 2973 -7.4; 3270 -7.8; 3597 -7.2; 3957 -7.1; 4353 -6.8; 4788 -0.5; 5267 -1.1; 5793 -3.8; 6373 -10.8; 7010 -11.4; 7711 -12.9; 8482 -14.1; 9330 -13.9; 10263 -12.0; 11289 -10.9; 12418 -10.6; 13660 -7.7; 15026 -6.2; 16529 -9.4; 18182 -12.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.77 | 4.4 dB  |
| Peaking | 928 Hz   | 1.36 | 4.5 dB  |
| Peaking | 5251 Hz  | 3.26 | 11.8 dB |
| Peaking | 7731 Hz  | 0.82 | -8.7 dB |
| Peaking | 17985 Hz | 2.45 | -6.4 dB |
| Peaking | 33 Hz    | 2.88 | -0.8 dB |
| Peaking | 60 Hz    | 3.57 | 2.4 dB  |
| Peaking | 209 Hz   | 0.88 | -1.8 dB |
| Peaking | 594 Hz   | 2.88 | 1.1 dB  |
| Peaking | 14739 Hz | 4.49 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T90%20250%20Ohm/Beyerdynamic%20T90%20250%20Ohm.png)