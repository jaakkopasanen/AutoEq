# Xaiomi Piston 3 Youth Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.6; 28 -6.1; 31 -6.6; 34 -7.1; 37 -7.4; 41 -7.7; 45 -8.0; 49 -8.4; 54 -8.7; 60 -9.0; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.4; 96 -10.7; 106 -10.7; 116 -10.8; 128 -10.8; 141 -10.8; 155 -10.7; 170 -10.6; 187 -10.3; 206 -10.0; 227 -9.6; 249 -9.2; 274 -8.7; 302 -8.2; 332 -7.7; 365 -7.1; 402 -6.6; 442 -5.8; 486 -5.4; 535 -4.9; 588 -4.1; 647 -3.6; 712 -3.3; 783 -2.8; 861 -2.9; 947 -2.9; 1042 -3.2; 1146 -3.5; 1261 -3.9; 1387 -4.5; 1526 -5.3; 1678 -6.1; 1846 -6.6; 2031 -7.0; 2234 -7.3; 2457 -7.3; 2703 -7.4; 2973 -6.8; 3270 -5.5; 3597 -5.0; 3957 -6.3; 4353 -9.8; 4788 -12.0; 5267 -8.3; 5793 -2.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xaiomi Piston 3 Youth Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xaiomi Piston 3 Youth Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.79 | -3.1 dB |
| Peaking | 181 Hz  | 0.77 | -3.5 dB |
| Peaking | 804 Hz  | 1.31 | 3.8 dB  |
| Peaking | 4803 Hz | 4.7  | -7.4 dB |
| Peaking | 6229 Hz | 4.69 | 6.9 dB  |
| Peaking | 20 Hz   | 2.14 | 1.6 dB  |
| Peaking | 1259 Hz | 2.86 | 1.2 dB  |
| Peaking | 2414 Hz | 1.28 | -1.9 dB |
| Peaking | 3520 Hz | 4.49 | 2.6 dB  |
| Peaking | 8127 Hz | 6.98 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xaiomi%20Piston%203%20Youth%20Edition/Xaiomi%20Piston%203%20Youth%20Edition.png)