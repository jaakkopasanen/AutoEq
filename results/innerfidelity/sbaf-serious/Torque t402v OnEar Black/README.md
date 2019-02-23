# Torque t402v OnEar Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.7; 25 -6.3; 28 -7.1; 31 -7.8; 34 -8.3; 37 -8.8; 41 -9.3; 45 -9.8; 49 -10.2; 54 -10.6; 60 -11.0; 66 -11.3; 72 -11.6; 79 -11.9; 87 -12.3; 96 -12.9; 106 -13.2; 116 -13.4; 128 -13.8; 141 -13.9; 155 -13.9; 170 -13.7; 187 -13.7; 206 -13.5; 227 -13.2; 249 -12.8; 274 -12.3; 302 -11.6; 332 -11.3; 365 -11.0; 402 -10.1; 442 -9.2; 486 -8.3; 535 -6.9; 588 -5.1; 647 -3.4; 712 -1.9; 783 -0.9; 861 -1.6; 947 -3.2; 1042 -5.2; 1146 -6.7; 1261 -7.7; 1387 -7.8; 1526 -9.6; 1678 -9.2; 1846 -7.7; 2031 -7.3; 2234 -7.9; 2457 -8.0; 2703 -7.9; 2973 -7.3; 3270 -6.3; 3597 -5.9; 3957 -5.9; 4353 -6.9; 4788 -6.0; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.53 | -2.6 dB |
| Peaking | 219 Hz  | 0.36 | -5.7 dB |
| Peaking | 785 Hz  | 1.43 | 9.5 dB  |
| Peaking | 1402 Hz | 1    | -3.5 dB |
| Peaking | 5917 Hz | 3.68 | 7.0 dB  |
| Peaking | 19 Hz   | 2.65 | 2.3 dB  |
| Peaking | 1968 Hz | 7.85 | 1.4 dB  |
| Peaking | 3305 Hz | 1.57 | -1.5 dB |
| Peaking | 3475 Hz | 4.09 | 2.3 dB  |
| Peaking | 8457 Hz | 6.4  | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Black/Torque%20t402v%20OnEar%20Black.png)