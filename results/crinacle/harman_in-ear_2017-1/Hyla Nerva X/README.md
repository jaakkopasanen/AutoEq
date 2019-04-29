# Hyla Nerva X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.2; 28 -9.5; 31 -9.6; 34 -9.8; 37 -9.9; 41 -10.1; 45 -10.2; 49 -10.2; 54 -10.3; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.1; 87 -11.4; 96 -11.6; 106 -11.8; 116 -12.0; 128 -12.1; 141 -12.2; 155 -12.3; 170 -12.3; 187 -12.2; 206 -12.1; 227 -12.0; 249 -11.8; 274 -11.6; 302 -11.3; 332 -11.0; 365 -10.7; 402 -10.4; 442 -10.1; 486 -9.8; 535 -9.4; 588 -9.0; 647 -8.7; 712 -8.2; 783 -7.8; 861 -7.4; 947 -7.3; 1042 -7.6; 1146 -8.1; 1261 -8.6; 1387 -8.8; 1526 -8.5; 1678 -7.2; 1846 -6.6; 2031 -6.4; 2234 -4.7; 2457 -2.5; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.5; 15026 -22.6; 16529 -26.4; 18182 -25.1; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla Nerva X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla Nerva X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 0.85 | -2.1 dB  |
| Peaking | 222 Hz   | 0.09 | -3.9 dB  |
| Peaking | 8146 Hz  | 0.25 | 12.1 dB  |
| Peaking | 17028 Hz | 0.5  | -27.8 dB |
| Peaking | 1647 Hz  | 1.18 | -7.2 dB  |
| Peaking | 1863 Hz  | 0.53 | 4.6 dB   |
| Peaking | 7964 Hz  | 2.58 | -4.0 dB  |
| Peaking | 12571 Hz | 3.05 | 5.7 dB   |
| Peaking | 14756 Hz | 3.23 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -23.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hyla%20Nerva%20X/Hyla%20Nerva%20X.png)