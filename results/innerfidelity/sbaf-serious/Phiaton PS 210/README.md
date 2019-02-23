# Phiaton PS 210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.4; 34 -1.8; 37 -2.2; 41 -2.7; 45 -3.2; 49 -3.6; 54 -4.1; 60 -4.6; 66 -5.1; 72 -5.6; 79 -6.1; 87 -6.6; 96 -7.1; 106 -7.4; 116 -7.7; 128 -8.2; 141 -8.6; 155 -8.8; 170 -9.0; 187 -9.0; 206 -9.2; 227 -9.2; 249 -9.3; 274 -9.3; 302 -9.2; 332 -9.2; 365 -9.0; 402 -9.2; 442 -9.7; 486 -9.1; 535 -8.9; 588 -8.8; 647 -8.7; 712 -8.3; 783 -7.5; 861 -6.7; 947 -6.1; 1042 -5.5; 1146 -5.0; 1261 -5.0; 1387 -5.5; 1526 -6.6; 1678 -7.8; 1846 -9.1; 2031 -10.3; 2234 -11.1; 2457 -9.1; 2703 -5.9; 2973 -2.3; 3270 -0.5; 3597 -0.5; 3957 -2.0; 4353 -6.0; 4788 -5.5; 5267 -5.0; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.54 | 6.1 dB   |
| Peaking | 402 Hz  | 0.29 | -4.0 dB  |
| Peaking | 2022 Hz | 0.45 | 6.7 dB   |
| Peaking | 2168 Hz | 1.7  | -10.7 dB |
| Peaking | 3263 Hz | 3.64 | 5.3 dB   |
| Peaking | 651 Hz  | 2.84 | -1.1 dB  |
| Peaking | 1109 Hz | 0.2  | 0.3 dB   |
| Peaking | 4558 Hz | 7.86 | -3.4 dB  |
| Peaking | 6292 Hz | 4.39 | 5.7 dB   |
| Peaking | 7472 Hz | 1.22 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20210/Phiaton%20PS%20210.png)