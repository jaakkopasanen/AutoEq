# Soranic SP3 SE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.4; 25 -7.6; 28 -7.8; 31 -8.0; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.5; 60 -8.6; 66 -8.7; 72 -8.8; 79 -9.0; 87 -9.1; 96 -9.2; 106 -9.3; 116 -9.4; 128 -9.4; 141 -9.4; 155 -9.2; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.5; 249 -8.3; 274 -8.0; 302 -7.7; 332 -7.3; 365 -7.0; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.1; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.3; 861 -5.3; 947 -5.5; 1042 -6.1; 1146 -6.9; 1261 -7.6; 1387 -8.0; 1526 -7.9; 1678 -7.5; 1846 -7.1; 2031 -7.1; 2234 -7.1; 2457 -5.7; 2703 -3.2; 2973 -1.4; 3270 -0.7; 3597 -0.6; 3957 -0.5; 4353 -2.7; 4788 -5.6; 5267 -8.2; 5793 -9.5; 6373 -9.6; 7010 -7.5; 7711 -6.3; 8482 -6.3; 9330 -6.3; 10263 -6.4; 11289 -6.4; 12418 -6.6; 13660 -19.0; 15026 -28.9; 16529 -27.2; 18182 -16.7; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soranic SP3 SE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soranic SP3 SE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 58 Hz    | 0.47 | -1.9 dB  |
| Peaking | 156 Hz   | 0.91 | -2.2 dB  |
| Peaking | 3641 Hz  | 2.19 | 7.1 dB   |
| Peaking | 5705 Hz  | 4.69 | -4.2 dB  |
| Peaking | 15903 Hz | 2.1  | -26.2 dB |
| Peaking | 857 Hz   | 1    | 4.3 dB   |
| Peaking | 1224 Hz  | 0.57 | -3.8 dB  |
| Peaking | 2891 Hz  | 4.69 | 2.8 dB   |
| Peaking | 12482 Hz | 1.63 | 12.0 dB  |
| Peaking | 14226 Hz | 2.1  | -13.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -23.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Soranic%20SP3%20SE/Soranic%20SP3%20SE.png)