# Torque t402v OnEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.7; 25 -15.0; 28 -15.4; 31 -15.7; 34 -15.9; 37 -16.1; 41 -16.3; 45 -16.4; 49 -16.6; 54 -16.8; 60 -17.0; 66 -17.3; 72 -17.5; 79 -17.7; 87 -18.0; 96 -18.5; 106 -18.9; 116 -19.3; 128 -19.6; 141 -19.8; 155 -19.7; 170 -19.3; 187 -19.4; 206 -19.0; 227 -18.5; 249 -17.9; 274 -17.2; 302 -16.4; 332 -15.9; 365 -15.3; 402 -14.5; 442 -13.7; 486 -12.9; 535 -11.7; 588 -9.8; 647 -7.9; 712 -5.9; 783 -4.1; 861 -3.6; 947 -5.0; 1042 -7.7; 1146 -10.5; 1261 -11.9; 1387 -10.4; 1526 -9.7; 1678 -8.2; 1846 -7.7; 2031 -8.5; 2234 -9.7; 2457 -10.0; 2703 -9.8; 2973 -8.9; 3270 -7.6; 3597 -7.1; 3957 -7.3; 4353 -8.4; 4788 -7.0; 5267 -2.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.28 | -9.3 dB |
| Peaking | 175 Hz  |  0.82 | -8.4 dB |
| Peaking | 365 Hz  |  1.86 | -4.4 dB |
| Peaking | 2425 Hz |  0.91 | -3.0 dB |
| Peaking | 5947 Hz |  3.73 | 7.5 dB  |
| Peaking | 520 Hz  |  3.23 | -2.4 dB |
| Peaking | 850 Hz  |  2.15 | 5.9 dB  |
| Peaking | 1228 Hz |  2.82 | -5.4 dB |
| Peaking | 1827 Hz |  5.41 | 2.0 dB  |
| Peaking | 4444 Hz | 10.42 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -10.7 dB |
| Peaking | 250 Hz   | 1.41 | -10.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Yellow/Torque%20t402v%20OnEar%20Yellow.png)