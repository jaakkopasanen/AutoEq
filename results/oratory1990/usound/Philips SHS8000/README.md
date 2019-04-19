# Philips SHS8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -2.0; 34 -2.2; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.6; 60 -4.0; 66 -4.3; 72 -4.7; 79 -5.0; 87 -5.5; 96 -5.9; 106 -6.2; 116 -6.6; 128 -6.8; 141 -7.1; 155 -7.2; 170 -7.2; 187 -7.2; 206 -7.1; 227 -6.9; 249 -6.7; 274 -6.5; 302 -6.2; 332 -5.8; 365 -5.7; 402 -5.5; 442 -5.2; 486 -4.8; 535 -4.5; 588 -4.2; 647 -3.8; 712 -3.5; 783 -3.3; 861 -3.1; 947 -3.3; 1042 -3.6; 1146 -4.1; 1261 -4.6; 1387 -4.9; 1526 -5.1; 1678 -5.2; 1846 -5.4; 2031 -6.0; 2234 -7.3; 2457 -9.1; 2703 -10.9; 2973 -11.0; 3270 -9.2; 3597 -7.3; 3957 -6.3; 4353 -6.1; 4788 -7.9; 5267 -9.1; 5793 -6.6; 6373 -4.3; 7010 -5.0; 7711 -8.2; 8482 -7.7; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHS8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHS8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.32 | 5.4 dB  |
| Peaking | 46 Hz    | 1.93 | 2.2 dB  |
| Peaking | 875 Hz   | 1.2  | 3.1 dB  |
| Peaking | 2840 Hz  | 3.16 | -5.7 dB |
| Peaking | 21125 Hz | 2.11 | -0.6 dB |
| Peaking | 174 Hz   | 1.49 | -1.6 dB |
| Peaking | 4235 Hz  | 4.27 | 1.5 dB  |
| Peaking | 5219 Hz  | 3.74 | -4.5 dB |
| Peaking | 6505 Hz  | 2.53 | 3.4 dB  |
| Peaking | 7934 Hz  | 5.42 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Philips%20SHS8000/Philips%20SHS8000.png)