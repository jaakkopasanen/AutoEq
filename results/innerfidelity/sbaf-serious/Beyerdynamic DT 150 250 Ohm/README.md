# Beyerdynamic DT 150 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.2; 25 -4.5; 28 -4.9; 31 -5.2; 34 -5.5; 37 -5.7; 41 -5.9; 45 -5.9; 49 -5.9; 54 -5.7; 60 -5.0; 66 -5.1; 72 -5.9; 79 -6.5; 87 -8.1; 96 -9.8; 106 -10.7; 116 -11.1; 128 -11.4; 141 -11.7; 155 -11.4; 170 -10.8; 187 -11.1; 206 -10.2; 227 -9.3; 249 -8.1; 274 -6.7; 302 -5.3; 332 -4.4; 365 -4.3; 402 -4.7; 442 -4.8; 486 -5.0; 535 -5.1; 588 -4.9; 647 -5.0; 712 -5.3; 783 -5.2; 861 -5.4; 947 -5.5; 1042 -5.3; 1146 -5.1; 1261 -5.1; 1387 -5.7; 1526 -6.5; 1678 -7.2; 1846 -7.8; 2031 -8.4; 2234 -8.7; 2457 -7.7; 2703 -6.6; 2973 -4.9; 3270 -3.9; 3597 -2.8; 3957 -4.4; 4353 -8.2; 4788 -7.4; 5267 -5.6; 5793 -5.1; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -6.1; 9330 -9.2; 10263 -6.3; 11289 -5.6; 12418 -5.6; 13660 -7.0; 15026 -7.4; 16529 -5.6; 18182 -5.6; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 150 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 150 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 1.38 | -6.7 dB |
| Peaking | 2142 Hz | 3.36 | -3.0 dB |
| Peaking | 3525 Hz | 3.67 | 5.1 dB  |
| Peaking | 6085 Hz | 0.89 | -5.7 dB |
| Peaking | 6491 Hz | 2.94 | 10.4 dB |
| Peaking | 21 Hz   | 2.09 | 1.9 dB  |
| Peaking | 67 Hz   | 3.34 | 1.3 dB  |
| Peaking | 101 Hz  | 3.26 | -2.4 dB |
| Peaking | 215 Hz  | 1.78 | -5.9 dB |
| Peaking | 238 Hz  | 0.74 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20150%20250%20Ohm/Beyerdynamic%20DT%20150%20250%20Ohm.png)