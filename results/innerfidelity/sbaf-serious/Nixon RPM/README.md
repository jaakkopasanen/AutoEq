# Nixon RPM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.8; 34 -2.8; 37 -3.6; 41 -4.6; 45 -5.3; 49 -5.9; 54 -6.4; 60 -6.6; 66 -7.2; 72 -7.8; 79 -8.1; 87 -8.4; 96 -8.7; 106 -8.5; 116 -8.5; 128 -8.8; 141 -8.8; 155 -8.8; 170 -8.6; 187 -8.6; 206 -8.6; 227 -8.3; 249 -8.3; 274 -8.0; 302 -8.0; 332 -9.1; 365 -8.5; 402 -7.9; 442 -7.6; 486 -7.0; 535 -6.2; 588 -5.7; 647 -5.7; 712 -6.1; 783 -6.2; 861 -6.7; 947 -6.7; 1042 -6.2; 1146 -5.8; 1261 -6.0; 1387 -5.5; 1526 -4.7; 1678 -3.9; 1846 -2.3; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nixon RPM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nixon RPM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.93 | 7.7 dB  |
| Peaking | 224 Hz  | 0.1  | -2.6 dB |
| Peaking | 614 Hz  | 1.88 | 2.7 dB  |
| Peaking | 2707 Hz | 0.83 | 7.6 dB  |
| Peaking | 5769 Hz | 3.45 | 4.4 dB  |
| Peaking | 268 Hz  | 4.88 | 0.6 dB  |
| Peaking | 2093 Hz | 3.57 | 2.6 dB  |
| Peaking | 2178 Hz | 1.4  | -1.6 dB |
| Peaking | 4031 Hz | 5.07 | 1.6 dB  |
| Peaking | 8515 Hz | 3.03 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nixon%20RPM/Nixon%20RPM.png)