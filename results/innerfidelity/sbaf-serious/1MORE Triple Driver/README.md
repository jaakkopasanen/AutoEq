# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.1; 25 -8.5; 28 -9.0; 31 -9.5; 34 -9.8; 37 -10.1; 41 -10.5; 45 -10.8; 49 -11.1; 54 -11.4; 60 -11.7; 66 -12.0; 72 -12.2; 79 -12.6; 87 -12.9; 96 -13.1; 106 -13.3; 116 -13.2; 128 -13.3; 141 -13.3; 155 -13.2; 170 -13.0; 187 -12.7; 206 -12.4; 227 -12.0; 249 -11.6; 274 -11.1; 302 -10.6; 332 -10.1; 365 -9.6; 402 -9.1; 442 -8.3; 486 -8.0; 535 -7.4; 588 -6.7; 647 -6.3; 712 -6.1; 783 -5.8; 861 -5.9; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.8; 1526 -8.7; 1678 -9.5; 1846 -10.0; 2031 -10.4; 2234 -11.0; 2457 -11.0; 2703 -10.6; 2973 -8.9; 3270 -7.2; 3597 -7.1; 3957 -9.5; 4353 -11.8; 4788 -9.2; 5267 -2.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -9.7; 10263 -10.1; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -9.7; 16529 -11.2; 18182 -8.8; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.48 | -5.7 dB |
| Peaking | 205 Hz   | 0.96 | -3.4 dB |
| Peaking | 2252 Hz  | 1.93 | -4.9 dB |
| Peaking | 4444 Hz  | 5.39 | -6.9 dB |
| Peaking | 5812 Hz  | 3.66 | 7.8 dB  |
| Peaking | 800 Hz   | 2.09 | 1.4 dB  |
| Peaking | 1632 Hz  | 5.48 | -1.1 dB |
| Peaking | 9937 Hz  | 3.08 | -6.1 dB |
| Peaking | 12631 Hz | 0.71 | 3.3 dB  |
| Peaking | 16106 Hz | 1.19 | -6.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)