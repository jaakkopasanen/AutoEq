# HiFiMAN RE-262
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.8; 37 -0.9; 41 -1.1; 45 -1.3; 49 -1.4; 54 -1.6; 60 -1.9; 66 -2.4; 72 -2.8; 79 -3.1; 87 -3.6; 96 -4.0; 106 -4.3; 116 -4.7; 128 -5.1; 141 -5.4; 155 -5.7; 170 -5.9; 187 -6.0; 206 -6.3; 227 -6.4; 249 -6.5; 274 -6.6; 302 -6.7; 332 -6.7; 365 -6.7; 402 -6.6; 442 -6.5; 486 -6.6; 535 -6.5; 588 -6.0; 647 -5.8; 712 -5.7; 783 -5.3; 861 -5.6; 947 -6.1; 1042 -6.8; 1146 -7.8; 1261 -9.2; 1387 -10.8; 1526 -12.5; 1678 -13.2; 1846 -11.8; 2031 -8.9; 2234 -5.8; 2457 -2.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-262 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-262 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.59 | 5.6 dB   |
| Peaking | 62 Hz   | 0.96 | 2.5 dB   |
| Peaking | 827 Hz  | 2.73 | 1.5 dB   |
| Peaking | 1688 Hz | 1.81 | -11.1 dB |
| Peaking | 3249 Hz | 0.73 | 8.4 dB   |
| Peaking | 307 Hz  | 1.56 | -0.5 dB  |
| Peaking | 2611 Hz | 6.05 | 2.2 dB   |
| Peaking | 3416 Hz | 1.55 | -1.2 dB  |
| Peaking | 6318 Hz | 2.04 | 5.6 dB   |
| Peaking | 7341 Hz | 1.44 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-262/HiFiMAN%20RE-262.png)