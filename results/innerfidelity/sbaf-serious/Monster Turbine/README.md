# Monster Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.3; 25 -15.2; 28 -15.0; 31 -14.9; 34 -14.7; 37 -14.6; 41 -14.4; 45 -14.2; 49 -14.0; 54 -13.8; 60 -13.6; 66 -13.5; 72 -13.3; 79 -13.2; 87 -13.1; 96 -13.0; 106 -12.7; 116 -12.3; 128 -12.1; 141 -11.7; 155 -11.3; 170 -10.9; 187 -10.4; 206 -9.9; 227 -9.3; 249 -8.9; 274 -8.3; 302 -7.6; 332 -7.1; 365 -6.5; 402 -6.0; 442 -5.3; 486 -4.9; 535 -4.4; 588 -3.7; 647 -3.4; 712 -3.3; 783 -3.1; 861 -3.3; 947 -3.7; 1042 -4.4; 1146 -4.5; 1261 -5.1; 1387 -5.6; 1526 -6.4; 1678 -7.4; 1846 -8.0; 2031 -8.6; 2234 -9.4; 2457 -9.8; 2703 -10.1; 2973 -8.7; 3270 -6.6; 3597 -5.4; 3957 -6.4; 4353 -9.2; 4788 -9.9; 5267 -6.9; 5793 -3.1; 6373 -0.5; 7010 -1.5; 7711 -3.7; 8482 -4.0; 9330 -4.1; 10263 -6.3; 11289 -6.0; 12418 -5.0; 13660 -6.2; 15026 -4.3; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.21 | -11.0 dB |
| Peaking | 155 Hz   | 0.8  | -3.7 dB  |
| Peaking | 2397 Hz  | 1.78 | -6.1 dB  |
| Peaking | 4719 Hz  | 4.55 | -6.0 dB  |
| Peaking | 6484 Hz  | 5.1  | 5.1 dB   |
| Peaking | 740 Hz   | 2.06 | 1.9 dB   |
| Peaking | 1697 Hz  | 3.18 | -1.4 dB  |
| Peaking | 2820 Hz  | 1.73 | 2.0 dB   |
| Peaking | 2840 Hz  | 4.72 | -3.0 dB  |
| Peaking | 11836 Hz | 1.48 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -1.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)