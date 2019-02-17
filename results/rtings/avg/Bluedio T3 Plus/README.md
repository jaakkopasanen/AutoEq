# Bluedio T3 Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -28.3; 23 -28.5; 25 -28.6; 28 -28.7; 31 -28.7; 34 -28.5; 37 -28.4; 41 -28.2; 45 -28.1; 49 -28.0; 54 -28.1; 60 -28.5; 66 -28.9; 72 -29.2; 79 -29.6; 87 -30.1; 96 -30.6; 106 -31.1; 116 -31.5; 128 -31.9; 141 -31.9; 155 -31.7; 170 -31.4; 187 -30.6; 206 -29.4; 227 -28.0; 249 -26.3; 274 -24.2; 302 -21.8; 332 -19.3; 365 -16.5; 402 -13.2; 442 -10.2; 486 -9.3; 535 -9.6; 588 -7.0; 647 -4.4; 712 -6.5; 783 -4.4; 861 -1.4; 947 -0.5; 1042 -1.6; 1146 -4.5; 1261 -7.8; 1387 -11.2; 1526 -14.6; 1678 -17.0; 1846 -20.9; 2031 -23.7; 2234 -25.3; 2457 -25.7; 2703 -26.3; 2973 -26.5; 3270 -26.4; 3597 -26.0; 3957 -23.4; 4353 -19.5; 4788 -16.3; 5267 -15.2; 5793 -15.2; 6373 -17.1; 7010 -17.0; 7711 -18.5; 8482 -19.8; 9330 -18.8; 10263 -16.5; 11289 -15.7; 12418 -16.6; 13660 -17.8; 15026 -19.4; 16529 -21.7; 18182 -21.6; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T3 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T3 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.2  | -26.4 dB |
| Peaking | 165 Hz   | 0.76 | -19.7 dB |
| Peaking | 2126 Hz  | 2.42 | -14.6 dB |
| Peaking | 3258 Hz  | 1.6  | -17.5 dB |
| Peaking | 17038 Hz | 0.15 | -19.4 dB |
| Peaking | 291 Hz   | 1.81 | -6.3 dB  |
| Peaking | 406 Hz   | 0.73 | 3.2 dB   |
| Peaking | 973 Hz   | 2.65 | 7.0 dB   |
| Peaking | 1547 Hz  | 2.82 | -4.1 dB  |
| Peaking | 8319 Hz  | 5.04 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -30.3 dB |
| Peaking | 62 Hz    | 1.41 | -13.0 dB |
| Peaking | 125 Hz   | 1.41 | -24.1 dB |
| Peaking | 250 Hz   | 1.41 | -20.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -23.9 dB |
| Peaking | 4000 Hz  | 1.41 | -15.2 dB |
| Peaking | 8000 Hz  | 1.41 | -9.3 dB  |
| Peaking | 16000 Hz | 1.41 | -31.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)