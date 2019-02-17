# Beyerdynamic DT 880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.2; 45 -2.5; 49 -2.9; 54 -3.4; 60 -3.8; 66 -3.7; 72 -3.8; 79 -4.7; 87 -5.5; 96 -6.1; 106 -6.5; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.8; 170 -7.9; 187 -8.0; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.0; 332 -8.1; 365 -8.0; 402 -7.9; 442 -7.3; 486 -7.2; 535 -7.3; 588 -7.0; 647 -6.9; 712 -6.9; 783 -6.6; 861 -6.9; 947 -6.7; 1042 -6.4; 1146 -6.2; 1261 -5.7; 1387 -5.9; 1526 -6.3; 1678 -6.6; 1846 -6.9; 2031 -6.4; 2234 -5.7; 2457 -4.9; 2703 -4.6; 2973 -4.7; 3270 -5.7; 3597 -6.8; 3957 -6.7; 4353 -6.9; 4788 -6.5; 5267 -7.9; 5793 -9.0; 6373 -8.7; 7010 -9.2; 7711 -12.0; 8482 -14.0; 9330 -13.0; 10263 -8.8; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -7.3; 16529 -7.1; 18182 -9.1; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.55 | 6.1 dB  |
| Peaking | 70 Hz    | 3.4  | 1.3 dB  |
| Peaking | 211 Hz   | 0.63 | -2.0 dB |
| Peaking | 2720 Hz  | 3.54 | 2.4 dB  |
| Peaking | 8518 Hz  | 2.65 | -8.0 dB |
| Peaking | 1300 Hz  | 3.83 | 0.9 dB  |
| Peaking | 1828 Hz  | 6.31 | -0.7 dB |
| Peaking | 5804 Hz  | 7.81 | -1.6 dB |
| Peaking | 11209 Hz | 5.87 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)