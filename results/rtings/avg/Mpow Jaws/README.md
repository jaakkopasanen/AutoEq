# Mpow Jaws
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.4; 28 -9.5; 31 -9.5; 34 -9.5; 37 -9.6; 41 -9.7; 45 -9.7; 49 -9.8; 54 -10.0; 60 -10.5; 66 -10.9; 72 -11.3; 79 -11.8; 87 -12.3; 96 -12.9; 106 -13.5; 116 -14.0; 128 -14.6; 141 -15.0; 155 -15.3; 170 -15.3; 187 -15.3; 206 -15.2; 227 -15.0; 249 -14.8; 274 -14.2; 302 -13.2; 332 -12.0; 365 -11.4; 402 -11.2; 442 -11.0; 486 -10.5; 535 -9.7; 588 -8.8; 647 -7.9; 712 -7.0; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.3; 1146 -6.7; 1261 -6.7; 1387 -6.3; 1526 -5.7; 1678 -5.2; 1846 -4.7; 2031 -3.9; 2234 -2.5; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -2.0; 3957 -3.0; 4353 -4.1; 4788 -4.1; 5267 -0.8; 5793 -3.4; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.14 | -2.5 dB |
| Peaking | 133 Hz  | 0.87 | -4.1 dB |
| Peaking | 247 Hz  | 0.78 | -5.8 dB |
| Peaking | 2847 Hz | 1.51 | 6.4 dB  |
| Peaking | 5400 Hz | 5.12 | 4.4 dB  |
| Peaking | 490 Hz  | 4.32 | -1.1 dB |
| Peaking | 792 Hz  | 4.02 | 1.5 dB  |
| Peaking | 6143 Hz | 6.92 | -0.9 dB |
| Peaking | 6748 Hz | 6.47 | 3.3 dB  |
| Peaking | 7479 Hz | 1.71 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Jaws/Mpow%20Jaws.png)