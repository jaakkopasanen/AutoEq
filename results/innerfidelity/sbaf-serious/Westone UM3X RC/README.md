# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.1; 28 -6.5; 31 -6.7; 34 -7.0; 37 -7.2; 41 -7.5; 45 -7.8; 49 -8.0; 54 -8.3; 60 -8.7; 66 -9.0; 72 -9.4; 79 -9.9; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.7; 155 -12.0; 170 -12.0; 187 -12.1; 206 -12.1; 227 -12.0; 249 -12.0; 274 -11.8; 302 -11.6; 332 -11.3; 365 -11.0; 402 -10.7; 442 -10.2; 486 -10.0; 535 -9.6; 588 -8.9; 647 -8.6; 712 -8.4; 783 -8.0; 861 -8.1; 947 -8.3; 1042 -8.5; 1146 -8.7; 1261 -9.0; 1387 -9.5; 1526 -9.9; 1678 -9.8; 1846 -8.9; 2031 -7.2; 2234 -5.3; 2457 -2.8; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.7; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 107 Hz   | 0.82 | -1.8 dB |
| Peaking | 254 Hz   | 0.45 | -5.1 dB |
| Peaking | 1661 Hz  | 1.17 | -9.1 dB |
| Peaking | 3271 Hz  | 0.42 | 8.9 dB  |
| Peaking | 9345 Hz  | 1.75 | -5.4 dB |
| Peaking | 21 Hz    | 1.79 | 1.3 dB  |
| Peaking | 2743 Hz  | 5.3  | 1.7 dB  |
| Peaking | 4287 Hz  | 0.75 | -0.8 dB |
| Peaking | 6011 Hz  | 4.63 | 2.0 dB  |
| Peaking | 15260 Hz | 2.29 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)