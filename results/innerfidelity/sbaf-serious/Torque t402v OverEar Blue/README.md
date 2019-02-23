# Torque t402v OverEar Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.6; 25 -7.2; 28 -8.0; 31 -8.6; 34 -9.1; 37 -9.6; 41 -10.1; 45 -10.5; 49 -10.9; 54 -11.2; 60 -11.6; 66 -11.9; 72 -12.2; 79 -12.4; 87 -12.6; 96 -12.9; 106 -13.7; 116 -14.4; 128 -15.1; 141 -15.4; 155 -15.8; 170 -15.2; 187 -16.3; 206 -16.8; 227 -17.1; 249 -17.3; 274 -17.1; 302 -16.2; 332 -14.8; 365 -12.8; 402 -10.5; 442 -8.1; 486 -6.1; 535 -4.0; 588 -1.4; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.8; 1042 -3.3; 1146 -4.7; 1261 -5.7; 1387 -6.2; 1526 -6.6; 1678 -4.3; 1846 -2.3; 2031 -2.0; 2234 -2.8; 2457 -3.0; 2703 -2.7; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -3.5; 7010 -5.9; 7711 -7.2; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.4  | -6.3 dB |
| Peaking | 277 Hz  | 1.01 | -8.0 dB |
| Peaking | 670 Hz  | 1.27 | 9.3 dB  |
| Peaking | 3412 Hz | 1.29 | 5.7 dB  |
| Peaking | 5313 Hz | 3.46 | 4.3 dB  |
| Peaking | 20 Hz   | 2.66 | 1.9 dB  |
| Peaking | 936 Hz  | 5.59 | 2.6 dB  |
| Peaking | 1539 Hz | 1.62 | -3.4 dB |
| Peaking | 1871 Hz | 3.42 | 4.8 dB  |
| Peaking | 8001 Hz | 4.61 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -12.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Blue/Torque%20t402v%20OverEar%20Blue.png)