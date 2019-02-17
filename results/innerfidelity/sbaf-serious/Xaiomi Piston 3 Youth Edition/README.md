# Xaiomi Piston 3 Youth Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.7; 28 -7.2; 31 -7.7; 34 -8.2; 37 -8.5; 41 -8.8; 45 -9.1; 49 -9.5; 54 -9.8; 60 -10.1; 66 -10.5; 72 -10.8; 79 -11.1; 87 -11.5; 96 -11.8; 106 -11.8; 116 -11.9; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.7; 187 -11.4; 206 -11.1; 227 -10.7; 249 -10.3; 274 -9.8; 302 -9.3; 332 -8.8; 365 -8.2; 402 -7.7; 442 -6.9; 486 -6.5; 535 -6.0; 588 -5.2; 647 -4.7; 712 -4.4; 783 -3.9; 861 -4.0; 947 -4.0; 1042 -4.3; 1146 -4.6; 1261 -5.0; 1387 -5.6; 1526 -6.4; 1678 -7.2; 1846 -7.7; 2031 -8.1; 2234 -8.4; 2457 -8.4; 2703 -8.5; 2973 -7.9; 3270 -6.6; 3597 -6.1; 3957 -7.4; 4353 -10.9; 4788 -13.1; 5267 -9.4; 5793 -4.0; 6373 -0.5; 7010 -1.7; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xaiomi Piston 3 Youth Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xaiomi Piston 3 Youth Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 86 Hz   | 0.44 | -6.5 dB |
| Peaking | 219 Hz  | 0.88 | -3.5 dB |
| Peaking | 2295 Hz | 1.7  | -4.4 dB |
| Peaking | 4800 Hz | 3.74 | -9.6 dB |
| Peaking | 6422 Hz | 4.1  | 5.9 dB  |
| Peaking | 408 Hz  | 2.11 | -0.8 dB |
| Peaking | 819 Hz  | 1.45 | 1.3 dB  |
| Peaking | 1632 Hz | 4.51 | -1.0 dB |
| Peaking | 2896 Hz | 7.18 | -1.0 dB |
| Peaking | 3517 Hz | 7.13 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xaiomi%20Piston%203%20Youth%20Edition/Xaiomi%20Piston%203%20Youth%20Edition.png)