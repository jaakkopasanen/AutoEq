# Thinksound ts01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.5; 25 -10.5; 28 -10.6; 31 -10.6; 34 -10.7; 37 -10.7; 41 -10.9; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.5; 66 -11.7; 72 -12.0; 79 -12.3; 87 -12.6; 96 -12.9; 106 -13.0; 116 -13.1; 128 -13.2; 141 -13.3; 155 -13.2; 170 -13.1; 187 -12.9; 206 -12.7; 227 -12.2; 249 -11.9; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.7; 402 -9.1; 442 -8.2; 486 -7.7; 535 -7.0; 588 -6.0; 647 -5.4; 712 -4.8; 783 -4.0; 861 -3.8; 947 -3.6; 1042 -3.7; 1146 -3.1; 1261 -2.8; 1387 -3.1; 1526 -3.3; 1678 -3.4; 1846 -3.2; 2031 -2.9; 2234 -2.8; 2457 -2.8; 2703 -3.1; 2973 -3.0; 3270 -2.0; 3597 -0.6; 3957 -0.5; 4353 -2.3; 4788 -3.6; 5267 -5.4; 5793 -10.6; 6373 -10.2; 7010 -4.2; 7711 -3.4; 8482 -3.7; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound ts01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.2  | -6.5 dB  |
| Peaking | 156 Hz  | 0.67 | -5.6 dB  |
| Peaking | 325 Hz  | 1.19 | -3.2 dB  |
| Peaking | 4337 Hz | 0.75 | 2.8 dB   |
| Peaking | 6016 Hz | 4.71 | -11.0 dB |
| Peaking | 1137 Hz | 1.59 | 1.0 dB   |
| Peaking | 2944 Hz | 5.1  | -1.0 dB  |
| Peaking | 3748 Hz | 5.26 | 2.1 dB   |
| Peaking | 4915 Hz | 0.39 | -0.6 dB  |
| Peaking | 7252 Hz | 7.28 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20ts01/Thinksound%20ts01.png)