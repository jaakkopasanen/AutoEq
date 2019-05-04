# Koss QZPro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.1; 41 -2.5; 45 -4.0; 49 -5.4; 54 -7.0; 60 -8.8; 66 -10.3; 72 -11.6; 79 -12.6; 87 -13.3; 96 -13.7; 106 -13.8; 116 -13.8; 128 -13.8; 141 -13.6; 155 -13.4; 170 -13.2; 187 -12.9; 206 -12.6; 227 -12.5; 249 -12.3; 274 -12.2; 302 -12.1; 332 -11.9; 365 -11.7; 402 -11.8; 442 -12.1; 486 -12.1; 535 -11.6; 588 -11.1; 647 -10.9; 712 -10.1; 783 -8.9; 861 -9.4; 947 -10.3; 1042 -11.1; 1146 -11.3; 1261 -10.5; 1387 -9.0; 1526 -7.2; 1678 -5.5; 1846 -3.9; 2031 -1.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZPro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.56 | 12.5 dB  |
| Peaking | 84 Hz   | 0.42 | -11.8 dB |
| Peaking | 488 Hz  | 1.01 | -3.7 dB  |
| Peaking | 1206 Hz | 1.85 | -6.4 dB  |
| Peaking | 3084 Hz | 0.61 | 7.3 dB   |
| Peaking | 262 Hz  | 4.15 | -0.3 dB  |
| Peaking | 2226 Hz | 4.6  | 1.9 dB   |
| Peaking | 2864 Hz | 1.13 | -0.9 dB  |
| Peaking | 6212 Hz | 2.09 | 5.5 dB   |
| Peaking | 7467 Hz | 1.41 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZPro/Koss%20QZPro.png)