# Elysian Minerva
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.2; 28 -7.7; 31 -8.0; 34 -8.3; 37 -8.6; 41 -8.9; 45 -9.2; 49 -9.5; 54 -9.9; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.2; 87 -11.6; 96 -12.0; 106 -12.3; 116 -12.7; 128 -12.9; 141 -13.1; 155 -13.2; 170 -13.2; 187 -13.2; 206 -13.1; 227 -12.9; 249 -12.7; 274 -12.4; 302 -12.0; 332 -11.5; 365 -11.0; 402 -10.5; 442 -10.1; 486 -9.6; 535 -9.2; 588 -8.7; 647 -8.3; 712 -8.0; 783 -7.8; 861 -7.8; 947 -8.2; 1042 -8.8; 1146 -9.3; 1261 -9.2; 1387 -8.1; 1526 -6.7; 1678 -5.2; 1846 -3.7; 2031 -2.3; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -0.6; 6373 -1.2; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -15.5; 15026 -27.1; 16529 -26.0; 18182 -9.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Minerva GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Minerva ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 97 Hz    | 0.44 | -1.6 dB  |
| Peaking | 211 Hz   | 0.38 | -5.8 dB  |
| Peaking | 1274 Hz  | 1.39 | -7.2 dB  |
| Peaking | 2762 Hz  | 0.33 | 7.6 dB   |
| Peaking | 15726 Hz | 2.24 | -25.8 dB |
| Peaking | 18 Hz    | 2.22 | 1.3 dB   |
| Peaking | 6093 Hz  | 3.96 | 3.2 dB   |
| Peaking | 7408 Hz  | 2.09 | -3.3 dB  |
| Peaking | 12586 Hz | 2.59 | 5.9 dB   |
| Peaking | 14495 Hz | 3.57 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Elysian%20Minerva/Elysian%20Minerva.png)