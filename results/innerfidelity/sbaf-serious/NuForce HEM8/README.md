# NuForce HEM8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.9; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.6; 106 -9.9; 116 -10.1; 128 -10.5; 141 -10.6; 155 -10.8; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.9; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.3; 365 -10.0; 402 -9.7; 442 -9.2; 486 -8.9; 535 -8.5; 588 -7.7; 647 -7.1; 712 -6.6; 783 -6.1; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.0; 1261 -7.2; 1387 -6.6; 1526 -5.1; 1678 -2.9; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -9.9; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce HEM8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce HEM8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.19 | 1.1 dB  |
| Peaking | 139 Hz  | 0.59 | -0.5 dB |
| Peaking | 199 Hz  | 0.39 | -4.4 dB |
| Peaking | 3595 Hz | 0.57 | 6.9 dB  |
| Peaking | 9176 Hz | 2.94 | -5.5 dB |
| Peaking | 805 Hz  | 2.17 | 1.6 dB  |
| Peaking | 1374 Hz | 1.67 | -3.8 dB |
| Peaking | 1869 Hz | 2.18 | 3.8 dB  |
| Peaking | 3599 Hz | 1.47 | -0.9 dB |
| Peaking | 5377 Hz | 4.03 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20HEM8/NuForce%20HEM8.png)