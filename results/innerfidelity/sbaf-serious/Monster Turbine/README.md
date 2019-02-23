# Monster Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.6; 25 -14.5; 28 -14.3; 31 -14.2; 34 -14.0; 37 -13.9; 41 -13.7; 45 -13.5; 49 -13.3; 54 -13.1; 60 -12.9; 66 -12.7; 72 -12.6; 79 -12.5; 87 -12.4; 96 -12.3; 106 -11.9; 116 -11.6; 128 -11.3; 141 -11.0; 155 -10.6; 170 -10.2; 187 -9.7; 206 -9.2; 227 -8.6; 249 -8.2; 274 -7.6; 302 -6.9; 332 -6.4; 365 -5.8; 402 -5.3; 442 -4.6; 486 -4.2; 535 -3.7; 588 -3.0; 647 -2.7; 712 -2.6; 783 -2.4; 861 -2.6; 947 -3.0; 1042 -3.7; 1146 -3.8; 1261 -4.4; 1387 -4.8; 1526 -5.7; 1678 -6.7; 1846 -7.3; 2031 -7.8; 2234 -8.7; 2457 -9.1; 2703 -9.3; 2973 -8.0; 3270 -5.9; 3597 -4.7; 3957 -5.7; 4353 -8.5; 4788 -9.1; 5267 -6.2; 5793 -2.4; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.54 | -7.3 dB |
| Peaking | 96 Hz   | 0.4  | -5.3 dB |
| Peaking | 714 Hz  | 0.75 | 4.2 dB  |
| Peaking | 2356 Hz | 1.65 | -3.8 dB |
| Peaking | 6296 Hz | 6.3  | 6.3 dB  |
| Peaking | 2804 Hz | 6.19 | -1.4 dB |
| Peaking | 3666 Hz | 2.98 | 3.3 dB  |
| Peaking | 4624 Hz | 3.43 | -4.7 dB |
| Peaking | 5677 Hz | 5.6  | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)