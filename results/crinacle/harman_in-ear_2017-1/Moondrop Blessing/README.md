# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.4; 28 -5.6; 31 -5.7; 34 -5.7; 37 -5.7; 41 -5.7; 45 -5.7; 49 -5.7; 54 -5.6; 60 -5.6; 66 -5.7; 72 -5.8; 79 -5.8; 87 -6.0; 96 -6.2; 106 -6.4; 116 -6.5; 128 -6.6; 141 -6.7; 155 -6.8; 170 -6.8; 187 -6.9; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.6; 302 -6.5; 332 -6.3; 365 -6.1; 402 -5.9; 442 -5.8; 486 -5.7; 535 -5.5; 588 -5.3; 647 -5.1; 712 -4.9; 783 -4.6; 861 -4.5; 947 -4.6; 1042 -5.1; 1146 -5.8; 1261 -6.4; 1387 -6.6; 1526 -6.5; 1678 -6.2; 1846 -6.0; 2031 -5.7; 2234 -5.5; 2457 -5.6; 2703 -5.6; 2973 -5.2; 3270 -4.4; 3597 -4.0; 3957 -4.1; 4353 -4.5; 4788 -4.6; 5267 -4.4; 5793 -3.1; 6373 -0.5; 7010 -2.9; 7711 -5.2; 8482 -5.5; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -12.5; 15026 -24.3; 16529 -29.0; 18182 -27.2; 20000 -25.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 177 Hz   | 0.9  | -1.5 dB  |
| Peaking | 1512 Hz  | 3.3  | -1.3 dB  |
| Peaking | 7151 Hz  | 0.36 | 18.0 dB  |
| Peaking | 12666 Hz | 1.49 | 16.5 dB  |
| Peaking | 15758 Hz | 0.25 | -35.4 dB |
| Peaking | 835 Hz   | 2.8  | 1.4 dB   |
| Peaking | 5352 Hz  | 3.84 | -1.7 dB  |
| Peaking | 6435 Hz  | 4.46 | 4.1 dB   |
| Peaking | 7573 Hz  | 3.3  | -2.1 dB  |
| Peaking | 10234 Hz | 3.99 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -27.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Moondrop%20Blessing/Moondrop%20Blessing.png)