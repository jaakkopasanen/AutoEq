# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.1; 60 -2.3; 66 -3.5; 72 -4.5; 79 -5.4; 87 -6.3; 96 -6.9; 106 -7.4; 116 -7.6; 128 -7.6; 141 -7.5; 155 -7.5; 170 -7.4; 187 -7.2; 206 -7.0; 227 -6.8; 249 -6.5; 274 -6.0; 302 -6.0; 332 -6.9; 365 -6.5; 402 -6.3; 442 -6.3; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.5; 1387 -8.5; 1526 -9.6; 1678 -10.6; 1846 -11.6; 2031 -12.2; 2234 -12.8; 2457 -11.8; 2703 -10.6; 2973 -9.2; 3270 -8.2; 3597 -8.1; 3957 -8.4; 4353 -8.7; 4788 -11.9; 5267 -12.2; 5793 -13.8; 6373 -12.7; 7010 -13.1; 7711 -12.6; 8482 -15.2; 9330 -16.8; 10263 -12.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.1; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.25 | 11.4 dB  |
| Peaking | 111 Hz   | 0.52 | -11.4 dB |
| Peaking | 2100 Hz  | 1.93 | -6.3 dB  |
| Peaking | 5974 Hz  | 2.02 | -6.4 dB  |
| Peaking | 9103 Hz  | 3.65 | -9.9 dB  |
| Peaking | 829 Hz   | 1.3  | 1.2 dB   |
| Peaking | 1849 Hz  | 0.17 | -0.5 dB  |
| Peaking | 3621 Hz  | 2.74 | 1.3 dB   |
| Peaking | 11813 Hz | 3.32 | 2.2 dB   |
| Peaking | 19861 Hz | 1.82 | -8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -9.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)