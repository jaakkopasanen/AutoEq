# Campfire Audio Vega (Foam Eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.4; 28 -11.5; 31 -11.6; 34 -11.6; 37 -11.6; 41 -11.6; 45 -11.6; 49 -11.6; 54 -11.7; 60 -11.8; 66 -11.9; 72 -12.1; 79 -12.2; 87 -12.4; 96 -12.5; 106 -12.6; 116 -12.7; 128 -12.7; 141 -12.6; 155 -12.4; 170 -12.2; 187 -11.8; 206 -11.5; 227 -11.0; 249 -10.6; 274 -10.1; 302 -9.5; 332 -9.0; 365 -8.5; 402 -7.9; 442 -7.4; 486 -6.9; 535 -6.3; 588 -5.9; 647 -5.4; 712 -4.9; 783 -4.6; 861 -4.4; 947 -4.4; 1042 -4.7; 1146 -5.0; 1261 -5.3; 1387 -5.4; 1526 -5.4; 1678 -5.0; 1846 -4.2; 2031 -3.1; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.2; 5267 -4.7; 5793 -6.3; 6373 -7.6; 7010 -8.5; 7711 -11.4; 8482 -13.2; 9330 -11.7; 10263 -10.4; 11289 -8.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.32 | -4.8 dB |
| Peaking | 127 Hz   | 0.94 | -4.0 dB |
| Peaking | 235 Hz   | 1.59 | -2.3 dB |
| Peaking | 3430 Hz  | 0.77 | 7.0 dB  |
| Peaking | 8383 Hz  | 1.64 | -8.2 dB |
| Peaking | 832 Hz   | 1.91 | 1.9 dB  |
| Peaking | 1610 Hz  | 1.99 | -1.5 dB |
| Peaking | 2396 Hz  | 5.78 | 1.3 dB  |
| Peaking | 5719 Hz  | 7.97 | -1.2 dB |
| Peaking | 12672 Hz | 4.68 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)