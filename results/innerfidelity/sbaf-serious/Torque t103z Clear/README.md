# Torque t103z Clear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.4; 25 -7.8; 28 -8.4; 31 -9.0; 34 -9.4; 37 -9.8; 41 -10.2; 45 -10.6; 49 -10.9; 54 -11.3; 60 -11.7; 66 -12.0; 72 -12.4; 79 -12.8; 87 -13.2; 96 -13.5; 106 -13.6; 116 -13.6; 128 -13.8; 141 -13.8; 155 -13.7; 170 -13.5; 187 -13.2; 206 -12.8; 227 -12.4; 249 -12.0; 274 -11.4; 302 -10.8; 332 -10.2; 365 -9.5; 402 -8.9; 442 -8.0; 486 -7.4; 535 -6.7; 588 -5.7; 647 -5.3; 712 -3.8; 783 -3.7; 861 -3.6; 947 -3.6; 1042 -3.7; 1146 -3.6; 1261 -3.7; 1387 -4.0; 1526 -4.3; 1678 -4.5; 1846 -4.3; 2031 -3.9; 2234 -3.8; 2457 -3.7; 2703 -4.6; 2973 -4.3; 3270 -3.1; 3597 -2.5; 3957 -4.1; 4353 -7.9; 4788 -5.9; 5267 -6.3; 5793 -1.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 87 Hz   | 0.38 | -2.6 dB |
| Peaking | 201 Hz  | 0.29 | -6.2 dB |
| Peaking | 796 Hz  | 0.56 | 5.1 dB  |
| Peaking | 3460 Hz | 5.8  | 3.1 dB  |
| Peaking | 6232 Hz | 6.25 | 6.4 dB  |
| Peaking | 1672 Hz | 1.85 | -1.7 dB |
| Peaking | 2000 Hz | 1.31 | 1.8 dB  |
| Peaking | 4845 Hz | 3.2  | -2.4 dB |
| Peaking | 5743 Hz | 9.67 | 2.3 dB  |
| Peaking | 8503 Hz | 5.54 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Clear/Torque%20t103z%20Clear.png)