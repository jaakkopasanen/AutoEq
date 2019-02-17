# Torque t402v OnEar Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.7; 25 -8.4; 28 -9.2; 31 -9.8; 34 -10.4; 37 -10.9; 41 -11.4; 45 -11.8; 49 -12.3; 54 -12.7; 60 -13.1; 66 -13.4; 72 -13.7; 79 -14.0; 87 -14.4; 96 -15.0; 106 -15.3; 116 -15.5; 128 -15.9; 141 -16.0; 155 -16.0; 170 -15.8; 187 -15.8; 206 -15.6; 227 -15.3; 249 -14.9; 274 -14.4; 302 -13.7; 332 -13.4; 365 -13.1; 402 -12.2; 442 -11.3; 486 -10.4; 535 -9.0; 588 -7.2; 647 -5.5; 712 -3.9; 783 -3.0; 861 -3.7; 947 -5.2; 1042 -7.3; 1146 -8.8; 1261 -9.7; 1387 -9.9; 1526 -11.7; 1678 -11.3; 1846 -9.8; 2031 -9.4; 2234 -10.0; 2457 -10.1; 2703 -9.9; 2973 -9.4; 3270 -8.4; 3597 -8.0; 3957 -8.0; 4353 -9.0; 4788 -8.1; 5267 -3.9; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 97 Hz   | 0.5  | -8.1 dB |
| Peaking | 250 Hz  | 1.1  | -5.3 dB |
| Peaking | 1563 Hz | 4.01 | -4.5 dB |
| Peaking | 2838 Hz | 1.21 | -3.3 dB |
| Peaking | 6053 Hz | 4.29 | 7.4 dB  |
| Peaking | 442 Hz  | 2.33 | -2.4 dB |
| Peaking | 784 Hz  | 2.07 | 5.4 dB  |
| Peaking | 1180 Hz | 2.96 | -2.5 dB |
| Peaking | 4447 Hz | 2.02 | 1.9 dB  |
| Peaking | 4553 Hz | 5.06 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -8.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Black/Torque%20t402v%20OnEar%20Black.png)