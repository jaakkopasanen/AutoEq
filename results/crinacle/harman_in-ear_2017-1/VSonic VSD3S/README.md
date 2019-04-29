# VSonic VSD3S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.7; 25 -12.8; 28 -12.9; 31 -13.0; 34 -13.0; 37 -13.0; 41 -13.1; 45 -13.1; 49 -13.1; 54 -13.2; 60 -13.2; 66 -13.3; 72 -13.4; 79 -13.5; 87 -13.7; 96 -13.7; 106 -13.8; 116 -13.8; 128 -13.8; 141 -13.7; 155 -13.5; 170 -13.3; 187 -13.0; 206 -12.6; 227 -12.3; 249 -11.9; 274 -11.5; 302 -11.0; 332 -10.5; 365 -10.0; 402 -9.6; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.2; 783 -6.6; 861 -6.1; 947 -5.7; 1042 -5.4; 1146 -5.3; 1261 -5.0; 1387 -4.2; 1526 -2.9; 1678 -1.6; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.6; 5793 -4.7; 6373 -8.2; 7010 -8.3; 7711 -10.1; 8482 -9.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -17.1; 15026 -21.7; 16529 -23.9; 18182 -25.2; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.55 | -4.6 dB  |
| Peaking | 130 Hz   | 0.34 | -6.8 dB  |
| Peaking | 3011 Hz  | 0.61 | 7.3 dB   |
| Peaking | 17925 Hz | 0.68 | -20.8 dB |
| Peaking | 1860 Hz  | 5.02 | 1.8 dB   |
| Peaking | 5044 Hz  | 2.14 | 6.3 dB   |
| Peaking | 6962 Hz  | 0.87 | -7.9 dB  |
| Peaking | 11698 Hz | 1.08 | 11.2 dB  |
| Peaking | 14371 Hz | 1.78 | -9.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20VSD3S/VSonic%20VSD3S.png)