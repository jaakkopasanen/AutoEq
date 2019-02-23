# Koss QZPro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.2; 41 -2.7; 45 -4.2; 49 -5.5; 54 -7.2; 60 -8.9; 66 -10.5; 72 -11.8; 79 -12.9; 87 -13.6; 96 -13.9; 106 -14.1; 116 -14.1; 128 -14.0; 141 -13.8; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.8; 227 -12.6; 249 -12.4; 274 -12.3; 302 -12.1; 332 -12.0; 365 -11.9; 402 -11.9; 442 -12.2; 486 -12.1; 535 -11.6; 588 -10.9; 647 -10.8; 712 -10.0; 783 -8.7; 861 -9.3; 947 -10.2; 1042 -10.9; 1146 -11.2; 1261 -10.3; 1387 -8.9; 1526 -7.0; 1678 -5.3; 1846 -3.6; 2031 -1.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 34 Hz   | 0.54 | 12.7 dB  |
| Peaking | 84 Hz   | 0.42 | -12.3 dB |
| Peaking | 482 Hz  | 1.01 | -3.7 dB  |
| Peaking | 1205 Hz | 1.87 | -6.4 dB  |
| Peaking | 3043 Hz | 0.6  | 7.3 dB   |
| Peaking | 797 Hz  | 9.61 | 1.0 dB   |
| Peaking | 2180 Hz | 4.31 | 2.0 dB   |
| Peaking | 2742 Hz | 1    | -1.0 dB  |
| Peaking | 6214 Hz | 2.01 | 5.7 dB   |
| Peaking | 7447 Hz | 1.4  | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZPro/Koss%20QZPro.png)