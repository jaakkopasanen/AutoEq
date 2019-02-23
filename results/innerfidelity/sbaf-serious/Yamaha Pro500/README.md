# Yamaha Pro500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -2.8; 28 -3.6; 31 -4.1; 34 -4.6; 37 -4.9; 41 -5.3; 45 -5.7; 49 -6.1; 54 -6.4; 60 -6.8; 66 -6.9; 72 -6.3; 79 -7.1; 87 -8.1; 96 -7.9; 106 -8.6; 116 -9.5; 128 -10.1; 141 -10.6; 155 -10.8; 170 -10.5; 187 -11.0; 206 -11.1; 227 -10.8; 249 -10.2; 274 -9.5; 302 -8.7; 332 -7.2; 365 -6.0; 402 -5.1; 442 -4.3; 486 -4.8; 535 -4.9; 588 -5.6; 647 -6.3; 712 -7.2; 783 -7.7; 861 -8.5; 947 -8.3; 1042 -9.1; 1146 -9.3; 1261 -9.4; 1387 -10.3; 1526 -10.6; 1678 -10.5; 1846 -9.3; 2031 -8.0; 2234 -6.7; 2457 -5.0; 2703 -3.4; 2973 -1.9; 3270 -4.2; 3597 -5.6; 3957 -4.6; 4353 -3.6; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.16 | 5.0 dB  |
| Peaking | 171 Hz  | 1.27 | -5.0 dB |
| Peaking | 1509 Hz | 1.67 | -4.6 dB |
| Peaking | 2861 Hz | 3.77 | 4.7 dB  |
| Peaking | 5510 Hz | 2.59 | 6.9 dB  |
| Peaking | 174 Hz  | 3.4  | 2.2 dB  |
| Peaking | 277 Hz  | 0.84 | -3.0 dB |
| Peaking | 430 Hz  | 1.31 | 4.7 dB  |
| Peaking | 862 Hz  | 2.44 | -1.4 dB |
| Peaking | 9081 Hz | 5.76 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro500/Yamaha%20Pro500.png)