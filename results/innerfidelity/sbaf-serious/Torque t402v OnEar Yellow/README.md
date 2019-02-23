# Torque t402v OnEar Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.8; 25 -12.1; 28 -12.4; 31 -12.7; 34 -12.9; 37 -13.1; 41 -13.3; 45 -13.4; 49 -13.6; 54 -13.8; 60 -14.0; 66 -14.3; 72 -14.6; 79 -14.7; 87 -15.1; 96 -15.6; 106 -16.0; 116 -16.3; 128 -16.6; 141 -16.8; 155 -16.8; 170 -16.4; 187 -16.4; 206 -16.1; 227 -15.5; 249 -14.9; 274 -14.2; 302 -13.4; 332 -12.9; 365 -12.4; 402 -11.6; 442 -10.7; 486 -10.0; 535 -8.7; 588 -6.8; 647 -4.9; 712 -3.0; 783 -1.1; 861 -0.7; 947 -2.0; 1042 -4.7; 1146 -7.6; 1261 -9.0; 1387 -7.4; 1526 -6.7; 1678 -5.3; 1846 -4.7; 2031 -5.5; 2234 -6.7; 2457 -7.1; 2703 -6.8; 2973 -6.0; 3270 -4.6; 3597 -4.2; 3957 -4.3; 4353 -5.4; 4788 -4.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.55 | -4.2 dB |
| Peaking | 160 Hz  | 0.41 | -9.9 dB |
| Peaking | 800 Hz  | 2.57 | 8.4 dB  |
| Peaking | 5715 Hz | 2.71 | 6.6 dB  |
| Peaking | 963 Hz  | 5.73 | 2.0 dB  |
| Peaking | 1237 Hz | 4.22 | -3.0 dB |
| Peaking | 1831 Hz | 3.38 | 2.9 dB  |
| Peaking | 2898 Hz | 0.94 | -1.9 dB |
| Peaking | 3454 Hz | 3.19 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Yellow/Torque%20t402v%20OnEar%20Yellow.png)