# Phiaton PS 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.1; 25 -2.7; 28 -3.4; 31 -4.0; 34 -4.6; 37 -5.0; 41 -5.6; 45 -6.1; 49 -6.6; 54 -7.1; 60 -7.7; 66 -8.3; 72 -8.8; 79 -9.4; 87 -10.0; 96 -10.6; 106 -11.0; 116 -11.3; 128 -11.8; 141 -12.2; 155 -12.5; 170 -12.7; 187 -12.9; 206 -13.1; 227 -13.3; 249 -13.5; 274 -13.5; 302 -13.6; 332 -13.6; 365 -13.7; 402 -13.9; 442 -13.5; 486 -13.6; 535 -13.2; 588 -12.4; 647 -11.5; 712 -10.4; 783 -9.0; 861 -7.8; 947 -6.9; 1042 -6.3; 1146 -6.0; 1261 -6.3; 1387 -7.2; 1526 -8.6; 1678 -10.0; 1846 -11.4; 2031 -12.2; 2234 -11.9; 2457 -8.9; 2703 -5.9; 2973 -2.4; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -4.9; 4788 -8.5; 5267 -10.6; 5793 -7.8; 6373 -4.2; 7010 -4.1; 7711 -6.2; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.95 | 5.2 dB   |
| Peaking | 276 Hz  | 0.39 | -7.7 dB  |
| Peaking | 2165 Hz | 2    | -14.4 dB |
| Peaking | 2912 Hz | 0.71 | 10.7 dB  |
| Peaking | 5150 Hz | 3.68 | -9.1 dB  |
| Peaking | 586 Hz  | 1.15 | -5.5 dB  |
| Peaking | 751 Hz  | 0.61 | 4.6 dB   |
| Peaking | 1657 Hz | 2.8  | -2.9 dB  |
| Peaking | 6728 Hz | 5.44 | 3.6 dB   |
| Peaking | 8013 Hz | 1.58 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -6.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%2020/Phiaton%20PS%2020.png)