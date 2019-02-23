# Campfire Audio Vega (Foam Eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.6; 28 -12.7; 31 -12.7; 34 -12.7; 37 -12.7; 41 -12.7; 45 -12.7; 49 -12.8; 54 -12.8; 60 -12.9; 66 -13.1; 72 -13.2; 79 -13.4; 87 -13.5; 96 -13.7; 106 -13.8; 116 -13.8; 128 -13.8; 141 -13.7; 155 -13.6; 170 -13.3; 187 -13.0; 206 -12.6; 227 -12.2; 249 -11.7; 274 -11.2; 302 -10.6; 332 -10.0; 365 -9.3; 402 -8.8; 442 -8.2; 486 -7.6; 535 -7.1; 588 -6.5; 647 -6.1; 712 -5.6; 783 -5.2; 861 -5.1; 947 -5.2; 1042 -5.5; 1146 -5.7; 1261 -5.8; 1387 -5.6; 1526 -5.3; 1678 -4.9; 1846 -4.0; 2031 -2.6; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -3.8; 5793 -5.2; 6373 -6.2; 7010 -6.2; 7711 -8.4; 8482 -11.5; 9330 -12.6; 10263 -12.7; 11289 -10.3; 12418 -6.6; 13660 -9.1; 15026 -17.4; 16529 -18.5; 18182 -11.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.22 | -5.9 dB  |
| Peaking | 170 Hz   | 0.73 | -4.4 dB  |
| Peaking | 3300 Hz  | 0.82 | 6.9 dB   |
| Peaking | 9252 Hz  | 2.41 | -7.1 dB  |
| Peaking | 16187 Hz | 1.95 | -14.1 dB |
| Peaking | 804 Hz   | 1.97 | 1.7 dB   |
| Peaking | 1600 Hz  | 1.17 | -1.3 dB  |
| Peaking | 2249 Hz  | 4.81 | 2.1 dB   |
| Peaking | 12795 Hz | 3.42 | 7.1 dB   |
| Peaking | 13673 Hz | 1.3  | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 16000 Hz | 1.41 | -12.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)