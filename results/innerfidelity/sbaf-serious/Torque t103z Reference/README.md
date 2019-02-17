# Torque t103z Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.2; 54 -2.0; 60 -2.8; 66 -3.6; 72 -4.3; 79 -5.1; 87 -6.0; 96 -6.9; 106 -7.6; 116 -8.3; 128 -9.1; 141 -9.9; 155 -10.7; 170 -11.4; 187 -12.0; 206 -12.7; 227 -13.2; 249 -13.8; 274 -14.1; 302 -14.2; 332 -13.9; 365 -13.5; 402 -12.8; 442 -11.9; 486 -11.0; 535 -10.1; 588 -8.9; 647 -8.3; 712 -6.8; 783 -6.5; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.0; 1387 -7.5; 1526 -8.2; 1678 -8.7; 1846 -9.0; 2031 -8.9; 2234 -7.9; 2457 -5.5; 2703 -2.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.61 | 6.9 dB   |
| Peaking | 270 Hz  | 0.73 | -8.3 dB  |
| Peaking | 2051 Hz | 1.5  | -10.3 dB |
| Peaking | 2942 Hz | 0.65 | 10.0 dB  |
| Peaking | 426 Hz  | 2.79 | -0.8 dB  |
| Peaking | 771 Hz  | 2.98 | 1.5 dB   |
| Peaking | 1457 Hz | 4.6  | -1.0 dB  |
| Peaking | 6139 Hz | 2.32 | 5.1 dB   |
| Peaking | 7526 Hz | 1.32 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Reference/Torque%20t103z%20Reference.png)