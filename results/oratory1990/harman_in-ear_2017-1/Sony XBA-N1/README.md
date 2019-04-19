# Sony XBA-N1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.2; 25 -11.4; 28 -11.7; 31 -11.9; 34 -12.0; 37 -12.2; 41 -12.3; 45 -12.4; 49 -12.4; 54 -12.5; 60 -12.6; 66 -12.7; 72 -12.7; 79 -12.7; 87 -12.7; 96 -12.6; 106 -12.5; 116 -12.9; 128 -13.5; 141 -13.4; 155 -13.1; 170 -12.8; 187 -12.4; 206 -11.9; 227 -11.4; 249 -10.9; 274 -10.4; 302 -9.8; 332 -9.1; 365 -8.5; 402 -7.9; 442 -7.4; 486 -6.9; 535 -6.3; 588 -5.9; 647 -5.5; 712 -5.1; 783 -4.8; 861 -4.8; 947 -5.0; 1042 -5.5; 1146 -5.8; 1261 -6.1; 1387 -6.3; 1526 -6.2; 1678 -6.4; 1846 -5.1; 2031 -3.6; 2234 -3.2; 2457 -2.7; 2703 -2.1; 2973 -0.9; 3270 -0.5; 3597 -1.4; 3957 -2.0; 4353 -2.2; 4788 -2.9; 5267 -2.1; 5793 -1.6; 6373 -3.1; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -8.8; 13660 -15.1; 15026 -24.8; 16529 -28.5; 18182 -22.6; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.35 | -5.7 dB  |
| Peaking | 169 Hz   | 0.93 | -4.4 dB  |
| Peaking | 4783 Hz  | 0.54 | 7.5 dB   |
| Peaking | 11955 Hz | 1.39 | 10.1 dB  |
| Peaking | 16124 Hz | 0.67 | -25.8 dB |
| Peaking | 765 Hz   | 1.99 | 1.8 dB   |
| Peaking | 1547 Hz  | 2.54 | -2.0 dB  |
| Peaking | 3128 Hz  | 2.37 | 2.1 dB   |
| Peaking | 4700 Hz  | 1.48 | -2.0 dB  |
| Peaking | 5803 Hz  | 4.39 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 16000 Hz | 1.41 | -24.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-N1/Sony%20XBA-N1.png)