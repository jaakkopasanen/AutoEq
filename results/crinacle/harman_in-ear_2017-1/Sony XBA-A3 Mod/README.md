# Sony XBA-A3 Mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.7; 25 -6.0; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.6; 49 -7.8; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.7; 96 -10.1; 106 -10.4; 116 -10.6; 128 -10.8; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.6; 206 -10.4; 227 -10.1; 249 -9.9; 274 -9.5; 302 -9.1; 332 -8.5; 365 -8.3; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.6; 588 -7.5; 647 -7.1; 712 -6.5; 783 -6.1; 861 -6.1; 947 -6.2; 1042 -6.7; 1146 -7.5; 1261 -8.3; 1387 -8.6; 1526 -8.4; 1678 -7.8; 1846 -6.7; 2031 -4.9; 2234 -2.8; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.0; 4788 -7.6; 5267 -4.3; 5793 -2.1; 6373 -4.8; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -9.0; 11289 -10.1; 12418 -12.5; 13660 -19.7; 15026 -26.3; 16529 -28.3; 18182 -26.1; 20000 -17.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 Mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 Mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 153 Hz   | 0.55 | -4.5 dB  |
| Peaking | 1642 Hz  | 1.39 | -7.2 dB  |
| Peaking | 2657 Hz  | 0.72 | 9.7 dB   |
| Peaking | 10196 Hz | 0.57 | 13.2 dB  |
| Peaking | 16099 Hz | 0.41 | -28.4 dB |
| Peaking | 20 Hz    | 1.73 | 1.7 dB   |
| Peaking | 3082 Hz  | 2.25 | -0.2 dB  |
| Peaking | 4009 Hz  | 4.04 | 2.9 dB   |
| Peaking | 4779 Hz  | 4.22 | -5.9 dB  |
| Peaking | 5628 Hz  | 5.13 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 16000 Hz | 1.41 | -29.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-A3%20Mod/Sony%20XBA-A3%20Mod.png)