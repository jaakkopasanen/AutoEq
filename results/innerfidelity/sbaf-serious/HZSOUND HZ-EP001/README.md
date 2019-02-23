# HZSOUND HZ-EP001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -9.9; 28 -9.9; 31 -9.9; 34 -9.9; 37 -9.8; 41 -9.7; 45 -9.8; 49 -9.8; 54 -9.8; 60 -9.9; 66 -10.1; 72 -10.2; 79 -10.3; 87 -10.6; 96 -10.8; 106 -10.9; 116 -10.9; 128 -11.1; 141 -11.2; 155 -11.4; 170 -11.4; 187 -11.4; 206 -11.3; 227 -11.2; 249 -11.2; 274 -11.1; 302 -11.0; 332 -10.9; 365 -11.1; 402 -10.7; 442 -8.1; 486 -9.0; 535 -8.9; 588 -8.3; 647 -8.1; 712 -7.6; 783 -7.4; 861 -7.3; 947 -7.3; 1042 -7.3; 1146 -7.1; 1261 -7.0; 1387 -7.2; 1526 -7.3; 1678 -7.2; 1846 -6.5; 2031 -6.0; 2234 -5.5; 2457 -4.4; 2703 -4.3; 2973 -4.0; 3270 -3.8; 3597 -5.6; 3957 -6.6; 4353 -6.4; 4788 -4.2; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HZSOUND HZ-EP001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ-EP001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.12 | -3.1 dB |
| Peaking | 240 Hz   | 0.67 | -3.1 dB |
| Peaking | 1058 Hz  | 0.06 | -0.6 dB |
| Peaking | 2768 Hz  | 2.55 | 3.1 dB  |
| Peaking | 5829 Hz  | 3.1  | 7.2 dB  |
| Peaking | 394 Hz   | 6.8  | -2.5 dB |
| Peaking | 427 Hz   | 7.44 | 2.4 dB  |
| Peaking | 4157 Hz  | 5.65 | -3.7 dB |
| Peaking | 4186 Hz  | 2.33 | 1.7 dB  |
| Peaking | 14323 Hz | 2.39 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ-EP001/HZSOUND%20HZ-EP001.png)