# Torque t402v OnEar Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.5; 25 -7.1; 28 -7.9; 31 -8.6; 34 -9.2; 37 -9.7; 41 -10.2; 45 -10.6; 49 -11.0; 54 -11.5; 60 -11.9; 66 -12.3; 72 -12.6; 79 -12.9; 87 -13.1; 96 -13.6; 106 -14.1; 116 -14.5; 128 -14.8; 141 -14.9; 155 -15.0; 170 -14.8; 187 -14.7; 206 -14.6; 227 -14.2; 249 -13.7; 274 -13.1; 302 -12.5; 332 -12.1; 365 -11.6; 402 -10.7; 442 -9.9; 486 -9.3; 535 -8.1; 588 -6.2; 647 -4.3; 712 -2.5; 783 -1.1; 861 -1.3; 947 -2.8; 1042 -5.0; 1146 -7.0; 1261 -8.4; 1387 -7.8; 1526 -8.9; 1678 -7.6; 1846 -6.3; 2031 -6.4; 2234 -7.3; 2457 -7.5; 2703 -7.3; 2973 -6.8; 3270 -5.6; 3597 -5.1; 3957 -5.1; 4353 -6.1; 4788 -5.1; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.52 | -1.1 dB |
| Peaking | 166 Hz  | 0.39 | -8.6 dB |
| Peaking | 810 Hz  | 1.76 | 8.6 dB  |
| Peaking | 1307 Hz | 1.92 | -3.3 dB |
| Peaking | 5839 Hz | 3.33 | 6.8 dB  |
| Peaking | 1937 Hz | 5.18 | 1.7 dB  |
| Peaking | 2729 Hz | 1.38 | -2.6 dB |
| Peaking | 3700 Hz | 1.25 | 3.0 dB  |
| Peaking | 4470 Hz | 5.09 | -2.9 dB |
| Peaking | 8166 Hz | 3.14 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Red/Torque%20t402v%20OnEar%20Red.png)