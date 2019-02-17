# Monster Turbine-Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.1; 23 -16.1; 25 -16.1; 28 -16.1; 31 -16.2; 34 -16.2; 37 -16.3; 41 -16.3; 45 -16.3; 49 -16.4; 54 -16.6; 60 -16.7; 66 -16.8; 72 -17.0; 79 -17.1; 87 -17.1; 96 -17.1; 106 -17.0; 116 -16.9; 128 -16.8; 141 -16.6; 155 -16.6; 170 -16.4; 187 -16.0; 206 -15.5; 227 -14.9; 249 -14.4; 274 -13.8; 302 -13.1; 332 -12.4; 365 -11.6; 402 -10.9; 442 -10.2; 486 -9.5; 535 -8.8; 588 -8.1; 647 -7.4; 712 -6.9; 783 -6.5; 861 -6.4; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.3; 1387 -8.1; 1526 -9.0; 1678 -9.9; 1846 -10.7; 2031 -10.7; 2234 -10.3; 2457 -9.3; 2703 -7.9; 2973 -6.3; 3270 -4.7; 3597 -4.3; 3957 -5.6; 4353 -6.8; 4788 -5.6; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine-Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine-Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.22 | -9.2 dB |
| Peaking | 134 Hz  | 0.67 | -5.3 dB |
| Peaking | 270 Hz  | 1.16 | -3.4 dB |
| Peaking | 1964 Hz | 2.62 | -4.8 dB |
| Peaking | 5894 Hz | 3.35 | 6.8 dB  |
| Peaking | 836 Hz  | 3    | 1.3 dB  |
| Peaking | 2639 Hz | 2.29 | -2.4 dB |
| Peaking | 3475 Hz | 1.63 | 3.6 dB  |
| Peaking | 4346 Hz | 4.46 | -3.4 dB |
| Peaking | 8174 Hz | 3.79 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine-Pro/Monster%20Turbine-Pro.png)