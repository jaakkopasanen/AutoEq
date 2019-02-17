# Bluedio U Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.7; 25 -13.1; 28 -13.4; 31 -13.5; 34 -13.5; 37 -13.5; 41 -13.5; 45 -13.6; 49 -13.7; 54 -13.9; 60 -14.1; 66 -14.3; 72 -14.5; 79 -14.7; 87 -15.0; 96 -15.2; 106 -15.5; 116 -15.7; 128 -15.7; 141 -15.5; 155 -14.9; 170 -13.9; 187 -12.5; 206 -10.8; 227 -8.5; 249 -5.7; 274 -4.0; 302 -2.4; 332 -0.6; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -1.0; 947 -4.7; 1042 -7.2; 1146 -7.3; 1261 -6.7; 1387 -6.8; 1526 -7.5; 1678 -8.3; 1846 -8.2; 2031 -9.1; 2234 -10.7; 2457 -11.7; 2703 -12.5; 2973 -12.7; 3270 -11.9; 3597 -9.3; 3957 -6.2; 4353 -2.7; 4788 -4.9; 5267 -7.7; 5793 -6.5; 6373 -3.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.3; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio U Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio U Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.35 | -6.5 dB |
| Peaking | 111 Hz  | 1.01 | -5.0 dB |
| Peaking | 173 Hz  | 1.42 | -6.1 dB |
| Peaking | 407 Hz  | 0.69 | 8.3 dB  |
| Peaking | 2611 Hz | 1.99 | -6.9 dB |
| Peaking | 838 Hz  | 3.2  | 4.7 dB  |
| Peaking | 1026 Hz | 2.67 | -4.3 dB |
| Peaking | 4387 Hz | 4.74 | 7.2 dB  |
| Peaking | 6085 Hz | 0.94 | -4.3 dB |
| Peaking | 6684 Hz | 3.5  | 8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -10.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB   |
| Peaking | 500 Hz   | 1.41 | 8.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20U%20Plus/Bluedio%20U%20Plus.png)