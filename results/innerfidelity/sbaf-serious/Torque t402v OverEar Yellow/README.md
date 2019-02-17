# Torque t402v OverEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.3; 23 -17.6; 25 -17.8; 28 -18.1; 31 -18.3; 34 -18.5; 37 -18.7; 41 -18.8; 45 -18.9; 49 -19.1; 54 -19.2; 60 -19.1; 66 -19.2; 72 -19.2; 79 -19.3; 87 -20.0; 96 -21.1; 106 -22.1; 116 -22.6; 128 -23.2; 141 -23.6; 155 -23.6; 170 -22.9; 187 -24.0; 206 -23.8; 227 -23.3; 249 -22.4; 274 -21.0; 302 -19.2; 332 -17.3; 365 -15.0; 402 -12.9; 442 -10.7; 486 -8.9; 535 -7.2; 588 -5.2; 647 -3.3; 712 -1.7; 783 -0.5; 861 -1.1; 947 -2.9; 1042 -5.9; 1146 -8.7; 1261 -9.7; 1387 -7.5; 1526 -7.0; 1678 -5.7; 1846 -5.1; 2031 -6.0; 2234 -7.3; 2457 -7.6; 2703 -7.2; 2973 -6.0; 3270 -3.6; 3597 -2.9; 3957 -2.6; 4353 -3.7; 4788 -4.0; 5267 -4.3; 5793 -6.6; 6373 -10.2; 7010 -9.5; 7711 -9.9; 8482 -11.7; 9330 -9.4; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -7.6; 15026 -7.1; 16529 -4.6; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.29 | -13.3 dB |
| Peaking | 145 Hz   | 0.95 | -11.4 dB |
| Peaking | 258 Hz   | 1.61 | -10.8 dB |
| Peaking | 2383 Hz  | 3.97 | -3.1 dB  |
| Peaking | 8018 Hz  | 2.34 | -7.0 dB  |
| Peaking | 384 Hz   | 2.82 | -2.3 dB  |
| Peaking | 799 Hz   | 1.87 | 6.8 dB   |
| Peaking | 1209 Hz  | 2.9  | -6.3 dB  |
| Peaking | 3884 Hz  | 3.58 | 2.7 dB   |
| Peaking | 14435 Hz | 4.51 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.0 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -14.3 dB |
| Peaking | 250 Hz   | 1.41 | -17.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Yellow/Torque%20t402v%20OverEar%20Yellow.png)