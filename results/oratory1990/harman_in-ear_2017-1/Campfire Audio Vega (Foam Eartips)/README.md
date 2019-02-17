# Campfire Audio Vega (Foam Eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.6; 25 -13.7; 28 -13.8; 31 -13.8; 34 -13.8; 37 -13.8; 41 -13.8; 45 -13.8; 49 -13.9; 54 -13.9; 60 -14.1; 66 -14.2; 72 -14.3; 79 -14.5; 87 -14.7; 96 -14.8; 106 -14.9; 116 -15.0; 128 -14.9; 141 -14.8; 155 -14.7; 170 -14.4; 187 -14.1; 206 -13.7; 227 -13.3; 249 -12.8; 274 -12.3; 302 -11.8; 332 -11.1; 365 -10.4; 402 -9.9; 442 -9.3; 486 -8.8; 535 -8.2; 588 -7.7; 647 -7.2; 712 -6.7; 783 -6.4; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -6.7; 1526 -6.4; 1678 -6.0; 1846 -5.2; 2031 -3.7; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.5; 5267 -5.0; 5793 -6.3; 6373 -7.3; 7010 -7.3; 7711 -9.5; 8482 -12.6; 9330 -13.8; 10263 -13.8; 11289 -11.4; 12418 -7.2; 13660 -10.2; 15026 -18.5; 16529 -19.6; 18182 -12.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.26 | -7.0 dB |
| Peaking | 139 Hz   | 0.83 | -5.0 dB |
| Peaking | 276 Hz   | 1.37 | -3.0 dB |
| Peaking | 16094 Hz | 2.77 | -6.6 dB |
| Peaking | 16108 Hz | 0.79 | -8.1 dB |
| Peaking | 1521 Hz  | 1.35 | -3.7 dB |
| Peaking | 3449 Hz  | 0.55 | 8.1 dB  |
| Peaking | 5662 Hz  | 3.92 | -2.7 dB |
| Peaking | 9538 Hz  | 1.25 | -8.6 dB |
| Peaking | 12632 Hz | 3.33 | 7.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB  |
| Peaking | 16000 Hz | 1.41 | -13.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)