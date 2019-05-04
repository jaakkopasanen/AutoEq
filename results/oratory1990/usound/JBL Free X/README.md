# JBL Free X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.4; 28 -11.5; 31 -11.4; 34 -11.4; 37 -11.3; 41 -11.1; 45 -10.9; 49 -10.8; 54 -10.6; 60 -10.5; 66 -10.3; 72 -10.1; 79 -10.0; 87 -9.8; 96 -9.5; 106 -9.1; 116 -8.7; 128 -8.5; 141 -8.2; 155 -7.6; 170 -7.0; 187 -6.5; 206 -6.0; 227 -5.7; 249 -5.4; 274 -5.4; 302 -5.3; 332 -5.2; 365 -5.0; 402 -4.8; 442 -4.7; 486 -4.4; 535 -4.2; 588 -3.9; 647 -3.7; 712 -3.4; 783 -3.2; 861 -3.1; 947 -3.2; 1042 -3.5; 1146 -3.9; 1261 -4.2; 1387 -4.4; 1526 -4.3; 1678 -4.2; 1846 -4.2; 2031 -4.5; 2234 -5.4; 2457 -6.6; 2703 -7.7; 2973 -7.3; 3270 -5.4; 3597 -3.4; 3957 -1.9; 4353 -1.0; 4788 -0.5; 5267 -0.9; 5793 -2.6; 6373 -6.0; 7010 -6.8; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -7.4; 11289 -9.7; 12418 -9.6; 13660 -10.0; 15026 -11.9; 16529 -10.9; 18182 -6.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.25 | -6.7 dB |
| Peaking | 799 Hz   | 0.84 | 1.6 dB  |
| Peaking | 2785 Hz  | 3.58 | -4.0 dB |
| Peaking | 4649 Hz  | 2.37 | 5.2 dB  |
| Peaking | 14872 Hz | 0.95 | -7.2 dB |
| Peaking | 232 Hz   | 4.04 | 0.7 dB  |
| Peaking | 6727 Hz  | 7.03 | -4.1 dB |
| Peaking | 9457 Hz  | 1.16 | 2.3 dB  |
| Peaking | 11107 Hz | 3.52 | -3.6 dB |
| Peaking | 18944 Hz | 3.03 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -8.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/JBL%20Free%20X/JBL%20Free%20X.png)