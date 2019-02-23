# Torque t402v OverEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.2; 25 -13.4; 28 -13.7; 31 -14.0; 34 -14.2; 37 -14.3; 41 -14.4; 45 -14.6; 49 -14.7; 54 -14.8; 60 -14.8; 66 -14.9; 72 -14.8; 79 -14.9; 87 -15.6; 96 -16.7; 106 -17.7; 116 -18.3; 128 -18.8; 141 -19.2; 155 -19.3; 170 -18.6; 187 -19.7; 206 -19.5; 227 -18.9; 249 -18.1; 274 -16.7; 302 -14.8; 332 -12.9; 365 -10.6; 402 -8.6; 442 -6.3; 486 -4.5; 535 -2.8; 588 -0.9; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -1.5; 1146 -4.3; 1261 -5.3; 1387 -3.1; 1526 -2.6; 1678 -1.3; 1846 -0.8; 2031 -1.6; 2234 -3.0; 2457 -3.2; 2703 -2.9; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.3; 6373 -5.8; 7010 -5.1; 7711 -6.2; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 117 Hz  | 0.11 | -5.3 dB  |
| Peaking | 231 Hz  | 0.52 | -13.2 dB |
| Peaking | 592 Hz  | 0.59 | 15.2 dB  |
| Peaking | 4046 Hz | 1.28 | 5.9 dB   |
| Peaking | 27 Hz   | 1.02 | -2.2 dB  |
| Peaking | 1232 Hz | 8.1  | -3.5 dB  |
| Peaking | 1817 Hz | 4.31 | 2.8 dB   |
| Peaking | 5372 Hz | 4.82 | 3.3 dB   |
| Peaking | 6885 Hz | 1.04 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -9.9 dB  |
| Peaking | 250 Hz   | 1.41 | -12.3 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Yellow/Torque%20t402v%20OverEar%20Yellow.png)