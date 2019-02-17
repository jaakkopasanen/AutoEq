# Koss QZPro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.5; 54 -3.1; 60 -4.8; 66 -6.4; 72 -7.7; 79 -8.8; 87 -9.5; 96 -9.8; 106 -10.0; 116 -10.0; 128 -9.9; 141 -9.7; 155 -9.5; 170 -9.3; 187 -9.0; 206 -8.7; 227 -8.5; 249 -8.3; 274 -8.2; 302 -8.0; 332 -7.9; 365 -7.8; 402 -7.8; 442 -8.1; 486 -8.0; 535 -7.5; 588 -6.8; 647 -6.7; 712 -5.9; 783 -4.6; 861 -5.2; 947 -6.1; 1042 -6.8; 1146 -7.1; 1261 -6.2; 1387 -4.7; 1526 -2.9; 1678 -1.2; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZPro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 47 Hz   | 0.4  | 17.1 dB  |
| Peaking | 79 Hz   | 0.44 | -15.8 dB |
| Peaking | 1185 Hz | 3.14 | -3.8 dB  |
| Peaking | 2250 Hz | 0.71 | 6.4 dB   |
| Peaking | 5236 Hz | 1.98 | 4.5 dB   |
| Peaking | 490 Hz  | 4.32 | -1.0 dB  |
| Peaking | 792 Hz  | 8.4  | 1.5 dB   |
| Peaking | 3881 Hz | 3.16 | 1.3 dB   |
| Peaking | 6386 Hz | 3.82 | 4.6 dB   |
| Peaking | 6819 Hz | 1.31 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZPro/Koss%20QZPro.png)