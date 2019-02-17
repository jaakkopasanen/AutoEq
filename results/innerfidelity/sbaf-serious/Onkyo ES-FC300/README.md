# Onkyo ES-FC300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.2; 25 -11.4; 28 -11.5; 31 -11.5; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.8; 49 -12.0; 54 -11.9; 60 -11.5; 66 -11.0; 72 -10.5; 79 -11.2; 87 -12.1; 96 -12.3; 106 -11.7; 116 -12.0; 128 -12.4; 141 -12.3; 155 -11.9; 170 -11.1; 187 -10.6; 206 -9.2; 227 -8.0; 249 -6.8; 274 -6.6; 302 -7.9; 332 -8.7; 365 -9.3; 402 -9.5; 442 -9.3; 486 -9.1; 535 -8.8; 588 -8.3; 647 -8.1; 712 -7.8; 783 -7.3; 861 -7.0; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -5.8; 1387 -5.8; 1526 -6.2; 1678 -6.5; 1846 -6.4; 2031 -5.9; 2234 -5.8; 2457 -5.6; 2703 -6.0; 2973 -5.3; 3270 -4.7; 3597 -4.2; 3957 -1.1; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo ES-FC300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo ES-FC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.51 | -3.7 dB |
| Peaking | 53 Hz   | 0.59 | -4.0 dB |
| Peaking | 135 Hz  | 1.52 | -4.4 dB |
| Peaking | 461 Hz  | 1.86 | -2.7 dB |
| Peaking | 5045 Hz | 1.67 | 6.8 dB  |
| Peaking | 261 Hz  | 6.82 | 1.9 dB  |
| Peaking | 1266 Hz | 4.98 | 0.8 dB  |
| Peaking | 6246 Hz | 5.63 | 2.0 dB  |
| Peaking | 6672 Hz | 4.97 | 1.9 dB  |
| Peaking | 7404 Hz | 1.85 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20ES-FC300/Onkyo%20ES-FC300.png)